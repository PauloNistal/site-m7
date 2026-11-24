# Gera as páginas do site M7 a partir de um layout comum.
# Uso: python3 build.py  (gera os .html nesta pasta)
import json, pathlib

ROOT = pathlib.Path(__file__).parent
SITE = "https://www.m7automacao.com.br"
WA = "5511968602016"

LOGO = '''<svg viewBox="196 88 262 302" aria-hidden="true"><path fill="rgb(158,180,213)" d="M 349.5 120 L 368.5 120 L 433.5 160 L 448 174.5 L 452 183.5 L 452 350.5 L 432.5 365 L 422.5 375 Q 418.4 378.9 409.5 378 Q 391.8 373.2 377.5 365 L 328 333.5 L 337.5 330 L 359.5 329 L 372.5 332 L 392.5 346 Q 397.9 350.6 407.5 351 L 415 345.5 L 417 341.5 L 417 317.5 L 418 316.5 L 418 240.5 L 417 237.5 L 418 234.5 L 417 233.5 L 417 186.5 L 414.5 184 L 345.5 143 L 322 127.5 L 324.5 124 L 336.5 121 L 348.5 121 L 349.5 120 Z "></path><path fill="rgb(238,69,83)" d="M 312.5 95 L 323.5 95 L 333.5 98 L 366 118.5 L 347 119.5 L 349 120.5 L 345.5 121 Q 343.8 118.3 337.5 120 Q 336 123.5 334.5 121 Q 329.1 119.1 330 122.5 L 328.5 122 Q 317.2 122.7 310.5 128 L 231.5 179 L 223 186.5 L 222 188.5 L 222 344.5 Q 226.2 349.8 234.5 351 L 244.5 347 L 266.5 332 L 294.5 317 L 297.5 314 L 308.5 309 L 317.5 308 L 318.5 309 L 326.5 309 L 349.5 316 L 362.5 322 L 369 327.5 Q 369.9 330.9 364.5 329 L 360.5 330 L 359.5 329 L 344.5 329 L 332.5 332 L 330.5 332 Q 327.2 330.9 328 333.5 L 328.5 335 Q 326.5 331 324.5 335 L 267.5 370 L 244.5 378 L 225.5 379 L 210.5 375 L 198 365.5 L 191 352.5 L 191 182.5 Q 198.1 165.1 212.5 155 L 246.5 131 L 312.5 95 Z "></path><path fill="rgb(238,69,83)" d="M 441.5 167 L 442.5 169 L 441.5 167 Z "></path><path fill="rgb(238,69,83)" d="M 288.5 188 L 345.5 188 Q 356.8 190.8 363 198.5 L 369 211.5 L 369 265.5 Q 366.3 277.8 357.5 284 L 345.5 289 L 287.5 289 Q 274.9 286.6 269 277.5 L 264 265.5 L 264 212.5 Q 266.4 200.4 274.5 194 L 283.5 189 L 288.5 188 Z "></path><path fill="rgb(238,69,83)" d="M 417.5 234 L 418 236.5 L 417 236.5 L 417.5 234 Z "></path><path fill="rgb(238,69,83)" d="M 417.5 240 L 418 272.5 L 417 272.5 L 417.5 240 Z "></path><path fill="rgb(238,69,83)" d="M 417.5 298 L 418 316.5 L 417 316.5 L 417.5 298 Z "></path><path fill="rgb(238,69,83)" d="M 426.5 371 L 425.5 373 L 426.5 371 Z "></path></svg>'''

ICON = {
 "chat": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12Z"/><path d="M8.5 11h.01M12 11h.01M15.5 11h.01"/></svg>',
 "flow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="6" height="6" rx="1.5"/><rect x="15" y="15" width="6" height="6" rx="1.5"/><path d="M9 6h4a3 3 0 0 1 3 3v6"/></svg>',
 "cal": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4M9 15l2 2 4-4"/></svg>',
 "doc": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9Z"/><path d="M14 3v6h6M8 13h8M8 17h5"/></svg>',
 "chart": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/></svg>',
 "crm": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0M17 11h5M19.5 8.5v5"/></svg>',
 "light": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18h6M10 21h4M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2.1h5c0-.9.4-1.6 1-2.1A6 6 0 0 0 12 3Z"/></svg>',
 "sound": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M11 5 6 9H3v6h3l5 4Z"/><path d="M15.5 8.5a5 5 0 0 1 0 7M18.5 5.5a9 9 0 0 1 0 13"/></svg>',
 "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3 4 6v6c0 4.5 3.4 8.3 8 9 4.6-.7 8-4.5 8-9V6Z"/><path d="m9 12 2 2 4-4"/></svg>',
 "wifi": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M2 8.8a15 15 0 0 1 20 0M5.5 12.4a10 10 0 0 1 13 0M9 16a5 5 0 0 1 6 0M12 19.5h.01"/></svg>',
 "temp": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M14 14.8V4a2 2 0 1 0-4 0v10.8a4 4 0 1 0 4 0Z"/></svg>',
 "blind": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3h18M5 3v14h14V3M5 7h14M5 11h14M5 15h14M12 17v4"/></svg>',
 "key": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><circle cx="8" cy="15" r="4"/><path d="m11 12 9-9M17 6l3 3M15 8l2 2"/></svg>',
 "cam": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M3 7h12a2 2 0 0 1 2 2v1l4-2v8l-4-2v1a2 2 0 0 1-2 2H3Z"/></svg>',
 "leaf": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M4 20c0-9 6-15 16-16-1 10-7 16-16 16Z"/><path d="M4 20 13 11"/></svg>',
 "plan": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3h18v18H3zM3 12h8V3M11 12v9M15 12h6"/></svg>',
 "rack": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="3" width="16" height="18" rx="2"/><path d="M4 9h16M4 15h16M8 6h.01M8 12h.01M8 18h.01"/></svg>',
 "hand": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M7 11 3 15l6 6 4-4M14 4l6 6-7 7-6-6Z"/></svg>',
}
ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
PLAY = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M7 4v16l13-8Z"/></svg>'
SEND = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m22 2-7 20-4-9-9-4Z"/><path d="M22 2 11 13"/></svg>'

NAV = [
  ("index.html", "Início"),
  ("ia-para-empresas.html", "IA para empresas"),
  ("automacao-residencial.html", "Residencial"),
  ("condominios.html", "Condomínios"),
  ("arquitetos.html", "Arquitetos"),
]

