/* M7 Automação — scripts do site
   CONFIG: troque N8N_WEBHOOK pela URL do webhook do n8n para receber cada lead automaticamente.
   Enquanto estiver vazio, o lead é enviado só pelo WhatsApp. */
const M7 = {
  WHATSAPP: "5511968602016", // número do Miguelzinho (assistente da M7)
  N8N_WEBHOOK: "https://m7-automacao-n8n.vmzfbe.easypanel.host/webhook/lead-site"
};

function siteCodigo() {
  const p = location.pathname;
  if (p.includes("ia-para-empresas")) return "SITE-IA";
  if (p.includes("residencial")) return "SITE-RES";
  if (p.includes("condominio")) return "SITE-COND";
  if (p.includes("arquitet")) return "SITE-ARQ";
  return "SITE-HOME";
}

function waLink(text) {
  return "https://wa.me/" + M7.WHATSAPP + "?text=" + encodeURIComponent(text + "\n\n[cod:" + siteCodigo() + "]");
}

async function sendLead(lead) {
  if (!M7.N8N_WEBHOOK) return false;
  try {
    const r = await fetch(M7.N8N_WEBHOOK, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ ...lead, pagina: location.pathname, origem: document.referrer || "direto", data: new Date().toISOString() })
    });
    return r.ok;
  } catch (e) { return false; }
}

/* Menu mobile */
document.addEventListener("click", (e) => {
  const b = e.target.closest(".menu-btn");
  if (!b) return;
  const nav = document.getElementById("nav");
  const open = nav.classList.toggle("open");
  b.setAttribute("aria-expanded", String(open));
  b.textContent = open ? "Fechar" : "Menu";
});

/* Links de WhatsApp com mensagem por página */
document.querySelectorAll("[data-wa]").forEach((a) => {
  a.href = waLink(a.dataset.wa || "Olá! Vim pelo site da M7 Automação.");
  a.target = "_blank"; a.rel = "noopener";
});

/* Formulários de lead */
document.querySelectorAll("form.lead-form").forEach((form) => {
  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const data = Object.fromEntries(new FormData(form).entries());
    const assunto = form.dataset.assunto || "Contato pelo site";
    const linhas = [assunto, ""];
    for (const [k, v] of Object.entries(data)) if (v) linhas.push(k.charAt(0).toUpperCase() + k.slice(1) + ": " + v);
    const btn = form.querySelector("button[type=submit], button:not([type])");
    if (btn) btn.disabled = true;
    const enviado = await sendLead({ tipo: assunto, ...data });
    const ok = form.querySelector(".form-ok");
    const link = waLink(linhas.join("\n"));
    const primeiro = data.nome ? data.nome.split(" ")[0] : "";
    if (enviado) {
      if (ok) {
        ok.hidden = false;
        ok.innerHTML = "Pronto, " + primeiro + "! O Miguelzinho, assistente da M7, vai te chamar no WhatsApp em instantes (das 8h às 20h). Se preferir, <a href=\"" + link + "\" target=\"_blank\" rel=\"noopener\"><strong>chame você agora</strong></a>.";
      }
      form.querySelectorAll("input, select, textarea").forEach((el) => { el.disabled = true; });
    } else {
      if (btn) btn.disabled = false;
      if (ok) {
        ok.hidden = false;
        ok.innerHTML = "Recebemos seus dados, " + primeiro + ". Para agilizar, <a href=\"" + link + "\" target=\"_blank\" rel=\"noopener\"><strong>toque aqui e envie a mensagem no WhatsApp</strong></a>.";
      }
      window.open(link, "_blank", "noopener");
    }
  });
});

/* Painel de casa interativo (LP residencial) */
document.querySelectorAll(".tile").forEach((t) => {
  t.addEventListener("click", () => {
    const on = t.getAttribute("aria-pressed") !== "true";
    t.setAttribute("aria-pressed", String(on));
    const s = t.querySelector("small");
    if (s && t.dataset.on) s.textContent = on ? t.dataset.on : t.dataset.off;
  });
});
document.querySelectorAll("[data-scene]").forEach((b) => {
  b.addEventListener("click", () => {
    const want = b.dataset.scene;
    document.querySelectorAll(".tile").forEach((t) => {
      const on = (t.dataset.scenes || "").split(",").includes(want);
      t.setAttribute("aria-pressed", String(on));
      const s = t.querySelector("small");
      if (s && t.dataset.on) s.textContent = on ? t.dataset.on : t.dataset.off;
    });
    const lbl = document.getElementById("scene-name");
    if (lbl) lbl.textContent = b.dataset.label || want;
  });
});

