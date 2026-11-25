# IA no Colégio: 3 versões da landing para o Paulo escolher (25/11/2026).
# Todas seguem a identidade do site (fundo escuro, Syne, azul gelo e vermelho M7) e mudam o efeito principal:
#   v1 "Desbloqueio": partículas formam o capelo e o M7, texto que se decifra, cards com holofote no mouse.
#   v2 "Aurora": luz de palco com aurora, título que surge do desfoque, chat que mostra o método, bento com borda brilhante.
#   v3 "Código": grade com feixes de luz, terminal que reescreve a regra, faixa rolante, trilhas numa linha do tempo.
# Sem preço (apresentação comercial). CTA: agendar conversa (WhatsApp com código SITE-COLEGIO pelo app.js).

CSS = '<link rel="stylesheet" href="/assets/colegio.css"><script src="/assets/colegio.js" defer></script>'

IC = {
 "exp": '<path d="M12 3l1.8 4.6L18 9l-4.2 1.4L12 15l-1.8-4.6L6 9l4.2-1.4z"/><path d="M19 15l.8 2.2L22 18l-2.2.8L19 21l-.8-2.2L16 18l2.2-.8z"/><path d="M5 15l.6 1.4L7 17l-1.4.6L5 19l-.6-1.4L3 17l1.4-.6z"/>',
 "cri": '<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20.5l1.4-5A8 8 0 1 1 21 12z"/><path d="M8.5 12h.01M12 12h.01M15.5 12h.01"/>',
 "fut": '<path d="M5 19c1-3 3-4.5 5-5M14 4c3.5 0 6 2.5 6 6-1.5 3.5-5 7-9 8l-5-5c1-4 4.5-7.5 8-9z"/><circle cx="14.5" cy="9.5" r="1.6"/><path d="M6.5 14.5 4 17l3 3 2.5-2.5"/>',
 "pro": '<path d="M3 5h11a3 3 0 0 1 3 3v11H6a3 3 0 0 1-3-3z"/><path d="M17 8h4v11h-4"/><path d="M7 9h6M7 13h4"/>',
 "lock": '<rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>',
 "pen": '<path d="M4 20h4L19 9l-4-4L4 16z"/><path d="M13 7l4 4"/>',
 "eye": '<circle cx="11" cy="11" r="6"/><path d="m20 20-4.3-4.3"/>',
 "book": '<path d="M4 4h7a3 3 0 0 1 3 3v13a2 2 0 0 0-2-2H4z"/><path d="M20 4h-4a2 2 0 0 0-2 2"/><path d="M20 4v14h-6"/>',
}
def ic(k, cls="cv-ic"):
    return f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{IC[k]}</svg>'

TR = [
  ("exp", "3º ao 5º ano", "Exploradores de IA", "Aprender o que é IA brincando, com criatividade e segurança.",
   ["O que é IA (e o que ela não é)", "Histórias e desenhos criados com IA", "Caça aos erros da IA", "O que nunca contar para a IA"],
   "Livro ilustrado da turma, apresentado numa mostra para os pais"),
  ("cri", "6º ao 9º ano", "Criadores de IA", "Usar IA para estudar, criar e pensar criticamente.",
   ["A arte do prompt", "IA como tutor de estudos, não como cola", "Fake news, deepfakes e checagem", "Ética: autoria e uso honesto"],
   "Chatbot ou campanha criativa sobre um tema do colégio"),
  ("fut", "Ensino médio", "IA para o Futuro", "IA aplicada ao vestibular, à carreira e ao empreendedorismo.",
   ["IA para o ENEM e os vestibulares", "Automação e um assistente próprio", "Profissões do futuro", "Dados, LGPD e ética"],
   "Protótipo apresentado num Demo Day aberto aos pais"),
  ("pro", "Professores", "IA na Sala de Aula", "Professores como aliados, ganhando tempo no dia a dia.",
   ["Aulas, provas e rubricas com IA", "Como lidar com alunos que usam IA", "Kit de prompts para o dia a dia", "Guia de uso responsável do colégio"],
   "Imersão de um dia, com o guia de IA do colégio pronto"),
]