VIDEOS = {
  "leandro": ("4ntb9oxkiNE", "5:08", "Depoimento", "Leandro: casa e escritório na temperatura certa ao chegar"),
  "cliente": ("Y41tYD5zo4Q", "7:16", "Depoimento", "A opinião sincera de um cliente que confiou na M7"),
  "pet": ("DMnVOfC9-i8", "1:21", "Funcionalidade", "Cuidar do pet sozinho em casa, pelo celular"),
  "luz": ("Hjl-f9JB5Fc", "0:43", "Funcionalidade", "Ficou na dúvida se apagou a luz? Confira de qualquer lugar"),
  "superfluo": ("SwePXzcqUHw", "1:46", "Conceito", "Automação é supérflua? Veja o que ela resolve no dia a dia"),
  "sofisticacao": ("YRsiL94C8M0", "0:55", "Instalação", "Sofisticação e praticidade entregues ao cliente"),
  "bertioga": ("zmOcghsTil8", "", "Obra real", "Bertioga: a área externa inteira acende com um toque"),
  "piscina": ("HqBkfnPbAh8", "", "Obra real", "Piscina e iluminação controladas pelo celular"),
  "cena": ("Dxcms6iU3Aw", "", "Obra real", "Cenas de iluminação: a sala muda de clima com um toque"),
  "tablet": ("g9L_j4eQCQg", "", "Obra real", "A casa inteira em um tablet: luz, clima e persianas"),
  "decorado": ("Hc9IXVOUy9A", "", "Decorado", "Apartamento decorado com automação completa"),
  "persianas": ("TlABweeASNI", "", "Obra real", "Persianas motorizadas integradas às cenas"),
}

def video(key):
    vid, dur, tag, title = VIDEOS[key]
    return f'''<a class="video" href="https://www.youtube.com/watch?v={vid}" target="_blank" rel="noopener">
  <div class="thumb" style="background-image:url('https://i.ytimg.com/vi/{vid}/hqdefault.jpg')"><span class="play">{PLAY}</span>{f'<span class="dur">{dur}</span>' if dur else ''}</div>
  <div class="meta"><span>{tag}</span><strong>{title}</strong></div>
</a>'''

def foto(nome, alt, legenda, cls=""):
    return f'<figure class="shot {cls}"><img src="assets/img/{nome}.webp" alt="{alt}" loading="lazy" decoding="async"><figcaption>{legenda}</figcaption></figure>'

def card(icon, title, text, tag=None):
    t = f'<span class="tag">{tag}</span>' if tag else ""
    return f'<div class="card"><span class="ico">{ICON[icon]}</span>{t}<h3>{title}</h3><p>{text}</p></div>'

def assistant(flow, title="Assistente M7"):
    return f'''<div class="assistant" data-flow="{flow}" aria-label="Assistente virtual da M7">
  <div class="as-head"><span class="as-avatar"><span>M7</span></span><div><strong>{title}</strong><small>online agora</small></div><span class="badge">Agente de IA</span></div>
  <div class="as-body" aria-live="polite"></div>
  <div class="as-opts"></div>
  <form class="as-input" autocomplete="off"><input id="as-{flow}" type="text" placeholder="Escolha uma opção acima" disabled aria-label="Sua resposta"><button type="submit" disabled aria-label="Enviar">{SEND}</button></form>
</div>'''

def faq(items):
    return '<div class="faq">' + "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in items) + "</div>"

def lead_form(assunto, fields_extra, button, note="Seus dados ficam só com a M7. Respondemos em horário comercial."):
    return f'''<form class="lead-form" data-assunto="{assunto}" novalidate>
  <div class="two">
    <div class="field"><label for="f-nome">Nome</label><input id="f-nome" name="nome" required autocomplete="name" placeholder="Como podemos te chamar"></div>
    <div class="field"><label for="f-whats">WhatsApp</label><input id="f-whats" name="whatsapp" required inputmode="tel" autocomplete="tel" placeholder="(11) 90000-0000"></div>
  </div>
  {fields_extra}
  <button class="btn btn-red" type="submit">{button} {ARROW}</button>
  <p class="form-note">{note}</p>
  <div class="form-ok" hidden></div>
</form>'''

def page(slug, title, desc, body, casa=False, schema=None, home=False):
    nav = "".join(f'<a href="{h}"{' aria-current="page"' if h == slug else ''}>{n}</a>' for h, n in NAV)
    canon = SITE + "/" + ("" if slug == "index.html" else slug.replace(".html", ""))
    ld = {
      "@context": "https://schema.org", "@type": "LocalBusiness",
      "name": "M7 Automação", "url": SITE, "telephone": "+55 11 91301-9826",
      "description": "Automação de processos com inteligência artificial para empresas em todo o Brasil e automação residencial e predial em São Paulo e Grande São Paulo.",
      "areaServed": ["São Paulo", "Grande São Paulo", "Brasil"],
      "address": {"@type": "PostalAddress", "addressLocality": "São Paulo", "addressRegion": "SP", "addressCountry": "BR"},
      "sameAs": ["https://www.youtube.com/@M7Automação", "https://facebook.com/m7automacao", "https://linkedin.com/company/m7automacao"]
    }
    extra_ld = f'<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>' if schema else ""
    fonts = "family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@500&family=Space+Grotesk:wght@500;600" + ("&family=Manrope:wght@300;600" if casa else "") + "&family=Syne:wght@600;700;800"
    return f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canon}">
<meta property="og:locale" content="pt_BR">
<meta name="theme-color" content="#07090d">
<link rel="icon" href="assets/logo.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{fonts}&display=swap">
<link rel="stylesheet" href="assets/style.css">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
{extra_ld}
<link rel="stylesheet" href="assets/home.css">
</head>
<body class="home{' casa' if casa else ''}{' index' if home else ' lp-page'}">
<header class="top">
  <div class="wrap">
    <a class="brand" href="index.html">{LOGO}<span>M7 AUTOMAÇÃO<small>IA · Residencial · Predial</small></span></a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav">Menu</button>
    <nav class="nav" id="nav">{nav}<a class="btn btn-red btn-sm" data-wa="Olá! Vim pelo site da M7 Automação e quero falar com um especialista.">Falar com especialista</a></nav>
  </div>
</header>
<main>
{body}
</main>
<footer>
  <div class="wrap">
    <div class="foot">
      <div class="stack" style="gap:12px">
        <a class="brand" href="index.html">{LOGO}<span>M7 AUTOMAÇÃO</span></a>
        <p>Automação de processos com IA para empresas de todo o Brasil. Automação residencial e predial em São Paulo e Grande SP.</p>
        <p class="mono small">WhatsApp: (11) 96860-2016</p>
      </div>
      <div><h4>Soluções</h4><ul><li><a href="ia-para-empresas.html">IA para empresas</a></li><li><a href="automacao-residencial.html">Automação residencial</a></li><li><a href="condominios.html">Condomínios e prédios</a></li><li><a href="arquitetos.html">Para arquitetos</a></li></ul></div>
      <div><h4>Conteúdo</h4><ul><li><a href="https://www.youtube.com/@M7Automa%C3%A7%C3%A3o" target="_blank" rel="noopener">YouTube</a></li><li><a href="https://linkedin.com/company/m7automacao" target="_blank" rel="noopener">LinkedIn</a></li><li><a href="https://facebook.com/m7automacao" target="_blank" rel="noopener">Facebook</a></li></ul></div>
      <div><h4>Atendimento</h4><ul><li>IA: todo o Brasil, online</li><li>Residencial e predial: São Paulo e Grande SP</li><li><a data-wa="Olá! Vim pelo site da M7 Automação.">Chamar no WhatsApp</a></li></ul></div>
    </div>
    <div class="legal"><span>© 2026 M7 Automação. Todos os direitos reservados.</span><span>Projetos independentes de marca.</span></div>
  </div>
