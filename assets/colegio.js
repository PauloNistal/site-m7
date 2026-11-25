// IA no Colégio: efeitos das 3 versões (texto que se decifra, holofote, contadores, chat, terminal, linha do tempo).
(() => {
  const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const onView = (el, fn, th = 0.35) => {
    if (!("IntersectionObserver" in window)) return fn();
    const io = new IntersectionObserver((es) => es.forEach((e) => { if (e.isIntersecting) { io.disconnect(); fn(); } }), { threshold: th });
    io.observe(el);
  };

  // v1: texto que se decifra e troca de frase
  document.querySelectorAll("[data-scramble]").forEach((el) => {
    const list = el.dataset.scramble.split("|"); if (reduce || list.length < 2) return;
    const chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#*+<>/";
    let i = 0;
    const to = (txt) => {
      const from = el.textContent, len = Math.max(from.length, txt.length); let f = 0;
      const tick = () => {
        let out = "";
        for (let k = 0; k < len; k++) {
          const done = k < f / 2;
          out += done ? (txt[k] || "") : (k < txt.length ? (txt[k] === " " ? " " : chars[(Math.random() * chars.length) | 0]) : "");
        }
        el.textContent = out; f++;
        if (f / 2 < len) requestAnimationFrame(tick); else el.textContent = txt;
      };
      tick();
    };
    setInterval(() => { i = (i + 1) % list.length; to(list[i]); }, 3200);
  });

  // v1: holofote que segue o mouse nos cards
  document.querySelectorAll("[data-spot]").forEach((grid) => {
    grid.addEventListener("pointermove", (e) => {
      grid.querySelectorAll(".cv-spot").forEach((c) => {
        const r = c.getBoundingClientRect();
        c.style.setProperty("--mx", e.clientX - r.left + "px");
        c.style.setProperty("--my", e.clientY - r.top + "px");
      });
    });
  });

  // contadores
  document.querySelectorAll("[data-count]").forEach((el) => {
    const n = +el.dataset.count; if (reduce) return;
    el.textContent = "0";
    onView(el, () => {
      const t0 = performance.now(), dur = 1200;
      const step = (t) => { const p = Math.min(1, (t - t0) / dur); el.textContent = Math.round(n * (1 - Math.pow(1 - p, 3))); if (p < 1) requestAnimationFrame(step); };
      requestAnimationFrame(step);
    });
  });

  // v2: chat que aparece mensagem por mensagem
  document.querySelectorAll("[data-chat]").forEach((box) => {
    const msgs = [...box.querySelectorAll(".cv-msg")];
    if (reduce) return msgs.forEach((m) => m.classList.add("show"));
    onView(box, () => msgs.forEach((m, k) => setTimeout(() => m.classList.add("show"), 600 + k * 1100)), 0.2);
  });

  // v3: terminal que digita, risca a regra antiga e escreve a nova
  document.querySelectorAll("[data-term]").forEach((pre) => {
    const lines = [...pre.querySelectorAll("span")];
    if (reduce) return;
    const texts = lines.map((l) => l.textContent);
    lines.forEach((l) => { l.textContent = ""; l.style.minHeight = "1.8em"; });
    const caret = document.createElement("i"); caret.className = "cv-caret";
    const run = () => {
      let li = 0;
      const typeLine = () => {
        if (li >= lines.length) return;
        const el = lines[li], txt = texts[li]; let c = 0; el.appendChild(caret);
        const t = setInterval(() => {
          c++; el.textContent = txt.slice(0, c); el.appendChild(caret);
          if (c >= txt.length) {
            clearInterval(t);
            if (li === 2) { lines[1].classList.add("del"); lines[2].classList.add("del"); }
            li++; setTimeout(typeLine, li === 3 ? 700 : 260);
          }
        }, 26);
      };
      typeLine();
    };
    onView(pre, run, 0.3);
  });

  // v3: feixe da linha do tempo acompanha a rolagem
  document.querySelectorAll("[data-tl]").forEach((tl) => {
    const bar = tl.querySelector(".cv-tl-line"), items = [...tl.querySelectorAll(".cv-tl-item")];
    const upd = () => {
      const r = tl.getBoundingClientRect(), mid = innerHeight * 0.6;
      const p = Math.max(0, Math.min(1, (mid - r.top) / r.height));
      bar.style.setProperty("--p", p * 100 + "%");
      items.forEach((it) => { const ir = it.getBoundingClientRect(); it.classList.toggle("lit", ir.top + 30 < mid); });
    };
    addEventListener("scroll", upd, { passive: true }); addEventListener("resize", upd); upd();
  });
})();