def trilha_card(t, i, cls):
    k, age, name, sub, mods, final = t
    lis = "".join(f"<li>{m}</li>" for m in mods)
    return f'''<article class="{cls} cv-tr-{k} reveal" style="--i:{i}">
  <div class="cv-tr-top">{ic(k)}<span class="cv-age">{age}</span></div>
  <h3>{name}</h3><p class="cv-tr-sub">{sub}</p>
  <ul class="cv-mods">{lis}</ul>
  <div class="cv-final"><span>Projeto final</span>{final}</div>
</article>'''


def proibir(v):
    return f'''<section class="x-sec cv-vs-sec">
  <div class="wrap">
    <div class="x-head reveal"><span class="x-label">Por que agora</span><h2 class="x-h2">A IA já está na mochila do aluno. Proibir só faz ele usar <em>escondido</em>.</h2><p class="lead">A pergunta não é se os alunos vão usar inteligência artificial. É se vão usar bem. O IA no Colégio troca a proibição por método.</p></div>
    <div class="cv-vs">
      <div class="cv-vs-col no reveal">
        <span class="cv-vs-tag">Proibir</span>
        <ul><li>O aluno usa em casa, sem ninguém orientar</li><li>Ninguém ensina a checar o que a IA responde</li><li>O professor vira fiscal de cola</li><li>Os pais não veem o colégio preparando para o futuro</li></ul>
      </div>
      <div class="cv-vs-mid" aria-hidden="true"><span>→</span></div>
      <div class="cv-vs-col yes reveal">
        <span class="cv-vs-tag">Ensinar com método</span>
        <ul><li>O aluno usa em aula, com regras claras</li><li>Aprende a duvidar, checar fontes e achar erros da IA</li><li>O professor ganha tempo e vira guia</li><li>O colégio mostra inovação responsável para as famílias</li></ul>
      </div>
    </div>
  </div>
</section>'''


def trilhas(v):
    if v == 1:
        cards = "".join(trilha_card(t, i, "cv-tr cv-spot") for i, t in enumerate(TR))
        grid = f'<div class="cv-tr-grid g1" data-spot>{cards}</div>'
    elif v == 2:
        cards = "".join(trilha_card(t, i, "cv-tr cv-shine") for i, t in enumerate(TR))
        grid = f'<div class="cv-bento">{cards}</div>'
    else:
        cards = "".join(f'<div class="cv-tl-item"><span class="cv-tl-dot" aria-hidden="true"></span>{trilha_card(t, i, "cv-tr cv-tl-card")}</div>' for i, t in enumerate(TR))
        grid = f'<div class="cv-tl" data-tl><div class="cv-tl-line" aria-hidden="true"><i></i></div>{cards}</div>'
    return f'''<section class="x-sec cv-tr-sec" id="trilhas">
  <div class="wrap">
    <div class="x-head reveal"><span class="x-label">A proposta</span><h2 class="x-h2">Quatro trilhas. Uma para cada <em>fase</em> do colégio.</h2><p class="lead">Do 3º ano do fundamental ao ensino médio, e uma trilha para os professores. O colégio escolhe uma trilha ou monta o programa completo.</p></div>
    {grid}
  </div>
</section>'''


def formato(v):
    return f'''<section class="x-sec cv-fmt">
  <div class="wrap">
    <div class="x-head reveal"><span class="x-label">Como funciona</span><h2 class="x-h2">Simples para o colégio. <em>A M7 cuida do resto.</em></h2></div>
    <div class="cv-stats">
      <div class="reveal"><b data-count="50">50</b><small>min</small><span>de aula por semana, por turma</span></div>
      <div class="reveal"><b data-count="12">12</b><small>semanas</small><span>em cada ciclo</span></div>
      <div class="reveal"><b data-count="9">9</b><small>alunos</small><span>no máximo por turma, conforme os computadores</span></div>
      <div class="reveal"><b data-count="3">3</b><small>horas</small><span>de imersão para os professores, num único dia</span></div>
    </div>
    <div class="cv-split">
      <div class="reveal"><span class="x-label">A M7 leva</span><ul><li>Conteúdo e material didático</li><li>As aulas, do primeiro ao último encontro</li><li>A organização da mostra ou do Demo Day</li></ul></div>
      <div class="reveal"><span class="x-label">O colégio oferece</span><ul><li>O espaço e os computadores</li><li>A comunicação com os pais</li><li>Os dias e horários das turmas</li></ul></div>
    </div>
  </div>
</section>'''