</footer>
<a class="wa-float" aria-label="Falar no WhatsApp" data-wa="Olá! Vim pelo site da M7 Automação."><span class="wa-icon"></span></a>
<script src="assets/app.js"></script><script src="assets/home.js"></script>
</body>
</html>
'''

# ---------------- HOME ----------------
home = f'''
<section class="x-hero">
  <div class="x-grid" aria-hidden="true"></div>
  <canvas id="swarm" aria-hidden="true"></canvas>
  <div class="wrap">
    <div class="x-copy">
      <span class="x-kicker"><i></i>Automação com inteligência artificial</span>
      <h1 class="x-title">Inteligência que <em>trabalha</em> por você.</h1>
      <div class="x-rot" aria-live="polite"><b id="rot-word">Na sua empresa.</b><span class="dots" aria-hidden="true"><span class="on"></span><span></span><span></span><span></span></span></div>
      <p class="x-sub">Agentes de IA que atendem, vendem e organizam a sua empresa. Casas e prédios que respondem a quem vive neles. Projetos sob medida da M7, de São Paulo para o Brasil.</p>
      <div class="x-cta"><a class="btn btn-glow" href="ia-para-empresas.html">Automatizar minha empresa {ARROW}</a><a class="btn btn-glass" href="automacao-residencial.html">Automatizar minha casa</a></div>
    </div>
  </div>
  <div class="x-hint" aria-hidden="true">Passe o mouse<br>sobre as partículas</div>
</section>

<div class="x-marquee" aria-hidden="true"><div class="x-track">
  <span>Agentes de IA no WhatsApp</span><span>Orçamentos em segundos</span><span>Agenda que se confirma sozinha</span><span>CRM sempre atualizado</span><span>Cenas de iluminação</span><span>Som em cada ambiente</span><span>Clima no ponto certo</span><span>Segurança pelo celular</span><span>Wi-Fi na casa toda</span>
  <span>Agentes de IA no WhatsApp</span><span>Orçamentos em segundos</span><span>Agenda que se confirma sozinha</span><span>CRM sempre atualizado</span><span>Cenas de iluminação</span><span>Som em cada ambiente</span><span>Clima no ponto certo</span><span>Segurança pelo celular</span><span>Wi-Fi na casa toda</span>
</div></div>

<section class="x-sec">
  <div class="wrap">
    <div class="x-head reveal"><span class="x-label">O cérebro M7</span><h2 class="x-h2">Tudo que entra, a IA <em>entende</em>. Tudo que precisa acontecer, ela <em>faz</em>.</h2><p class="lead">Mensagens, formulários, e-mails e sensores chegam a um só cérebro, que decide e executa. Na empresa vira venda e organização. Em casa vira conforto e segurança.</p></div>
    <div class="brain reveal">
      <div class="brain-stage">
        <svg id="brain" viewBox="0 0 1000 480" role="img" aria-label="Diagrama: entradas (WhatsApp, site, e-mail, sensores) passam pela IA da M7 e viram ações (CRM, agenda, orçamento, iluminação, clima, segurança)">
          <g id="wires"></g>
          <circle class="core-ring" cx="500" cy="230" r="86"/>
          <circle class="core-ring b" cx="500" cy="230" r="104"/>
          <circle cx="500" cy="230" r="62" fill="#0b0f17" stroke="rgba(238,69,83,.6)" stroke-width="1.4"/>
          <text class="core-txt" x="500" y="236" text-anchor="middle">M7</text>
          <text class="core-sub" x="500" y="258" text-anchor="middle">IA</text>
          <g id="pulses"></g>
          <g id="nodes"></g>
        </svg>
      </div>
      <div class="feed"><div class="feed-head"><span>Acontecendo agora</span><b>simulação</b></div><ol id="feed"></ol><p class="feed-note">Exemplos do que os agentes e automações da M7 fazem no dia a dia dos clientes.</p></div>
    </div>
  </div>
</section>

<section class="x-sec" style="padding-top:0">
  <div class="wrap">
    <div class="x-head reveal"><span class="x-label">Escolha o seu mundo</span><h2 class="x-h2">Duas frentes. O mesmo cuidado de projeto.</h2></div>
    <div class="worlds">
      <a class="world biz reveal" href="ia-para-empresas.html">
        <span class="x-label">Para empresas · todo o Brasil</span>
        <h3>Sua operação no piloto automático.</h3>
        <p>Atendimento 24 horas no WhatsApp, agenda que se confirma sozinha, orçamentos na hora e fim do retrabalho em planilhas.</p>
        <ul><li>Agentes de atendimento</li><li>Fluxos entre sistemas</li><li>Backoffice</li><li>Indicadores</li></ul>
        <span class="go">Ver como funciona {ARROW}</span>
        <svg class="art" viewBox="0 0 200 200" aria-hidden="true"><defs><linearGradient id="gb" x1="0" x2="1"><stop offset="0" stop-color="#9eb4d5" stop-opacity=".9"/><stop offset="1" stop-color="#ee4553" stop-opacity=".9"/></linearGradient></defs><g fill="none" stroke="url(#gb)" stroke-width="1"><circle cx="100" cy="100" r="30"/><circle cx="100" cy="100" r="55" stroke-dasharray="2 5"/><circle cx="100" cy="100" r="80" stroke-opacity=".5"/><path d="M100 20v30M100 150v30M20 100h30M150 100h30M43 43l21 21M136 136l21 21M157 43l-21 21M64 136l-21 21"/></g><g fill="#d6e3f5"><circle cx="100" cy="20" r="3"/><circle cx="180" cy="100" r="3"/><circle cx="100" cy="180" r="3"/><circle cx="20" cy="100" r="3"/><circle cx="157" cy="43" r="3"/><circle cx="43" cy="157" r="3"/></g><circle cx="100" cy="100" r="9" fill="#ee4553"/></svg>
      </a>
      <a class="world casa reveal" href="automacao-residencial.html">
        <span class="x-label">Para casas e prédios · SP e Grande SP</span>
        <h3>A casa que se ajusta a você.</h3>
        <p>Luz, som, clima, persianas, segurança e Wi-Fi integrados em um só toque. Projetos independentes de marca.</p>
        <ul><li>Iluminação e cenas</li><li>Áudio e vídeo</li><li>Climatização</li><li>Segurança</li></ul>
        <span class="go">Ver projetos {ARROW}</span>
        <svg class="art" viewBox="0 0 200 200" aria-hidden="true"><defs><linearGradient id="gc" x1="0" x2="1" y1="0" y2="1"><stop offset="0" stop-color="#f3dfb4"/><stop offset="1" stop-color="#b8894a"/></linearGradient><radialGradient id="glow"><stop offset="0" stop-color="#f3dfb4" stop-opacity=".55"/><stop offset="1" stop-color="#f3dfb4" stop-opacity="0"/></radialGradient></defs><circle cx="118" cy="92" r="70" fill="url(#glow)"/><path d="M30 104 100 44l70 60v76H30Z" fill="none" stroke="url(#gc)" stroke-width="1.4"/><path d="M80 180v-44h40v44" fill="none" stroke="url(#gc)" stroke-width="1.4"/><rect x="48" y="112" width="22" height="18" rx="2" fill="#f3dfb4" fill-opacity=".85"/><rect x="130" y="112" width="22" height="18" rx="2" fill="#f3dfb4" fill-opacity=".35"/><circle cx="100" cy="88" r="7" fill="none" stroke="#f3dfb4" stroke-width="1.4"/></svg>
      </a>
    </div>
    <div class="mini">
      <a href="condominios.html"><div><b>Condomínios e prédios</b><span>Acesso, câmeras, economia e IA para moradores</span></div>{ARROW}</a>
      <a href="arquitetos.html"><div><b>Para arquitetos</b><span>Parceria técnica desde a planta</span></div>{ARROW}</a>
    </div>
  </div>