/* ===== Assistente M7 =====
   Conversa guiada que qualifica o visitante e entrega o resumo no WhatsApp (e no n8n, se configurado).
   Cada fluxo é uma lista de perguntas; "opts" mostra botões, sem "opts" aceita texto livre. */
const FLOWS = {
  geral: [
    { k: "frente", q: "Oi! Eu sou o assistente da M7. Em 1 minuto entendo o que você precisa e já te conecto com um especialista. Por onde começamos?", opts: ["Automatizar minha empresa com IA", "Automatizar minha casa", "Sou de um condomínio", "Sou arquiteto(a)"] },
    { k: "detalhe", when: (a) => a.frente.includes("empresa"), q: "Boa! O que mais toma tempo da sua equipe hoje?", opts: ["Responder clientes no WhatsApp", "Agenda e confirmações", "Orçamentos e propostas", "Planilhas e tarefas manuais"] },
    { k: "detalhe", when: (a) => a.frente.includes("casa"), q: "Legal! O que você quer controlar primeiro?", opts: ["Iluminação e cenas", "Som e home theater", "Segurança e câmeras", "Wi-Fi que funcione na casa toda"] },
    { k: "detalhe", when: (a) => a.frente.includes("condom"), q: "Entendi. Qual é a prioridade do condomínio?", opts: ["Controle de acesso", "Câmeras e segurança", "Economia de energia nas áreas comuns", "Atendimento a moradores com IA"] },
    { k: "detalhe", when: (a) => a.frente.includes("arquitet"), q: "Que bom ter você aqui. Em que fase está o projeto?", opts: ["Ainda na planta", "Obra em andamento", "Quero parceria para vários projetos"] },
    { k: "porte", when: (a) => a.frente.includes("empresa"), q: "Quantas pessoas trabalham na empresa?", opts: ["Só eu", "2 a 10", "11 a 50", "Mais de 50"] },
    { k: "local", when: (a) => !a.frente.includes("empresa"), q: "Em qual cidade ou bairro fica o imóvel?" },
    { k: "nome", q: "Perfeito. Como posso te chamar?" },
    { k: "fim" }
  ],
  ia: [
    { k: "frente", auto: "Automação de processos com IA" },
    { k: "detalhe", q: "Oi! Sou um agente de IA como os que a M7 implanta. Vou fazer seu Raio-X rápido. O que mais trava sua operação hoje?", opts: ["Atendimento no WhatsApp", "Agenda e confirmações", "Orçamentos e propostas", "Planilhas e tarefas manuais"] },
    { k: "volume", q: "Quantas mensagens ou atendimentos vocês recebem por dia, mais ou menos?", opts: ["Até 20", "20 a 100", "Mais de 100", "Não sei medir"] },
    { k: "segmento", q: "Qual é o segmento da empresa?", opts: ["Clínica ou consultório", "Escola", "Comércio ou serviços", "Indústria", "Outro"] },
    { k: "nome", q: "Ótimo, já dá para desenhar algo. Como posso te chamar?" },
    { k: "fim" }
  ],
  casa: [
    { k: "frente", auto: "Automação residencial" },
    { k: "detalhe", q: "Olá! Vamos imaginar sua casa respondendo a você. O que você quer resolver primeiro?", opts: ["Iluminação e cenas", "Som e home theater", "Segurança e câmeras", "Wi-Fi na casa toda", "Tudo integrado"] },
    { k: "fase", q: "Em que momento está o imóvel?", opts: ["Na planta", "Em obra ou reforma", "Pronto, já moro"] },
    { k: "local", q: "Em qual bairro ou cidade fica?" },
    { k: "nome", q: "Como posso te chamar?" },
    { k: "fim" }
  ],
  condominio: [
    { k: "frente", auto: "Automação para condomínio" },
    { k: "detalhe", q: "Olá! Conte para mim: qual é a prioridade do condomínio?", opts: ["Controle de acesso", "Câmeras e segurança", "Economia de energia", "Atendimento a moradores com IA"] },
    { k: "porte", q: "Quantas unidades tem o condomínio?", opts: ["Até 30", "31 a 100", "Mais de 100"] },
    { k: "papel", q: "Você é…", opts: ["Síndico(a)", "Administradora", "Conselho", "Morador(a)"] },
    { k: "nome", q: "Como posso te chamar?" },
    { k: "fim" }
  ],
  arquiteto: [
    { k: "frente", auto: "Parceria com arquiteto(a)" },
    { k: "detalhe", q: "Olá! Que tipo de projeto você tem agora?", opts: ["Residencial de alto padrão", "Apartamento", "Comercial ou corporativo", "Vários, quero parceria contínua"] },
    { k: "fase", q: "Em que fase ele está?", opts: ["Estudo preliminar", "Executivo", "Obra em andamento"] },
    { k: "nome", q: "Como posso te chamar?" },
    { k: "fim" }
  ]
};