def jornada(v):
    return f'''<section class="x-sec cv-jr">
  <div class="wrap">
    <div class="x-head reveal"><span class="x-label">O ciclo</span><h2 class="x-h2">12 semanas que terminam num <em>palco</em>.</h2><p class="lead">No fim de cada ciclo o colégio abre as portas para as famílias verem o que os alunos criaram com IA. É inovação que os pais enxergam e compartilham.</p></div>
    <ol class="cv-steps">
      <li class="reveal"><span>Semana 1</span><h3>Lançamento</h3><p>Palestra para os pais e primeira aula da turma.</p></li>
      <li class="reveal"><span>Semanas 2 a 6</span><h3>Fundamentos</h3><p>Como a IA funciona, prompts, segurança e pensamento crítico.</p></li>
      <li class="reveal"><span>Semanas 7 a 11</span><h3>Mão na massa</h3><p>Cada turma desenvolve o seu projeto, com orientação em toda aula.</p></li>
      <li class="reveal on"><span>Semana 12</span><h3>Mostra ou Demo Day</h3><p>Os alunos apresentam os projetos para os pais e o colégio.</p></li>
    </ol>
    <div class="cv-rules">
      <div class="reveal">{ic("lock")}<h3>Dados protegidos</h3><p>Os alunos aprendem o que nunca compartilhar com a IA.</p></div>
      <div class="reveal">{ic("pen")}<h3>Autoria do aluno</h3><p>A IA ajuda a pensar. Quem faz é o aluno.</p></div>
      <div class="reveal">{ic("eye")}<h3>Pensamento crítico</h3><p>Checar fontes e reconhecer fake news e deepfakes.</p></div>
      <div class="reveal">{ic("book")}<h3>Guia do colégio</h3><p>Regras de uso de IA para alunos e professores.</p></div>
    </div>
  </div>
</section>'''


def ganhos(v):
    return '''<section class="x-sec cv-win-sec">
  <div class="wrap">
    <div class="x-head reveal"><span class="x-label">Quem ganha</span><h2 class="x-h2">Bom para o colégio, para os pais e para os <em>professores</em>.</h2></div>
    <div class="cv-wins">
      <div class="cv-win reveal"><h3>O colégio</h3><ul><li>Diferencial concreto na captação de alunos</li><li>Posição de colégio inovador e responsável</li><li>Conteúdo pronto para o Instagram e as campanhas</li></ul></div>
      <div class="cv-win reveal"><h3>Os pais</h3><ul><li>Veem o que os filhos criaram na mostra e no Demo Day</li><li>Sabem que a IA é usada com segurança</li><li>Filhos preparados para o mundo que já chegou</li></ul></div>
      <div class="cv-win reveal"><h3>Os professores</h3><ul><li>Aulas, provas e rubricas em menos tempo</li><li>Seguros para lidar com alunos que usam IA</li><li>Kit de prompts e guia de uso responsável</li></ul></div>
    </div>
  </div>
</section>'''