</section>

<section class="x-sec" style="padding-top:0">
  <div class="wrap">
    <div class="x-head reveal"><span class="x-label">Como a M7 pensa</span><h2 class="x-h2">Tecnologia escolhida para o <em>seu</em> caso.</h2></div>
    <div class="tenets">
      <div class="tenet reveal"><b>Sob medida<i>.</i></b><p>Nada de pacote pronto. Primeiro entendemos a rotina da sua casa ou o gargalo da sua empresa.</p></div>
      <div class="tenet reveal"><b>Sem marca presa<i>.</i></b><p>Usamos os melhores equipamentos e modelos de IA do mercado (OpenAI, Anthropic, Google) conforme cada projeto.</p></div>
      <div class="tenet reveal"><b>Resultado medido<i>.</i></b><p>Automação que se paga em tempo economizado, menos erros e mais vendas, com números que você acompanha.</p></div>
    </div>
  </div>
</section>

<section class="x-sec" style="padding-top:0">
  <div class="wrap try">
    <div class="stack reveal" style="gap:22px">
      <span class="x-label">Experimente agora</span>
      <h2 class="x-h2">Converse com um agente de IA da M7.</h2>
      <p class="lead">Este assistente faz o que um agente faz na sua empresa: entende o que você precisa, qualifica e entrega o pedido pronto para a equipe, em menos de um minuto.</p>
      <ul class="checks"><li>Atende 24 horas, inclusive fim de semana</li><li>Fala com o tom da sua marca</li><li>Passa para uma pessoa quando precisa</li></ul>
    </div>
    <div class="phone reveal">{assistant("geral")}</div>
  </div>
</section>

<section class="x-sec" style="padding-top:0">
  <div class="wrap">
    <div class="x-head reveal"><span class="x-label">Quem já tem M7</span><h2 class="x-h2">Veja e ouça nossos clientes.</h2></div>
    <div class="grid g3">{video("cliente")}{video("leandro")}{video("bertioga")}</div>
  </div>
</section>

<section class="x-sec" style="padding-top:0">
  <div class="wrap">
    <div class="x-cta-band reveal">
      <span class="x-label">Raio-X de Automação M7 · gratuito</span>
      <h2 class="x-h2">Descubra o que dá para <em>automatizar</em> no seu negócio.</h2>
      <p>Uma conversa de 30 minutos, online. Você sai com um mapa do que pode virar automático e quanto tempo isso libera para a sua equipe.</p>
      <div class="x-cta"><a class="btn btn-glow" href="ia-para-empresas.html#raio-x">Quero meu Raio-X {ARROW}</a><a class="btn btn-wa" data-wa="Olá! Quero agendar o Raio-X de Automação da M7."><span class="wa-icon"></span> WhatsApp</a></div>
    </div>
  </div>
</section>
'''

# ---------------- IA PARA EMPRESAS ----------------
ia_faq = [
 ("Preciso entender de tecnologia para usar?", "Não. A M7 desenha, implanta e treina sua equipe. No dia a dia, sua empresa só acompanha os resultados e os atendimentos que chegam prontos."),
 ("A IA vai responder coisas erradas para o meu cliente?", "O agente é treinado com as informações da sua empresa (serviços, preços, regras e tom de voz) e tem limites claros. Quando a conversa sai do que ele sabe, passa para uma pessoa da equipe."),
 ("Funciona com o WhatsApp que eu já uso?", "Sim. Integramos ao WhatsApp Business da empresa e às ferramentas que você já tem, como agenda, CRM, planilhas e ERP."),
 ("Vocês atendem empresas fora de São Paulo?", "Sim. Projetos de IA são feitos 100% online para empresas de todo o Brasil."),
 ("Quanto custa?", "Depende do processo automatizado e do volume. No Raio-X gratuito mostramos o escopo e o investimento antes de qualquer compromisso."),
 ("Em quanto tempo fica pronto?", "Um primeiro agente de atendimento costuma entrar no ar em poucas semanas. Fluxos maiores são entregues em etapas, para você já ganhar tempo desde o começo."),
]
ia_schema = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in ia_faq]}
ia = f'''
<section class="hero x-hero lp" data-shapes="chat,m7">
  <div class="x-grid" aria-hidden="true"></div>
  <canvas id="swarm" aria-hidden="true"></canvas>
  <div class="wrap hero-grid">
    <div class="stack" style="gap:24px">
      <span class="eyebrow">Automação de processos com IA · todo o Brasil</span>
      <h1>Chega de responder <strong>a mesma coisa</strong> o dia todo. A IA faz.</h1>
      <p class="lead">Agentes de IA que atendem no WhatsApp 24 horas, qualificam clientes, marcam horários, montam orçamentos e alimentam seus sistemas. Para micro e pequenas empresas que querem crescer sem aumentar a equipe.</p>
      <div class="row"><a class="btn btn-red" href="#raio-x">Quero meu Raio-X gratuito {ARROW}</a><a class="btn btn-ghost" href="#como">Como funciona</a></div>
      <p class="small muted">Teste ao lado: este assistente é um agente como os que implantamos.</p>
    </div>
    {assistant("ia", "Agente de Raio-X")}
  </div>
</section>

