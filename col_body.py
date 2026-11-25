# Corpo da landing IA no Colégio (identidade própria: caderno quadriculado, tinta azul, marca-texto).
def col_body(ARROW, faq, lead_form, col_faq, PROD_CSS):
    TR = [
      ("exp", "3º ao 5º ano", "Exploradores de IA", "Aprender o que é IA brincando, com criatividade e segurança.", "#FF7A45",
       ["O que é IA (e o que ela não é)", "Histórias e desenhos criados com IA", "Caça aos erros da IA: a máquina também erra", "Segurança: o que nunca contar para a IA"],
       "Livro ilustrado da turma", "Cada aluno cria uma página com texto e ilustração. O livro é apresentado numa mostra para os pais."),
      ("cri", "6º ao 9º ano", "Criadores de IA", "Usar IA para estudar, criar e pensar criticamente.", "#6C4CF5",
       ["A arte do prompt: pedir bem para receber bem", "IA como tutor de estudos, não como cola", "Fake news, deepfakes e checagem de fontes", "Ética: autoria, cola e uso honesto"],
       "Chatbot ou campanha criativa", "A turma escolhe um tema do colégio e cria um chatbot ou uma campanha feita com IA."),
      ("fut", "Ensino médio", "IA para o Futuro", "IA aplicada ao vestibular, à carreira e ao empreendedorismo.", "#12B886",
       ["IA para estudar para o ENEM e os vestibulares", "Automação e criação de um assistente próprio", "Profissões do futuro e o mercado de trabalho", "Dados, LGPD e ética na prática"],
       "Protótipo no Demo Day", "Em grupos, os alunos constroem um protótipo e apresentam num Demo Day aberto aos pais."),
      ("pro", "Professores", "IA na Sala de Aula", "Professores como aliados, ganhando tempo no dia a dia.", "#E8436B",
       ["Planejamento de aulas com IA", "Provas, exercícios e rubricas em minutos", "Desafio real: como lidar com alunos que usam IA", "Kit de prompts pronto para o dia a dia"],
       "Guia de uso responsável de IA", "O colégio sai da imersão com um guia próprio de uso de IA para alunos e professores."),
    ]
    tabs = "".join(f'<button class="ct-tab{" on" if i==0 else ""}" role="tab" aria-selected="{"true" if i==0 else "false"}" aria-controls="tr-{k}" id="tb-{k}" style="--c:{c}"><small>{t}</small>{n}</button>' for i,(k,t,n,s,c,m,pf,pd) in enumerate(TR))
    panels = "".join(f'''<div class="ct-panel{" on" if i==0 else ""}" role="tabpanel" id="tr-{k}" aria-labelledby="tb-{k}" style="--c:{c}"{"" if i==0 else " hidden"}>
  <div class="ct-pl"><span class="ct-age">{t}</span><h3>{n}</h3><p class="ct-sub">{s}</p>
    <ol class="ct-mods">{"".join(f"<li><span>{j+1:02d}</span>{x}</li>" for j,x in enumerate(m))}</ol></div>
  <div class="ct-final"><span class="ct-stamp">Projeto final</span><h4>{pf}</h4><p>{pd}</p><div class="ct-doodle" aria-hidden="true">{["📚","💬","🚀","🧭"][i]}</div></div>
</div>''' for i,(k,t,n,s,c,m,pf,pd) in enumerate(TR))
    return f'''{PROD_CSS}
<div class="cl">
<section class="cl-hero">
  <div class="wrap cl-hero-grid">
    <div class="stack" style="gap:22px">
      <span class="cl-kicker"><b>IA no Colégio</b> · curso extracurricular da M7</span>
      <h1>A IA já está na mochila dos seus alunos. <mark>Ensine a usar bem.</mark></h1>
      <p class="cl-lead">Curso de inteligência artificial dentro do próprio colégio, do 3º ano do fundamental ao ensino médio, com uma trilha para professores. Criatividade, pensamento crítico e responsabilidade, com projetos que os pais vão ver.</p>
      <div class="row"><a class="cl-btn" href="#conversa">Agendar uma conversa {ARROW}</a><a class="cl-btn ghost" href="#trilhas">Ver as 4 trilhas</a></div>
      <div class="cl-chips"><span>4 trilhas</span><span>Ciclos de 12 semanas</span><span>Turmas de até 9 alunos</span><span>Demo Day para os pais</span></div>
    </div>
    <div class="cl-board reveal" aria-hidden="true">
      <div class="cl-chat">
        <div class="msg me">Faz minha redação sobre o meio ambiente?</div>
        <div class="msg ai">Posso te ajudar a <b>pensar</b> nela. Qual problema do seu bairro você queria resolver?</div>
        <div class="msg me">O lixo na praça perto da escola.</div>
        <div class="msg ai typing"><i></i><i></i><i></i></div>
      </div>
      <span class="cl-sticker s1">✓ checou a fonte</span>
      <span class="cl-sticker s2">✍️ autoria do aluno</span>
      <span class="cl-sticker s3">★ prompt nota 10</span>
    </div>
  </div>
</section>

<section class="cl-band">
  <div class="wrap">
    <div class="cl-head reveal"><span class="cl-eye">Por que agora</span><h2>A pergunta não é <s>se</s> os alunos vão usar IA. É <mark>se vão usar bem</mark>.</h2></div>
    <div class="cl-pains">
      <div class="cl-pain reveal"><b>📱</b><h3>A IA já chegou</h3><p>Está no celular, nas tarefas e nas pesquisas dos alunos, com ou sem a escola.</p></div>
      <div class="cl-pain reveal"><b>👨‍👩‍👧</b><h3>Os pais querem futuro</h3><p>As famílias querem os filhos preparados para o mundo que já está aí.</p></div>
      <div class="cl-pain reveal"><b>🧑‍🏫</b><h3>Professores sem chão</h3><p>Cola, autoria e uso de IA em sala viraram dúvida de todo dia.</p></div>
      <div class="cl-pain reveal"><b>🏫</b><h3>Diferencial na matrícula</h3><p>O colégio precisa mostrar inovação concreta para atrair novas famílias.</p></div>
    </div>
    <p class="cl-quote reveal">“A IA não é um problema para o colégio. Ela ajuda alunos e professores quando é usada com criatividade, pensamento crítico e responsabilidade.”</p>
  </div>
</section>

<section class="cl-band paper" id="trilhas">
  <div class="wrap">
    <div class="cl-head reveal"><span class="cl-eye">A proposta</span><h2>Quatro trilhas, uma para cada fase.</h2><p>Escolha uma trilha ou monte o programa completo. Toque em cada trilha para ver os módulos.</p></div>
    <div class="ct" data-tabs>
      <div class="ct-tabs" role="tablist">{tabs}</div>
      {panels}
    </div>
  </div>
</section>

<section class="cl-band dark">
  <div class="wrap">
    <div class="cl-head reveal"><span class="cl-eye light">A jornada do ciclo</span><h2>12 semanas que terminam num palco.</h2><p>Uma aula de 50 minutos por semana, por turma. No fim, os alunos apresentam o que criaram.</p></div>
    <div class="cl-road">
      <div class="cl-road-line"><i></i></div>
      <div class="cl-stop reveal"><span>Semana 1</span><h3>Aula inaugural</h3><p>Palestra de lançamento para os pais e primeiro contato da turma com a IA.</p></div>
      <div class="cl-stop reveal"><span>Semanas 2 a 6</span><h3>Fundamentos</h3><p>Como a IA funciona, prompts, segurança e pensamento crítico.</p></div>
      <div class="cl-stop reveal"><span>Semanas 7 a 11</span><h3>Mão na massa</h3><p>Cada turma desenvolve o seu projeto, com orientação a cada aula.</p></div>
      <div class="cl-stop reveal big"><span>Semana 12</span><h3>Mostra ou Demo Day</h3><p>Os alunos apresentam os projetos para os pais e para o colégio.</p></div>
    </div>
  </div>
</section>

<section class="cl-band">
  <div class="wrap">
    <div class="cl-head reveal"><span class="cl-eye">Quem ganha</span><h2>Bom para o colégio, para os pais e para os professores.</h2></div>
    <div class="cl-wins">
      <div class="cl-win reveal" style="--c:#6C4CF5"><span class="cl-win-ico">🏫</span><h3>O colégio</h3><ul><li>Diferencial forte na captação de novos alunos</li><li>Posicionamento de colégio inovador e responsável</li><li>Conteúdo pronto para o Instagram e as campanhas</li></ul></div>
      <div class="cl-win reveal" style="--c:#FF7A45"><span class="cl-win-ico">👨‍👩‍👧</span><h3>Os pais</h3><ul><li>Veem o que os filhos criaram na mostra e no Demo Day</li><li>Sabem que a IA está sendo usada com segurança</li><li>Filhos mais preparados para o futuro</li></ul></div>
      <div class="cl-win reveal" style="--c:#12B886"><span class="cl-win-ico">🧑‍🏫</span><h3>Os professores</h3><ul><li>Mais produtivos com aulas, provas e rubricas</li><li>Seguros para lidar com alunos que usam IA</li><li>Kit de prompts e guia de uso responsável</li></ul></div>
    </div>
  </div>
</section>

<section class="cl-band paper">
  <div class="wrap cl-show">
    <div class="stack reveal" style="gap:16px">
      <span class="cl-eye">O grande final</span>
      <h2>A mostra que os pais <mark>não esquecem</mark>.</h2>
      <p>No fim de cada ciclo o colégio abre as portas: os pequenos apresentam o livro ilustrado da turma, os do fundamental II mostram chatbots e campanhas e o ensino médio sobe ao palco no Demo Day. É inovação que as famílias enxergam e compartilham.</p>
      <ul class="cl-ticks"><li>Evento aberto às famílias</li><li>Fotos e vídeos prontos para as redes do colégio</li><li>Projetos com autoria dos alunos</li></ul>
    </div>
    <div class="cl-invite reveal" aria-hidden="true">
      <span class="cl-inv-tag">Convite</span>
      <h3>Demo Day<br><small>IA no Colégio</small></h3>
      <p>Venha ver o que a turma criou com inteligência artificial.</p>
      <div class="cl-inv-row"><span>📅 Fim do ciclo</span><span>📍 No colégio</span></div>
      <div class="cl-inv-proj"><i>Livro da turma</i><i>Chatbot da cantina</i><i>App de estudos</i></div>
    </div>
  </div>
</section>

<section class="cl-band">
  <div class="wrap">
    <div class="cl-head reveal"><span class="cl-eye">Segurança e ética</span><h2>IA ensinada com responsabilidade, do primeiro ao último dia.</h2></div>
    <div class="cl-rules">
      <div class="reveal"><b>🔒</b><h3>Dados protegidos</h3><p>Os alunos aprendem o que nunca compartilhar com a IA, e as atividades seguem a LGPD.</p></div>
      <div class="reveal"><b>✍️</b><h3>Autoria em primeiro lugar</h3><p>A IA ajuda a pensar, não faz pelo aluno. Cola e autoria são temas das aulas.</p></div>
      <div class="reveal"><b>🔎</b><h3>Pensamento crítico</h3><p>Checar fontes, reconhecer erros da IA e identificar fake news e deepfakes.</p></div>
      <div class="reveal"><b>📘</b><h3>Guia do colégio</h3><p>Professores saem com um guia de uso responsável de IA para toda a escola.</p></div>
    </div>
  </div>
</section>

<section class="cl-band dark">
  <div class="wrap">
    <div class="cl-head reveal"><span class="cl-eye light">Como funciona</span><h2>Simples para o colégio. A M7 cuida do resto.</h2></div>
    <div class="cl-stats">
      <div class="reveal"><b>50 min</b><span>de aula por semana, por turma</span></div>
      <div class="reveal"><b>12</b><span>semanas por ciclo</span></div>
      <div class="reveal"><b>até 9</b><span>alunos por turma, conforme os computadores</span></div>
      <div class="reveal"><b>3 h</b><span>de imersão para os professores, num único dia</span></div>
    </div>
    <div class="cl-split">
      <div><h3>A M7 leva</h3><ul><li>Conteúdo e material didático</li><li>As aulas, do primeiro ao último encontro</li><li>A organização da mostra ou do Demo Day</li></ul></div>
      <div><h3>O colégio oferece</h3><ul><li>O espaço e os computadores</li><li>A comunicação com os pais</li><li>Os dias e horários das turmas</li></ul></div>
    </div>
  </div>
</section>

<section class="cl-band paper" id="conversa">
  <div class="wrap cl-cta">
    <div class="stack" style="gap:18px">
      <span class="cl-eye">Próximos passos</span>
      <h2>Leve IA para o seu colégio. <mark>Agende uma conversa</mark> e conheça as trilhas.</h2>
      <ol class="cl-next"><li><b>Conversa</b> com a direção para validar as trilhas e o formato</li><li><b>Turmas:</b> dias, horários e tamanho</li><li><b>Parceria</b> e calendário do ciclo</li><li><b>Lançamento</b> com palestra para os pais</li></ol>
      <a class="cl-wa" data-wa="Olá! Vim pelo site da M7 e quero levar o IA no Colégio para o meu colégio. Podemos agendar uma conversa?">Prefere o WhatsApp? Fale direto com a M7 {ARROW}</a>
    </div>
    <div class="cl-form reveal">
      <h3>Agende uma conversa</h3>
      <p class="small">Em 20 minutos mostramos as trilhas e montamos o formato ideal para o seu colégio.</p>
      {lead_form("IA no Colégio (agendar conversa)", """<div class="two"><div class="field"><label for="f-colegio">Colégio</label><input id="f-colegio" name="colegio" autocomplete="organization" placeholder="Nome do colégio"></div><div class="field"><label for="f-cargo">Seu cargo</label><select id="f-cargo" name="cargo"><option value="">Selecione</option><option>Mantenedor(a) / dono(a)</option><option>Diretor(a)</option><option>Coordenador(a)</option><option>Professor(a)</option><option>Outro</option></select></div></div>
  <div class="two"><div class="field"><label for="f-cidade">Cidade</label><input id="f-cidade" name="cidade" placeholder="Ex.: São Paulo"></div><div class="field"><label for="f-trilha">Interesse</label><select id="f-trilha" name="interesse"><option value="">Selecione</option><option>Programa completo</option><option>Exploradores (3º ao 5º)</option><option>Criadores (6º ao 9º)</option><option>IA para o Futuro (médio)</option><option>Imersão de professores</option></select></div></div>""", "Agendar uma conversa")}
    </div>
  </div>
</section>

<section class="cl-band">
  <div class="wrap">
    <div class="cl-head"><span class="cl-eye">Perguntas frequentes</span><h2>Antes de você perguntar.</h2></div>
    {faq(col_faq)}
    <p class="cl-sign">IA no Colégio é um programa da <a href="ia-para-empresas.html">M7 Automação</a>, especialista em agentes de inteligência artificial.</p>
  </div>
</section>
</div>'''