def cta(ARROW, lead_form):
    form = lead_form("IA no Colégio (agendar conversa)", """<div class="two"><div class="field"><label for="f-colegio">Colégio</label><input id="f-colegio" name="colegio" autocomplete="organization" placeholder="Nome do colégio"></div><div class="field"><label for="f-cargo">Seu cargo</label><select id="f-cargo" name="cargo"><option value="">Selecione</option><option>Mantenedor(a) / dono(a)</option><option>Diretor(a)</option><option>Coordenador(a)</option><option>Professor(a)</option><option>Outro</option></select></div></div>
  <div class="two"><div class="field"><label for="f-cidade">Cidade</label><input id="f-cidade" name="cidade" placeholder="Ex.: São Paulo"></div><div class="field"><label for="f-trilha">Interesse</label><select id="f-trilha" name="interesse"><option value="">Selecione</option><option>Programa completo</option><option>Exploradores (3º ao 5º)</option><option>Criadores (6º ao 9º)</option><option>IA para o Futuro (médio)</option><option>Imersão de professores</option></select></div></div>""", "Agendar uma conversa")
    return f'''<section class="x-sec cv-cta" id="conversa">
  <div class="wrap cv-cta-grid">
    <div class="stack" style="gap:20px">
      <span class="x-label">Próximo passo</span>
      <h2 class="x-h2">Leve IA para o seu colégio. <em>Agende uma conversa.</em></h2>
      <p class="lead">Em 20 minutos mostramos as trilhas e montamos o formato ideal para o seu colégio: turmas, horários e o calendário do primeiro ciclo.</p>
      <ol class="cv-next"><li>Conversa com a direção para validar as trilhas</li><li>Turmas: dias, horários e tamanho</li><li>Parceria e calendário do ciclo</li><li>Lançamento com palestra para os pais</li></ol>
      <a class="btn btn-glass" data-wa="Olá! Vim pelo site da M7 e quero levar o IA no Colégio para o meu colégio. Podemos agendar uma conversa?">Prefiro falar pelo WhatsApp {ARROW}</a>
    </div>
    <div class="cv-form reveal"><h3>Agende uma conversa</h3>{form}</div>
  </div>
</section>'''


def faqsec(faq, col_faq):
    return f'''<section class="x-sec cv-faq">
  <div class="wrap">
    <div class="x-head"><span class="x-label">Perguntas frequentes</span><h2 class="x-h2">Antes de você perguntar.</h2></div>
    {faq(col_faq)}
    <p class="cv-sign">IA no Colégio é um programa da <a href="ia-para-empresas.html">M7 Automação</a>, especialista em agentes de inteligência artificial.</p>
  </div>
</section>'''


# ---------------- HEROS ----------------
def hero1(ARROW):
    return f'''<section class="x-hero cv-h1" data-shapes="cap,m7">
  <div class="x-grid" aria-hidden="true"></div>
  <canvas id="swarm" aria-hidden="true"></canvas>
  <div class="wrap">
    <div class="x-copy">
      <span class="x-kicker"><i></i><span class="cv-scr" data-scramble="IA no Colégio · curso da M7|IA com criatividade|IA com pensamento crítico|IA com responsabilidade">IA no Colégio · curso da M7</span></span>
      <h1 class="x-title">Muitas escolas <span class="cv-ban">proíbem</span> a IA. Nós <em>ensinamos</em> a usar.</h1>
      <p class="x-sub">Curso extracurricular de inteligência artificial dentro do colégio, do 3º ano do fundamental ao ensino médio, com uma trilha para professores. Criatividade, pensamento crítico e responsabilidade, com projetos que os pais vão ver.</p>
      <div class="x-cta"><a class="btn btn-glow" href="#conversa">Agendar uma conversa {ARROW}</a><a class="btn btn-glass" href="#trilhas">Ver as 4 trilhas</a></div>
    </div>
  </div>
  <div class="x-hint" aria-hidden="true">Passe o mouse<br>sobre as partículas</div>
</section>'''