<section class="band alt">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">O dia a dia que a IA resolve</span><h2>O que muda na sua operação.</h2></div>
    <div class="compare">
      <div class="before"><h3>Hoje</h3><ul><li>Cliente manda mensagem à noite e só tem resposta no dia seguinte</li><li>Alguém da equipe passa horas respondendo as mesmas perguntas</li><li>Agenda confirmada no braço, com faltas sem aviso</li><li>Orçamento demora dias e o cliente fecha com outro</li><li>Dados digitados duas ou três vezes em sistemas diferentes</li></ul></div>
      <div class="after"><h3>Com a M7</h3><ul><li>Resposta em segundos, 24 horas por dia, com o tom da sua marca</li><li>Perguntas repetidas resolvidas pela IA, equipe livre para vender</li><li>Confirmação e lembrete automáticos, com remarcação pelo próprio cliente</li><li>Orçamento gerado a partir da conversa e enviado na hora</li><li>Informação que entra uma vez e flui para CRM, planilha e financeiro</li></ul></div>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">Soluções</span><h2>O que automatizamos.</h2></div>
    <div class="grid g3">
      {card("chat", "Agente de atendimento no WhatsApp", "Responde, tira dúvidas, qualifica e passa para a equipe só o que precisa de gente. Funciona no número que você já usa.")}
      {card("cal", "Agenda e confirmações", "Marca, confirma, lembra e remarca horários sozinho. Ideal para clínicas, consultórios, escolas e prestadores de serviço.")}
      {card("doc", "Orçamentos e propostas", "Gera orçamento a partir das informações da conversa, com seus preços e regras, pronto para enviar.")}
      {card("crm", "CRM e follow-up", "Todo contato registrado e acompanhado. A IA lembra de quem não respondeu e retoma a conversa no momento certo.")}
      {card("flow", "Fluxos entre sistemas", "Conectamos WhatsApp, e-mail, planilhas, ERP e CRM para os dados fluírem sem digitação manual.")}
      {card("chart", "Relatórios e indicadores", "Painéis simples com atendimentos, vendas e gargalos, atualizados automaticamente.")}
    </div>
  </div>
</section>

<section class="band alt" id="como">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">Como funciona</span><h2>Do diagnóstico ao agente no ar.</h2></div>
    <div class="steps">
      <div class="step"><h3>Raio-X gratuito</h3><p>Conversa online de 30 minutos para mapear onde sua equipe perde tempo e dinheiro.</p></div>
      <div class="step"><h3>Projeto e proposta</h3><p>Desenhamos a automação, mostramos o fluxo e o investimento antes de começar.</p></div>
      <div class="step"><h3>Implantação</h3><p>Treinamos a IA com as regras da sua empresa e integramos às suas ferramentas.</p></div>
      <div class="step"><h3>Acompanhamento</h3><p>Medimos resultados, ajustamos respostas e expandimos para novos processos.</p></div>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">Por segmento</span><h2>Exemplos do que dá para automatizar.</h2></div>
    <div class="grid g4">
      {card("cal", "Clínicas e consultórios", "Agendamento, confirmação, triagem inicial e envio de orientações pré-consulta.", "Saúde")}
      {card("doc", "Escolas", "Matrículas, atendimento a pais, avisos e cobrança organizados sem sobrecarregar a secretaria.", "Educação")}
      {card("chat", "Comércio e serviços", "Atendimento, catálogo, orçamento e pós-venda no WhatsApp, inclusive fora do horário.", "Varejo")}
      {card("flow", "Indústria e distribuição", "Pedidos, estoque e suporte a clientes com dados integrados ao ERP.", "Operação")}
    </div>
  </div>
</section>

<section class="band alt" id="raio-x">
  <div class="wrap form-wrap">
    <div class="stack" style="gap:20px">
      <span class="eyebrow">Raio-X de Automação M7</span>
      <h2>Receba um mapa do que dá para automatizar na sua empresa.</h2>
      <p class="lead">Sem custo e sem compromisso. Em 30 minutos online você descobre:</p>
      <ul class="checks"><li>Quais tarefas da sua equipe podem virar automáticas</li><li>Quanto tempo por semana isso libera</li><li>Por onde começar para ter resultado rápido</li><li>O investimento estimado de cada etapa</li></ul>
    </div>
    {lead_form("Raio-X de Automação (IA para empresas)", '''<div class="two"><div class="field"><label for="f-empresa">Empresa</label><input id="f-empresa" name="empresa" autocomplete="organization" placeholder="Nome da empresa"></div><div class="field"><label for="f-equipe">Tamanho da equipe</label><select id="f-equipe" name="equipe"><option value="">Selecione</option><option>Só eu</option><option>2 a 10 pessoas</option><option>11 a 50 pessoas</option><option>Mais de 50</option></select></div></div>
  <div class="field"><label for="f-gargalo">O que mais toma tempo hoje?</label><textarea id="f-gargalo" name="gargalo" placeholder="Ex.: respondemos as mesmas perguntas no WhatsApp o dia todo"></textarea></div>''', "Quero meu Raio-X")}
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">Perguntas frequentes</span><h2>Antes de você perguntar.</h2></div>
    {faq(ia_faq)}
  </div>
</section>
'''

# ---------------- RESIDENCIAL ----------------
res_faq = [
 ("Preciso quebrar paredes para automatizar?", "Na maioria dos casos, não. Existem soluções sem fio para imóveis prontos. Em obra ou reforma, planejamos a infraestrutura para o resultado ficar mais robusto e invisível."),
 ("Fico preso a uma marca?", "Não. A M7 é independente de marca: escolhemos os equipamentos que fazem mais sentido para o seu projeto e orçamento."),
 ("Dá para controlar tudo pelo celular e por voz?", "Sim. Iluminação, som, ar-condicionado, persianas, câmeras e portões em um só aplicativo, com assistentes de voz como Alexa e Google."),
 ("Vocês atendem onde?", "Projetos residenciais e prediais em São Paulo capital e Grande São Paulo."),
 ("E depois da instalação?", "Entregamos tudo configurado, ensinamos a família a usar e seguimos disponíveis para ajustes e novas cenas."),
]
res = f'''
<section class="hero x-hero lp" data-shapes="house,m7">
  <div class="x-grid" aria-hidden="true"></div>
  <canvas id="swarm" aria-hidden="true"></canvas>
  <div class="wrap hero-grid">
    <div class="stack" style="gap:24px">
      <span class="eyebrow">Automação residencial · São Paulo e Grande SP</span>
      <h1>A casa que <strong>se ajusta a você</strong>, e não o contrário.</h1>
      <p class="lead">Luz, som, clima, persianas, segurança e Wi-Fi integrados em um só toque. Projetos sob medida, independentes de marca, do planejamento à entrega.</p>
      <div class="row"><a class="btn btn-red" href="#orcamento">Quero um projeto para minha casa {ARROW}</a><a class="btn btn-ghost" href="#videos">Ver clientes</a></div>
    </div>
    <div class="scene" aria-label="Exemplo de painel de casa inteligente">
      <div class="scene-top"><div><span>Cena ativa</span><br><b id="scene-name">Chegando em casa</b></div><span>Sala · 23 °C</span></div>
      <div class="row" style="gap:8px">
        <button class="btn btn-ghost btn-sm" type="button" data-scene="chegar" data-label="Chegando em casa">Chegar</button>
        <button class="btn btn-ghost btn-sm" type="button" data-scene="cinema" data-label="Cinema">Cinema</button>
        <button class="btn btn-ghost btn-sm" type="button" data-scene="dormir" data-label="Boa noite">Dormir</button>
      </div>
      <div class="tiles">
        <button class="tile" type="button" aria-pressed="true" data-scenes="chegar" data-on="Ligadas · 70%" data-off="Desligadas"><span class="t-ico">{ICON["light"]}</span><strong>Iluminação</strong><small>Ligadas · 70%</small></button>
        <button class="tile" type="button" aria-pressed="true" data-scenes="chegar,cinema" data-on="Tocando" data-off="Pausado"><span class="t-ico">{ICON["sound"]}</span><strong>Som ambiente</strong><small>Tocando</small></button>
        <button class="tile" type="button" aria-pressed="true" data-scenes="chegar,cinema,dormir" data-on="23 °C" data-off="Desligado"><span class="t-ico">{ICON["temp"]}</span><strong>Climatização</strong><small>23 °C</small></button>
        <button class="tile" type="button" aria-pressed="false" data-scenes="cinema,dormir" data-on="Fechadas" data-off="Abertas"><span class="t-ico">{ICON["blind"]}</span><strong>Persianas</strong><small>Abertas</small></button>
        <button class="tile" type="button" aria-pressed="false" data-scenes="dormir" data-on="Ativado" data-off="Desativado"><span class="t-ico">{ICON["shield"]}</span><strong>Alarme</strong><small>Desativado</small></button>
        <button class="tile" type="button" aria-pressed="true" data-scenes="chegar,cinema,dormir" data-on="Casa toda" data-off="Pausado"><span class="t-ico">{ICON["wifi"]}</span><strong>Wi-Fi mesh</strong><small>Casa toda</small></button>
      </div>
      <div class="scene-cta"><span>Toque nas cenas e nos ambientes para testar.</span></div>
    </div>
  </div>