function initAssistant(root) {
  const flow = FLOWS[root.dataset.flow] || FLOWS.geral;
  const body = root.querySelector(".as-body");
  const opts = root.querySelector(".as-opts");
  const form = root.querySelector(".as-input");
  const input = form.querySelector("input");
  const btn = form.querySelector("button");
  const answers = {};
  let i = -1;

  const scroll = () => { body.scrollTop = body.scrollHeight; };
  const add = (text, who, cls) => {
    const d = document.createElement("div");
    d.className = "msg " + who + (cls ? " " + cls : "");
    d.textContent = text;
    body.appendChild(d); scroll();
    return d;
  };
  const typing = (ms) => new Promise((res) => {
    const t = document.createElement("div");
    t.className = "msg bot typing"; t.innerHTML = "<i></i><i></i><i></i>";
    body.appendChild(t); scroll();
    setTimeout(() => { t.remove(); res(); }, ms);
  });
  const setText = (on, ph) => {
    input.disabled = !on; btn.disabled = !on;
    input.placeholder = on ? (ph || "Digite aqui…") : "Escolha uma opção acima";
    if (on) input.focus({ preventScroll: true });
  };

  async function next() {
    opts.innerHTML = "";
    i++;
    while (flow[i] && ((flow[i].when && !flow[i].when(answers)) || flow[i].auto)) {
      if (flow[i].auto && !(flow[i].when && !flow[i].when(answers))) answers[flow[i].k] = flow[i].auto;
      i++;
    }
    const step = flow[i];
    if (!step) return;
    if (step.k === "fim") return finish();
    await typing(i === 0 ? 500 : 700);
    add(step.q, "bot");
    if (step.opts) {
      setText(false);
      step.opts.forEach((o) => {
        const b = document.createElement("button");
        b.type = "button"; b.textContent = o;
        b.addEventListener("click", () => answer(o));
        opts.appendChild(b);
      });
      scroll();
    } else {
      setText(true, step.k === "nome" ? "Seu nome" : "Digite aqui…");
    }
  }

  function answer(v) {
    v = String(v).trim();
    if (!v) return;
    const step = flow[i];
    answers[step.k] = v;
    add(v, "me");
    input.value = "";
    next();
  }

  async function finish() {
    setText(false);
    const nome = (answers.nome || "").split(" ")[0];
    await typing(900);
    add("Obrigado, " + nome + "! Organizei o seu pedido assim:", "bot");
    const labels = { frente: "Interesse", detalhe: "Prioridade", porte: "Porte", volume: "Volume diário", segmento: "Segmento", local: "Local", fase: "Fase", papel: "Perfil", nome: "Nome" };
    const resumo = Object.entries(answers).map(([k, v]) => (labels[k] || k) + ": " + v).join("\n");
    add(resumo, "bot", "sum");
    sendLead({ tipo: "Assistente do site", ...answers });
    await typing(700);
    add("É isso que um agente de IA da M7 faz no seu atendimento: entende, qualifica e entrega pronto para a equipe. Toque abaixo para falar com um especialista.", "bot");
    const a = document.createElement("a");
    a.className = "btn btn-wa btn-sm";
    a.href = waLink("Olá! Usei o assistente do site da M7.\n\n" + resumo);
    a.target = "_blank"; a.rel = "noopener";
    a.innerHTML = WA_ICON + " Enviar no WhatsApp";
    const r = document.createElement("button");
    r.type = "button"; r.textContent = "Recomeçar";
    r.addEventListener("click", () => { body.innerHTML = ""; for (const k in answers) delete answers[k]; i = -1; next(); });
    opts.innerHTML = ""; opts.append(a, r);
    scroll();
  }

  form.addEventListener("submit", (e) => { e.preventDefault(); if (!input.disabled) answer(input.value); });
  next();
}

const WA_ICON = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2c-1.5 0-3-.4-4.3-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.2-.4.3-.4.8-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.3-.2-.5-.3Z"/></svg>';

document.querySelectorAll(".assistant").forEach(initAssistant);
document.querySelectorAll(".wa-icon").forEach((s) => { s.outerHTML = WA_ICON; });