def hero2(ARROW):
    words = "A IA não é o problema da escola.".split()
    h = " ".join(f'<span style="--d:{i*90}ms">{w}</span>' for i, w in enumerate(words))
    return f'''<section class="cv-h2">
  <div class="cv-aurora" aria-hidden="true"><i></i><i></i><i></i></div>
  <div class="cv-spotlight" aria-hidden="true"></div>
  <div class="wrap cv-h2-in">
    <span class="cv-pill"><b>Novo</b> IA no Colégio · curso extracurricular da M7</span>
    <h1 class="cv-blur">{h}<br><em class="cv-grad" style="--d:700ms">É a aula que faltava.</em></h1>
    <p class="cv-h2-sub">Enquanto muitas escolas proíbem, a M7 leva a inteligência artificial para dentro da sala, com método: do 3º ano do fundamental ao ensino médio, e uma trilha para os professores.</p>
    <div class="x-cta"><a class="btn btn-glow" href="#conversa">Agendar uma conversa {ARROW}</a><a class="btn btn-glass" href="#trilhas">Ver as 4 trilhas</a></div>
    <div class="cv-chat" aria-hidden="true" data-chat>
      <div class="cv-chat-top"><i></i><i></i><i></i><span>Aula de IA · 7º ano</span></div>
      <div class="cv-msg me">Faz minha redação sobre o meio ambiente?</div>
      <div class="cv-msg ai">Fazer por você eu não faço. Mas posso te ajudar a <b>pensar</b> nela. Qual problema do seu bairro você queria resolver?</div>
      <div class="cv-msg me">O lixo na praça perto da escola.</div>
      <div class="cv-msg ai">Ótimo tema. Vamos listar 3 causas e checar uma fonte confiável para cada uma.</div>
    </div>
  </div>
</section>'''


def hero3(ARROW):
    beams = "".join(f'<i style="--x:{x}%;--d:{d}s;--t:{t}s"></i>' for x, d, t in [(12, 0, 6), (31, 2.2, 7), (54, 1.1, 5.5), (73, 3.4, 6.5), (90, .6, 7.5)])
    lines = [
      ('c', '# regulamento do colégio'),
      ('r', '- proibido usar inteligência artificial'),
      ('m', '  resultado: o aluno usa escondido'),
      ('c', '# nova regra, com a M7'),
      ('g', '+ IA em aula, com método'),
      ('g', '+ criatividade'),
      ('g', '+ pensamento crítico'),
      ('g', '+ responsabilidade'),
      ('p', '> iniciar IA no Colégio'),
    ]
    term = "".join(f'<span class="t-{c}">{t}</span>' for c, t in lines)
    return f'''<section class="cv-h3">
  <div class="cv-beams" aria-hidden="true"><div class="cv-g"></div>{beams}</div>
  <div class="wrap cv-h3-grid">
    <div class="stack" style="gap:24px">
      <span class="x-label cv-lbl">IA no Colégio · curso extracurricular da M7</span>
      <h1 class="cv-h3-t">Proibir não é <span class="cv-sweep">plano pedagógico</span>.</h1>
      <p class="lead">A IA já está no celular, nas tarefas e nas pesquisas dos alunos. A M7 leva inteligência artificial para dentro do colégio, do 3º ano do fundamental ao ensino médio, com uma trilha para os professores.</p>
      <div class="x-cta"><a class="btn btn-glow" href="#conversa">Agendar uma conversa {ARROW}</a><a class="btn btn-glass" href="#trilhas">Ver as 4 trilhas</a></div>
    </div>
    <div class="cv-term" aria-hidden="true">
      <div class="cv-term-top"><i></i><i></i><i></i><span>colegio.md</span></div>
      <pre data-term>{term}</pre>
    </div>
  </div>
</section>
<div class="x-marquee" aria-hidden="true"><div class="x-track">
  {"".join(f"<span>{w}</span>" for w in ["A arte do prompt", "Checagem de fontes", "Caça aos erros da IA", "Fake news e deepfakes", "IA para o ENEM", "Ética e autoria", "Dados e LGPD", "Livro da turma", "Demo Day"] * 2)}
</div></div>'''


def build(ARROW, faq, lead_form, col_faq):
    out = {}
    for v, hero in ((1, hero1), (2, hero2), (3, hero3)):
        body = f'''{CSS}
<div class="cv cv{v}">
{hero(ARROW)}
{proibir(v)}
{trilhas(v)}
{jornada(v)}
{formato(v)}
{ganhos(v)}
{cta(ARROW, lead_form)}
{faqsec(faq, col_faq)}
</div>'''
        out[v] = body
    return out