</section>

<section class="band alt">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">O que integramos</span><h2>Tudo conversando entre si, <strong>em um só controle.</strong></h2></div>
    <div class="grid g3">
      {card("light", "Iluminação e cenas", "Cenas para cada momento: chegar, receber, cinema, dormir. Dimerização e horários automáticos.")}
      {card("sound", "Áudio e vídeo", "Som ambiente por cômodo, home theater e salas de TV com controle único e acústica pensada.")}
      {card("temp", "Climatização", "Ar-condicionado ligando antes de você chegar e desligando quando o ambiente fica vazio.")}
      {card("blind", "Persianas e cortinas", "Motorizadas, por horário, por luz do sol ou integradas às cenas da casa.")}
      {card("cam", "Segurança e câmeras", "Câmeras, sensores, fechaduras e portões acompanhados pelo celular, de qualquer lugar.")}
      {card("wifi", "Rede de alta performance", "Wi-Fi que cobre a casa toda, com cabeamento e rack organizados. A base de tudo que é inteligente.")}
    </div>
  </div>
</section>

<section class="band" id="obras">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">Obras reais da M7</span><h2>Nada de banco de imagem. <strong>Isto é o que entregamos.</strong></h2></div>
    <div class="gallery g2">
      {foto("sala-cena-noturna", "Sala e varanda com cena de iluminação noturna automatizada", "Cena noturna: sala e varanda com luz indireta, acionada por um toque.", "wide")}
      {foto("interruptor-touch-cenas", "Teclado touch preto com teclas de cena", "Teclado touch com cenas personalizadas.")}
      {foto("fechadura-digital", "Fechadura digital instalada em porta branca", "Fechadura digital: biometria, senha e app.")}
    </div>
  </div>
</section>

<section class="band alt" id="short">
  <div class="wrap split short-split">
    <div class="stack reveal" style="gap:18px">
      <span class="eyebrow">Veja funcionando · 17 segundos</span>
      <h2>Saiu com pressa? <strong>Um comando e a casa apaga.</strong></h2>
      <p class="lead">Luzes, TV e o que mais ficou ligado desligam juntos, com um toque ou pela voz. É o tipo de detalhe que muda o dia a dia.</p>
      <ul class="checks"><li>Cena "Saindo de casa" em um toque</li><li>Funciona pelo celular, teclado ou assistente de voz</li><li>Confere de qualquer lugar se ficou algo ligado</li></ul>
      <div class="row"><a class="btn btn-wa" data-wa="Olá! Vi o vídeo da cena Saindo de casa no site e quero algo assim."><span class="wa-icon"></span> Quero isso em casa</a></div>
    </div>
    <div class="short reveal"><iframe src="https://www.youtube-nocookie.com/embed/Sodq3krnwiw?rel=0&modestbranding=1" title="Um comando e todas as luzes se apagam" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>
  </div>
</section>

<section class="band" id="videos">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">Clientes M7</span><h2>Quem mora com M7 conta como é.</h2></div>
    <div class="grid g3">{video("leandro")}{video("cliente")}{video("pet")}</div>
    <div class="grid g3 mt-m">{video("luz")}{video("sofisticacao")}{video("superfluo")}</div>
  </div>
</section>

<section class="band alt" id="obras-video">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">Obras em vídeo</span><h2>Veja funcionando, <strong>não só na foto.</strong></h2></div>
    <div class="grid g3">{video("bertioga")}{video("cena")}{video("tablet")}</div>
    <div class="grid g3 mt-m">{video("piscina")}{video("persianas")}{video("decorado")}</div>
  </div>
</section>

<section class="band alt">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">Como trabalhamos</span><h2>Do primeiro café à casa funcionando.</h2></div>
    <div class="steps">
      <div class="step"><h3>Visita e briefing</h3><p>Entendemos a rotina da família, o imóvel e o que você quer sentir em cada ambiente.</p></div>
      <div class="step"><h3>Projeto sob medida</h3><p>Escolhemos tecnologia e marcas certas para o seu caso, com proposta detalhada.</p></div>
      <div class="step"><h3>Instalação limpa</h3><p>Equipe própria, infraestrutura organizada e alinhada com arquiteto e obra.</p></div>
      <div class="step"><h3>Entrega e suporte</h3><p>Tudo configurado, família treinada e suporte para novas cenas e ajustes.</p></div>
    </div>
  </div>
</section>

<section class="band" id="orcamento">
  <div class="wrap form-wrap">
    <div class="stack" style="gap:20px">
      <span class="eyebrow">Projeto residencial</span>
      <h2>Vamos desenhar a <strong>sua</strong> casa inteligente.</h2>
      <p class="lead">Atendemos São Paulo capital e Grande SP. Conte um pouco sobre o imóvel e um especialista retorna com os próximos passos.</p>
      <ul class="checks"><li>Imóveis prontos, em obra ou na planta</li><li>Projetos para casas e apartamentos</li><li>Trabalhamos junto com seu arquiteto</li></ul>
    </div>
    {lead_form("Projeto de automação residencial", '''<div class="two"><div class="field"><label for="f-bairro">Bairro / cidade</label><input id="f-bairro" name="local" placeholder="Ex.: Moema, Alphaville"></div><div class="field"><label for="f-fase">Fase do imóvel</label><select id="f-fase" name="fase"><option value="">Selecione</option><option>Na planta</option><option>Em obra ou reforma</option><option>Pronto, já moro</option></select></div></div>
  <div class="field"><label for="f-interesse">O que você quer automatizar?</label><textarea id="f-interesse" name="interesse" placeholder="Ex.: iluminação da sala, home theater e câmeras"></textarea></div>''', "Quero meu projeto")}
  </div>
</section>

<section class="band alt">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">Perguntas frequentes</span><h2>Dúvidas comuns sobre automação residencial.</h2></div>
    {faq(res_faq)}
  </div>
</section>
'''

# ---------------- CONDOMÍNIOS ----------------
con_faq = [
 ("Dá para fazer em um condomínio antigo?", "Sim. Avaliamos a infraestrutura existente e propomos soluções que aproveitam o que já funciona, com etapas que cabem no orçamento do condomínio."),
 ("A automação reduz custos?", "Iluminação por sensores e horários, controle de equipamentos e monitoramento remoto reduzem desperdícios. No diagnóstico estimamos onde está a economia."),
 ("Como funciona o atendimento a moradores com IA?", "Um agente no WhatsApp do condomínio responde dúvidas frequentes, registra solicitações, reservas de áreas comuns e encaminha o que precisa ao síndico ou à administradora."),
 ("Vocês apresentam o projeto em assembleia?", "Sim. Preparamos uma proposta clara, com etapas e investimento, para facilitar a aprovação."),
]
con = f'''
<section class="hero x-hero lp" data-shapes="building,m7">
  <div class="x-grid" aria-hidden="true"></div>
  <canvas id="swarm" aria-hidden="true"></canvas>
  <div class="wrap hero-grid">
    <div class="stack" style="gap:24px">
      <span class="eyebrow">Condomínios e prédios · São Paulo e Grande SP</span>
      <h1>Condomínio mais <strong>seguro, econômico</strong> e fácil de administrar.</h1>
      <p class="lead">Controle de acesso, câmeras integradas, iluminação inteligente nas áreas comuns e um agente de IA que atende moradores no WhatsApp. Projetos para síndicos, conselhos e administradoras.</p>
      <div class="row"><a class="btn btn-red" href="#diagnostico">Agendar diagnóstico do condomínio {ARROW}</a></div>
    </div>
    {assistant("condominio", "Assistente do Condomínio")}
  </div>
</section>

<section class="band alt">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">Soluções prediais</span><h2>O que o seu condomínio ganha.</h2></div>
    <div class="grid g3">
      {card("key", "Controle de acesso", "Entrada de moradores, visitantes e prestadores com registro, por app, tag ou reconhecimento.")}
      {card("cam", "Câmeras e monitoramento", "CFTV integrado e acompanhado à distância, com acesso controlado para portaria e síndico.")}
      {card("leaf", "Economia nas áreas comuns", "Iluminação por sensor e horário, bombas e equipamentos monitorados para cortar desperdício.")}
      {card("chat", "Atendimento a moradores com IA", "Dúvidas, reservas e solicitações resolvidas no WhatsApp, 24 horas, sem sobrecarregar o síndico.")}
      {card("wifi", "Rede e Wi-Fi nas áreas comuns", "Conectividade estável no salão, academia e portaria, base para todos os sistemas.")}
      {card("chart", "Relatórios para o síndico", "Ocorrências, acessos e consumo organizados para prestar contas com transparência.")}
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">Como funciona</span><h2>Um caminho claro até a aprovação.</h2></div>
    <div class="steps">
      <div class="step"><h3>Diagnóstico</h3><p>Visita técnica para avaliar acesso, câmeras, rede e consumo.</p></div>
      <div class="step"><h3>Proposta em etapas</h3><p>Prioridades e investimento organizados para caber no caixa do condomínio.</p></div>
      <div class="step"><h3>Apresentação</h3><p>Material pronto para conselho e assembleia.</p></div>
      <div class="step"><h3>Implantação e suporte</h3><p>Instalação com mínimo impacto na rotina e acompanhamento contínuo.</p></div>
    </div>
  </div>
</section>

<section class="band" id="videos">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">Obras em vídeo</span><h2>Áreas comuns e decorados <strong>que vendem sozinhos.</strong></h2></div>
    <div class="grid g3">{video("decorado")}{video("bertioga")}{video("piscina")}</div>
  </div>
</section>

<section class="band alt" id="diagnostico">
  <div class="wrap form-wrap">
    <div class="stack" style="gap:20px">
      <span class="eyebrow">Diagnóstico do condomínio</span>
      <h2>Vamos avaliar o seu prédio.</h2>
      <p class="lead">Para síndicos, conselheiros e administradoras em São Paulo e Grande SP.</p>
      <ul class="checks"><li>Levantamento de segurança e acesso</li><li>Oportunidades de economia de energia</li><li>Proposta em etapas para assembleia</li></ul>
    </div>
    {lead_form("Diagnóstico de condomínio", '''<div class="two"><div class="field"><label for="f-cond">Condomínio e bairro</label><input id="f-cond" name="condominio" placeholder="Nome e bairro"></div><div class="field"><label for="f-unid">Número de unidades</label><select id="f-unid" name="unidades"><option value="">Selecione</option><option>Até 30</option><option>31 a 100</option><option>Mais de 100</option></select></div></div>
  <div class="field"><label for="f-papel">Você é</label><select id="f-papel" name="perfil"><option value="">Selecione</option><option>Síndico(a)</option><option>Administradora</option><option>Conselho</option><option>Morador(a)</option></select></div>''', "Agendar diagnóstico")}
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">Perguntas frequentes</span><h2>Dúvidas de síndicos e administradoras.</h2></div>
    {faq(con_faq)}
  </div>
</section>
'''

# ---------------- ARQUITETOS ----------------
arq_faq = [
 ("Em que momento devo envolver a M7?", "O ideal é no estudo preliminar ou no início do executivo. Assim a infraestrutura de automação e rede entra no projeto sem retrabalho na obra."),
 ("A automação vai interferir no meu projeto?", "Não. Nosso papel é técnico: a estética é sua. Escolhemos teclados, sensores e equipamentos que conversam com o seu desenho."),
 ("Vocês acompanham a obra?", "Sim. Fazemos compatibilização, orientação ao eletricista e visitas técnicas até a entrega final ao cliente."),
 ("Como funciona a parceria?", "Atendemos seus clientes com o mesmo cuidado que você, e conversamos sobre um modelo de parceria contínua. As condições são apresentadas em uma conversa rápida."),
]
arq = f'''
<section class="hero x-hero lp" data-shapes="house,building">
  <div class="x-grid" aria-hidden="true"></div>
  <canvas id="swarm" aria-hidden="true"></canvas>
  <div class="wrap hero-grid">
    <div class="stack" style="gap:24px">
      <span class="eyebrow">Para arquitetos e designers de interiores</span>
      <h1>Seu projeto <strong>perfeito também por dentro</strong> das paredes.</h1>
      <p class="lead">A M7 cuida da automação, áudio e vídeo e rede dos seus projetos desde a planta. Você entrega um imóvel inteligente, sem conflito na obra e sem surpresa para o cliente.</p>
      <div class="row"><a class="btn btn-red" href="#parceria">Quero ser parceiro(a) M7 {ARROW}</a><a class="btn btn-wa" data-wa="Olá! Sou arquiteto(a) e quero conversar sobre parceria com a M7."><span class="wa-icon"></span> Conversar agora</a></div>
    </div>
    {assistant("arquiteto", "Assistente para Arquitetos")}
  </div>
</section>

<section class="band alt">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">O que entregamos ao escritório</span><h2>Tecnologia que <strong>respeita o seu desenho.</strong></h2></div>
    <div class="grid g3">
      {card("plan", "Projeto de infraestrutura", "Pontos, tubulação, quadro e rack definidos junto com o seu executivo.")}
      {card("hand", "Compatibilização", "Automação, elétrica, ar e marcenaria conversando antes da obra começar.")}
      {card("light", "Cenas de iluminação", "Seu projeto luminotécnico vira cenas reais, dimerizadas e fáceis de usar.")}
      {card("sound", "Áudio e vídeo integrados", "Caixas embutidas, telas e home theater que somem no ambiente.")}
      {card("rack", "Rede e rack organizados", "Wi-Fi para o imóvel todo e central técnica limpa e documentada.")}
      {card("shield", "Independência de marca", "Escolhemos o equipamento pelo projeto e pelo cliente, não por contrato com fabricante.")}
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap split">
    <div class="stack" style="gap:18px">
      <span class="eyebrow">Por que arquitetos indicam</span>
      <h2>Menos ruído na obra. <strong>Mais encanto na entrega.</strong></h2>
      <p class="lead">O cliente final percebe a casa funcionando. Você recebe o crédito por um projeto completo.</p>
    </div>
    <div>
      <div class="kpi"><b>Desde a planta</b><span>Infraestrutura prevista no executivo, sem quebra-quebra depois.</span></div>
      <div class="kpi"><b>Um só interlocutor</b><span>A M7 conversa com eletricista, marceneiro e fornecedores de ar e som.</span></div>
      <div class="kpi"><b>Entrega documentada</b><span>Plantas, rack identificado e treinamento para o cliente.</span></div>
    </div>
  </div>
</section>

<section class="band" id="obras">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">Bastidores de obra</span><h2>Infraestrutura <strong>organizada e documentada.</strong></h2></div>
    <div class="gallery g3p">
      {foto("forro-circuito-c22", "Ponto de forro com circuito identificado C22", "Cada circuito identificado no forro.")}
      {foto("modulo-identificado", "Módulo de automação etiquetado C25", "Módulos etiquetados, batendo com a planta.")}
      {foto("interruptor-touch-cenas", "Teclado touch com cenas", "Acabamento final que some no desenho.")}
    </div>
  </div>
</section>

<section class="band alt" id="videos">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">Projetos entregues</span><h2>O resultado que o seu cliente <strong>vai ver.</strong></h2></div>
    <div class="grid g3">{video("decorado")}{video("cena")}{video("persianas")}</div>
  </div>
</section>

<section class="band" id="parceria">
  <div class="wrap form-wrap">
    <div class="stack" style="gap:20px">
      <span class="eyebrow">Programa de parceria</span>
      <h2>Vamos conversar sobre o seu próximo projeto.</h2>
      <p class="lead">Atendemos escritórios com projetos em São Paulo e Grande SP. Condições de parceria apresentadas em uma conversa rápida.</p>
      <ul class="checks"><li>Apoio técnico em reuniões com o seu cliente</li><li>Orçamento rápido a partir da planta</li><li>Acompanhamento de obra até a entrega</li></ul>
    </div>
    {lead_form("Parceria para arquitetos", '''<div class="two"><div class="field"><label for="f-esc">Escritório</label><input id="f-esc" name="escritorio" placeholder="Nome do escritório"></div><div class="field"><label for="f-tipo">Tipo de projeto</label><select id="f-tipo" name="projeto"><option value="">Selecione</option><option>Residencial alto padrão</option><option>Apartamento</option><option>Comercial / corporativo</option><option>Vários</option></select></div></div>
  <div class="field"><label for="f-msg">Conte sobre o projeto (opcional)</label><textarea id="f-msg" name="mensagem" placeholder="Fase, local e o que o cliente deseja"></textarea></div>''', "Quero conversar")}
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">Perguntas frequentes</span><h2>O que arquitetos costumam perguntar.</h2></div>
    {faq(arq_faq)}
  </div>
</section>
'''

PAGES = [
  ("index.html", "M7 Automação | IA para empresas e casas inteligentes em SP", "Agentes de IA que atendem e vendem pela sua empresa e automação residencial e predial sob medida em São Paulo. Converse com nosso assistente.", home, False, None),
  ("ia-para-empresas.html", "Automação de Processos com IA para Pequenas Empresas | M7", "Agentes de IA no WhatsApp, agenda, orçamentos e integrações para micro e pequenas empresas de todo o Brasil. Faça o Raio-X de Automação gratuito.", ia, False, ia_schema),
  ("automacao-residencial.html", "Automação Residencial em São Paulo | M7 Automação", "Iluminação, som, climatização, segurança e Wi-Fi integrados. Projetos de automação residencial sob medida em São Paulo e Grande SP.", res, True, {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in res_faq]}),
  ("condominios.html", "Automação para Condomínios e Prédios em SP | M7 Automação", "Controle de acesso, câmeras, economia de energia e atendimento a moradores com IA para condomínios em São Paulo e Grande SP.", con, True, None),
  ("arquitetos.html", "Automação para Arquitetos e Projetos de Interiores | M7", "Parceria técnica em automação, áudio e vídeo e rede para escritórios de arquitetura em São Paulo. Infraestrutura pensada desde a planta.", arq, True, None),
]

for slug, title, desc, body, casa, schema in PAGES:
    (ROOT / slug).write_text(page(slug, title, desc, body, casa, schema, home=(slug == "index.html")), encoding="utf-8")

(ROOT / "assets" / "logo.svg").write_text(LOGO.replace('aria-hidden="true"', 'xmlns="http://www.w3.org/2000/svg"'), encoding="utf-8")
(ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")
urls = "".join(f"<url><loc>{SITE}/{'' if s == 'index.html' else s.replace('.html','')}</loc></url>" for s, *_ in PAGES)
(ROOT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n', encoding="utf-8")
(ROOT / "vercel.json").write_text(json.dumps({"cleanUrls": True, "trailingSlash": False, "redirects": [
  {"source": "/automacao-ia-processos", "destination": "/ia-para-empresas", "permanent": True},
  {"source": "/automacao-ia-processos/", "destination": "/ia-para-empresas", "permanent": True},
  {"source": "/automacao-residencial/", "destination": "/automacao-residencial", "permanent": True}
]}, indent=2), encoding="utf-8")
print("ok", [p[0] for p in PAGES])
