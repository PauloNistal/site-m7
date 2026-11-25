# Produtos próprios da M7 (vitrine + landing pages). Importado pelo build.py.
# Regras comerciais (Paulo, 24/11/2026):
# - Bem-te-li: preço público de clínica R$ 199/mês e de família R$ 39,90 / R$ 29,90 no anual.
#   Nunca citar a oferta "Clínica Fundadora" nem clínicas em negociação. Falar com pais e profissionais, nunca com a criança.
# - IA no Colégio: sem preço no site (funciona como apresentação comercial), CTA "agende uma conversa".

PROD_CSS = '<link rel="stylesheet" href="/assets/produtos.css">'

BIRD = '''<svg class="bird" viewBox="0 0 120 100" aria-hidden="true">
  <g class="bird-body">
    <path d="M20 62c0-22 18-38 40-38 16 0 28 8 34 20l18 4-16 8c-4 18-20 30-38 30C34 86 20 78 20 62Z" fill="#FFC72C"/>
    <path d="M60 24c10 0 20 5 26 12-10-2-22 0-30 6-6-6-6-14 4-18Z" fill="#1D2B5E"/>
    <circle cx="80" cy="44" r="5" fill="#1D2B5E"/><circle cx="81.5" cy="42.5" r="1.6" fill="#fff"/>
    <path d="M94 44l18 4-16 8Z" fill="#F08A24"/>
    <path d="M62 86l-4 10M72 85l2 10" stroke="#1D2B5E" stroke-width="3" stroke-linecap="round"/>
  </g>
  <path class="bird-wing" d="M30 58c8-14 26-18 38-10-6 14-22 22-38 10Z" fill="#1D2B5E"/>
</svg>'''

ORBIT = '''<svg class="orbit" viewBox="0 0 200 200" aria-hidden="true">
  <defs><linearGradient id="og" x1="0" x2="1"><stop offset="0" stop-color="#9eb4d5"/><stop offset="1" stop-color="#ee4553"/></linearGradient></defs>
  <circle cx="100" cy="100" r="34" fill="none" stroke="url(#og)" stroke-width="1.4"/>
  <circle cx="100" cy="100" r="62" fill="none" stroke="rgba(158,180,213,.35)" stroke-dasharray="3 6"/>
  <circle cx="100" cy="100" r="88" fill="none" stroke="rgba(158,180,213,.2)"/>
  <g class="o1"><circle cx="100" cy="38" r="6" fill="#9eb4d5"/></g>
  <g class="o2"><circle cx="188" cy="100" r="5" fill="#ee4553"/></g>
  <g class="o3"><circle cx="100" cy="188" r="4" fill="#d6e3f5"/></g>
  <path d="M84 108v-14l16-8 16 8v14M92 102v10M108 102v10M80 94l20-10 20 10" fill="none" stroke="#eef2f8" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>'''


def vitrine(ARROW, titulo="Produtos M7", h2="Agentes de IA que a M7 já <em>empacotou</em> em produto.", lead="Além dos projetos sob medida, a M7 cria produtos próprios de IA. A mesma tecnologia de agentes que implantamos nas empresas, pronta para usar."):
    return f'''{PROD_CSS}
<section class="x-sec prod-sec" id="produtos">
  <div class="wrap">
    <div class="x-head reveal"><span class="x-label">{titulo}</span><h2 class="x-h2">{h2}</h2><p class="lead">{lead}</p></div>
    <div class="prods">
      <a class="prod prod-bt reveal" href="bem-te-li.html">
        <span class="prod-tag">Saúde e educação infantil</span>
        <div class="prod-art">{BIRD}<div class="prod-bars" aria-hidden="true"><i style="--h:38%"></i><i style="--h:52%"></i><i style="--h:61%"></i><i style="--h:74%"></i><i style="--h:88%"></i></div></div>
        <h3>Bem-te-li</h3>
        <p>App que treina a leitura em voz alta de crianças de 7 a 10 anos e mede a evolução com IA entre uma sessão de terapia e outra. Com a marca da sua clínica.</p>
        <ul><li>4 agentes de IA</li><li>White label</li><li>Lista de espera para famílias</li></ul>
        <span class="go">Conhecer o Bem-te-li {ARROW}</span>
      </a>
      <a class="prod prod-col reveal" href="ia-no-colegio.html">
        <span class="prod-tag">Para colégios particulares</span>
        <div class="prod-art">{ORBIT}</div>
        <h3>IA no Colégio</h3>
        <p>Curso extracurricular de inteligência artificial dentro do colégio, do 3º ano do fundamental ao ensino médio, com uma trilha para professores.</p>
        <ul><li>4 trilhas</li><li>Ciclos de 12 semanas</li><li>Mostra e Demo Day para os pais</li></ul>
        <span class="go">Ver as trilhas {ARROW}</span>
      </a>
    </div>
  </div>
</section>'''


def build(ARROW, card, faq, faq_schema, lead_form):
    # ---------------- BEM-TE-LI ----------------
    bt_faq = [
     ("O Bem-te-li substitui a terapia?", "Não. O Bem-te-li não diagnostica e não substitui o fonoaudiólogo ou o psicopedagogo. A IA escuta, mede e organiza a leitura. Diagnóstico e conduta são sempre do profissional."),
     ("Para que idade ele foi feito?", "Para crianças de 7 a 10 anos com dificuldade de leitura, com textos ajustados à idade, ao ano escolar e aos interesses de cada uma."),
     ("Precisa baixar aplicativo?", "Não. É um app web: abre no navegador do celular ou do tablet, sem loja de aplicativos."),
     ("E a voz da criança, fica guardada?", "Só é gravada com o consentimento específico dos pais ou responsáveis. O áudio é apagado automaticamente em até 3 dias. Ficam apenas a transcrição e as métricas de leitura."),
     ("Quanto custa?", "Para famílias, R$ 39,90 por mês ou R$ 29,90 por mês no plano anual, com 7 dias grátis e 50% de desconto na segunda criança. Para clínicas, a partir de R$ 199 por mês para até 10 crianças."),
     ("Já está disponível?", "O Bem-te-li está em pré-lançamento. Clínicas e profissionais já podem conversar com a M7 para começar. Famílias podem entrar na lista de espera e são avisadas primeiro."),
    ]
    bt = f'''{PROD_CSS}
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@600;700;800&family=Nunito+Sans:wght@400;600;700&display=swap">
<div class="bt">
<section class="bt-hero">
  <div class="wrap bt-hero-grid">
    <div class="stack" style="gap:22px">
      <span class="bt-kicker">Bem-te-li <small>by M7 Automação</small></span>
      <h1>A criança lê. <span>A IA escuta.</span> O profissional acompanha a evolução.</h1>
      <p class="bt-lead">App que treina a leitura em voz alta de crianças de 7 a 10 anos com dificuldade de leitura e mede a evolução delas com IA, entre uma sessão de terapia e outra.</p>
      <div class="row"><a class="bt-btn blue" href="#clinicas">Sou clínica ou profissional {ARROW}</a><a class="bt-btn yellow" href="#familias">Sou mãe, pai ou responsável</a></div>
      <p class="bt-note">Em pré-lançamento · app web, abre no celular ou tablet</p>
    </div>
    <div class="bt-phone reveal" aria-hidden="true">
      {BIRD}
      <div class="bt-screen">
        <div class="bt-sc-top"><b>Treino do dia</b><span>★ 3 dias seguidos</span></div>
        <div class="bt-text"><p><span class="r">O</span> <span class="r">time</span> <span class="r">entrou</span> <span class="r">em</span> <span class="r">campo</span> <span class="r">e</span> <span class="r">a</span> <span class="r">torcida</span> <span class="r">gritou</span> <span class="r">o</span> <span class="r">nome</span> <span class="r">do</span> <span class="r">goleiro.</span></p></div>
        <div class="bt-wave"><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div>
        <div class="bt-metrics"><div><small>PCPM</small><b class="count" data-to="62">62</b></div><div><small>Precisão</small><b>94%</b></div><div><small>Meta do ano</small><b>65</b></div></div>
      </div>
    </div>
  </div>
</section>

<section class="bt-band cream">
  <div class="wrap bt-split">
    <div class="bt-big reveal"><b>50</b><span>minutos por semana com o profissional</span></div>
    <div class="bt-big reveal"><b>167</b><span>horas por semana sem ninguém medindo a leitura</span></div>
    <div class="stack reveal" style="gap:14px">
      <h2>O problema não está na sessão. Está no intervalo entre elas.</h2>
      <p>O fono ou o psicopedagogo vê a criança cerca de 50 minutos por semana. Nas outras 167 horas, ninguém mede como ela está lendo, e os pais não têm tempo nem técnica para acompanhar com método. O Bem-te-li cuida desse intervalo.</p>
    </div>
  </div>
</section>

<section class="bt-band">
  <div class="wrap">
    <div class="bt-head reveal"><span class="bt-eyebrow">Como funciona</span><h2>Quatro agentes de IA trabalhando juntos para a criança ler melhor.</h2><p>Cada leitura passa pelos quatro agentes, e o resultado de uma leitura ajusta o texto da próxima.</p></div>
    <div class="bt-agents">
      <div class="bt-agent reveal"><span class="n">1</span><h3>Redator</h3><p>Escreve o texto no nível certo para cada criança: idade, ano escolar, interesses e o foco definido pelo profissional. Quem gosta de futebol lê sobre futebol.</p></div>
      <div class="bt-agent reveal"><span class="n">2</span><h3>Ouvinte</h3><p>Escuta a leitura em voz alta e transcreve palavra por palavra.</p></div>
      <div class="bt-agent reveal"><span class="n">3</span><h3>Analista</h3><p>Mede palavras corretas por minuto (PCPM), precisão e padrões de erro, como trocas de letras, omissões e hesitações.</p></div>
      <div class="bt-agent reveal"><span class="n">4</span><h3>Relator</h3><p>Entrega um resumo simples para a família e a curva de evolução no painel do profissional.</p></div>
    </div>
  </div>
</section>

<section class="bt-band cream">
  <div class="wrap">
    <div class="bt-head reveal"><span class="bt-eyebrow">O que o Bem-te-li entrega</span><h2>Método entre as sessões, com as métricas que o profissional já usa.</h2></div>
    <div class="bt-grid">
      <div class="bt-card reveal"><h3>Texto no nível certo</h3><p>Textos feitos para cada criança, com o foco que o profissional definir.</p></div>
      <div class="bt-card reveal"><h3>Medição automática</h3><p>PCPM, precisão e tipo de erro em cada leitura, sem planilha.</p></div>
      <div class="bt-card reveal"><h3>Régua por ano escolar</h3><p>Fluência comparada à referência do CAEd para cada ano. Exemplo: cerca de 65 PCPM ao fim do 2º ano.</p></div>
      <div class="bt-card reveal"><h3>Relatório e painel</h3><p>Resumo semanal simples para a família e painel técnico com todos os pacientes para o profissional.</p></div>
      <div class="bt-card reveal"><h3>Treino que engaja</h3><p>Estrelas, dias seguidos e medalhas para manter o hábito de ler em casa.</p></div>
      <div class="bt-card reveal"><h3>Privacidade de verdade</h3><p>Gravação só com consentimento dos pais. Áudio apagado em até 3 dias.</p></div>
    </div>
  </div>
</section>

<section class="bt-band navy" id="clinicas">
  <div class="wrap bt-offer">
    <div class="stack" style="gap:18px">
      <span class="bt-eyebrow light">Para clínicas, profissionais e escolas</span>
      <h2>Um app de leitura com a marca da sua clínica.</h2>
      <p>O Bem-te-li sai com o logo, as cores e o endereço da sua clínica. A família vê a sua clínica, não a M7. Você acompanha todos os pacientes num painel só, sem desenvolver nada.</p>
      <ul class="bt-checks"><li>White label completo, pronto para usar</li><li>Painel com a curva de evolução de cada paciente</li><li>Relatórios automáticos para as famílias</li><li>Dados de cada clínica isolados: uma não enxerga a outra</li></ul>
      <div class="bt-mini">
        <div><b>Profissional autônomo</b><p>Painel gratuito para acompanhar seus pacientes. As famílias deles ganham cupom de desconto na assinatura.</p></div>
        <div><b>Escolas</b><p>Acompanhamento da fluência da turma pela coordenação. Fale com a gente para um piloto.</p></div>
      </div>
    </div>
    <div class="bt-price reveal">
      <span class="bt-eyebrow">Clínica white label</span>
      <div class="bt-amount"><small>R$</small>199<small>/mês</small></div>
      <p>até 10 crianças</p>
      <ul><li>+ R$ 15/mês por criança extra</li><li>Implantação com a sua marca: de R$ 497 a R$ 997, conforme a personalização</li></ul>
      <a class="bt-btn yellow" data-wa="Olá! Vim pelo site da M7 e quero conhecer o Bem-te-li para a minha clínica.">Quero o Bem-te-li na minha clínica {ARROW}</a>
      <a class="bt-link" data-wa="Olá! Vim pelo site da M7. Sou profissional autônomo(a) e quero conhecer o painel do Bem-te-li.">Sou autônomo(a) e quero o painel gratuito</a>
      <a class="bt-link" data-wa="Olá! Vim pelo site da M7 e quero conhecer o Bem-te-li para a minha escola.">Sou de uma escola e quero saber mais</a>
    </div>
  </div>
</section>

<section class="bt-band yellow" id="familias">
  <div class="wrap bt-offer">
    <div class="stack" style="gap:18px">
      <span class="bt-eyebrow">Para famílias</span>
      <h2>Treino de leitura em casa, com relatório toda semana.</h2>
      <p>Seu filho lê um texto feito para ele, a IA mede a leitura e você recebe um resumo simples da evolução. O Bem-te-li está em pré-lançamento: entre na lista de espera e seja avisado primeiro.</p>
      <div class="bt-price light">
        <div class="bt-plans">
          <div><span>Mensal</span><b>R$ 39,90</b><small>/mês</small></div>
          <div class="hl"><span>Anual</span><b>R$ 29,90</b><small>/mês</small></div>
        </div>
        <ul><li>7 dias grátis para testar</li><li>2ª criança com 50% de desconto</li><li>Sem baixar nada: abre no navegador</li></ul>
      </div>
    </div>
    <div class="bt-form reveal">
      <h3>Lista de espera</h3>
      <p class="small">Pedimos só os dados do responsável. Nenhum dado da criança é coletado aqui.</p>
      {lead_form("Lista de espera Bem-te-li (família)", '''<div class="field"><label for="f-ano">Ano escolar da criança</label><select id="f-ano" name="ano_escolar"><option value="">Selecione</option><option>1º ano</option><option>2º ano</option><option>3º ano</option><option>4º ano</option><option>5º ano</option><option>Outro</option></select></div>
  <div class="field"><label for="f-acomp">Faz acompanhamento com fono ou psicopedagogo?</label><select id="f-acomp" name="acompanhamento"><option value="">Selecione</option><option>Sim</option><option>Não</option><option>Ainda vou procurar</option></select></div>''', "Entrar na lista de espera", note='Seus dados ficam só com a M7 (<a href="/politica-de-privacidade">política de privacidade</a>). Avisamos pelo WhatsApp quando abrir.')}
    </div>
  </div>
</section>

<section class="bt-band">
  <div class="wrap">
    <div class="bt-head reveal"><span class="bt-eyebrow">Privacidade e ética</span><h2>Voz de criança só é gravada com consentimento dos pais. E some em até 3 dias.</h2></div>
    <div class="bt-grid">
      <div class="bt-card"><h3>Consentimento específico</h3><p>Termo próprio para pais e responsáveis, conforme a LGPD (art. 14) e o ECA Digital. Sem o termo aceito, a gravação fica bloqueada.</p></div>
      <div class="bt-card"><h3>Áudio apagado</h3><p>O áudio é apagado automaticamente em até 3 dias. Ficam só a transcrição e as métricas.</p></div>
      <div class="bt-card"><h3>Controle total</h3><p>Apagar a criança apaga todos os dados dela. No white label, a clínica é a controladora dos dados.</p></div>
    </div>
  </div>
</section>

<section class="bt-band cream">
  <div class="wrap">
    <div class="bt-head"><span class="bt-eyebrow">Perguntas frequentes</span><h2>Antes de você perguntar.</h2></div>
    {faq(bt_faq)}
    <p class="bt-sign">Bem-te-li é um produto da <a href="ia-para-empresas.html">M7 Automação</a>, especialista em agentes de IA.</p>
  </div>
</section>
</div>'''

    # ---------------- IA NO COLÉGIO ----------------
    col_faq = [
     ("O colégio precisa ter laboratório de informática?", "Precisa de computadores para os alunos. O tamanho das turmas é definido pelo número de máquinas disponíveis (referência: até 9 alunos por turma)."),
     ("Quem dá as aulas?", "A M7. Levamos o conteúdo, o material didático e as aulas. O colégio cuida do espaço, dos computadores e da comunicação com os pais."),
     ("Como os pais participam?", "No fim de cada ciclo há uma mostra ou um Demo Day com os projetos dos alunos, aberto às famílias. Também sugerimos uma palestra de lançamento para os pais."),
     ("E os professores?", "A Trilha Professores é uma imersão de um dia, de cerca de 3 horas, com planejamento de aulas, provas e rubricas com IA e um guia de uso responsável para o colégio."),
     ("Quanto custa?", "O investimento depende do número de turmas e das trilhas escolhidas. Apresentamos a proposta na conversa, depois de entender o colégio."),
    ]
    trilha = lambda tag, nome, sub, itens, final: f'<div class="trilha reveal"><span class="tag">{tag}</span><h3>{nome}</h3><p>{sub}</p><ul>{"".join(f"<li>{i}</li>" for i in itens)}</ul><p class="final"><b>Projeto final:</b> {final}</p></div>'
    col = f'''{PROD_CSS}
<section class="hero x-hero lp col-hero">
  <div class="x-grid" aria-hidden="true"></div>
  <div class="wrap hero-grid">
    <div class="stack" style="gap:24px">
      <span class="eyebrow">IA no Colégio · curso extracurricular da M7</span>
      <h1>A IA já está na mochila dos seus alunos. <strong>Ensine a usar bem.</strong></h1>
      <p class="lead">Curso de inteligência artificial dentro do próprio colégio, para alunos do 3º ano do fundamental ao ensino médio e para professores. Com criatividade, pensamento crítico e responsabilidade.</p>
      <div class="row"><a class="btn btn-red" data-wa="Olá! Vim pelo site da M7 e quero levar o IA no Colégio para o meu colégio. Podemos agendar uma conversa?">Agendar uma conversa {ARROW}</a><a class="btn btn-ghost" href="#trilhas">Conhecer as trilhas</a></div>
    </div>
    <div class="col-art reveal">{ORBIT}</div>
  </div>
</section>

<section class="band alt">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">Por que agora</span><h2>A pergunta não é se os alunos vão usar IA. É se vão usar bem.</h2></div>
    <div class="grid g4">
      {card("chat", "A IA já chegou", "Está no celular, nas tarefas e nas pesquisas dos alunos, com ou sem a escola.")}
      {card("light", "Pais querem futuro", "As famílias querem os filhos preparados para o mundo que vem aí.")}
      {card("shield", "Professores sem chão", "Cola, autoria e uso de IA em sala viraram dúvida diária.")}
      {card("chart", "Diferencial na matrícula", "O colégio precisa mostrar inovação concreta para atrair novas famílias.")}
    </div>
  </div>
</section>

<section class="band" id="trilhas">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">A proposta</span><h2>Quatro trilhas, uma para cada fase.</h2><p class="lead">A IA não é um problema para o colégio. Ela ajuda alunos e professores quando é usada com criatividade, pensamento crítico e responsabilidade.</p></div>
    <div class="trilhas">
      {trilha("3º ao 5º ano", "Exploradores de IA", "Aprender o que é IA brincando, com criatividade e segurança.", ["Histórias e desenhos com IA", "Caça aos erros da IA", "Segurança: o que não contar para a IA"], "livro ilustrado da turma, apresentado numa mostra para os pais.")}
      {trilha("6º ao 9º ano", "Criadores de IA", "Usar IA para estudar, criar e pensar criticamente.", ["A arte do prompt e a IA como tutor de estudos", "Fake news, deepfakes e checagem", "Ética: cola, autoria e uso honesto"], "chatbot ou campanha criativa sobre um tema do colégio.")}
      {trilha("Ensino médio", "IA para o Futuro", "IA aplicada ao vestibular, à carreira e ao empreendedorismo.", ["IA para o ENEM e os vestibulares", "Automação e criação de um assistente próprio", "Profissões do futuro, dados, LGPD e ética"], "protótipo apresentado num Demo Day.")}
      {trilha("Professores", "IA na Sala de Aula", "Professores como aliados, ganhando tempo no dia a dia.", ["Planejamento de aulas, provas e rubricas com IA", "Como lidar com alunos que usam IA", "Kit de prompts para o dia a dia"], "guia de uso responsável de IA do colégio.")}
    </div>
  </div>
</section>

<section class="band alt">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">Como funciona</span><h2>Simples para o colégio, marcante para os alunos.</h2></div>
    <div class="col-stats">
      <div class="reveal"><b>50 min</b><span>aula semanal por turma</span></div>
      <div class="reveal"><b>12</b><span>semanas por ciclo</span></div>
      <div class="reveal"><b>até 9</b><span>alunos por turma, conforme os computadores</span></div>
      <div class="reveal"><b>3 h</b><span>de imersão para os professores, num único dia</span></div>
    </div>
    <div class="compare" style="margin-top:32px">
      <div class="after"><h3>A M7 leva</h3><ul><li>Conteúdo e material didático</li><li>As aulas, do primeiro ao último encontro</li><li>A mostra ou o Demo Day de fim de ciclo</li></ul></div>
      <div class="before"><h3>O colégio oferece</h3><ul><li>O espaço e os computadores</li><li>A comunicação com os pais</li><li>Os dias e horários das turmas</li></ul></div>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">O que o colégio ganha</span><h2>Inovação que os pais enxergam.</h2></div>
    <ul class="checks col-gains"><li>Diferencial forte na captação de novos alunos</li><li>Pais engajados com a mostra de projetos e o Demo Day</li><li>Professores mais produtivos e seguros com a tecnologia</li><li>Conteúdo pronto para o Instagram e as campanhas do colégio</li><li>Posicionamento de colégio inovador e responsável no uso de IA</li></ul>
  </div>
</section>

<section class="band alt" id="conversa">
  <div class="wrap form-wrap">
    <div class="stack" style="gap:20px">
      <span class="eyebrow">Próximos passos</span>
      <h2>Leve IA para o seu colégio: agende uma conversa e conheça as trilhas.</h2>
      <div class="steps col-steps">
        <div class="step"><h3>Conversa</h3><p>Validamos as trilhas e o formato com a direção.</p></div>
        <div class="step"><h3>Turmas</h3><p>Definimos dias, horários e tamanho das turmas.</p></div>
        <div class="step"><h3>Parceria</h3><p>Fechamos o modelo e o calendário do ciclo.</p></div>
        <div class="step"><h3>Lançamento</h3><p>Palestra para os pais e início do primeiro ciclo.</p></div>
      </div>
    </div>
    {lead_form("IA no Colégio (agendar conversa)", '''<div class="two"><div class="field"><label for="f-colegio">Colégio</label><input id="f-colegio" name="colegio" autocomplete="organization" placeholder="Nome do colégio"></div><div class="field"><label for="f-cargo">Seu cargo</label><select id="f-cargo" name="cargo"><option value="">Selecione</option><option>Mantenedor(a) / dono(a)</option><option>Diretor(a)</option><option>Coordenador(a)</option><option>Professor(a)</option><option>Outro</option></select></div></div>
  <div class="field"><label for="f-cidade">Cidade</label><input id="f-cidade" name="cidade" placeholder="Ex.: São Paulo"></div>''', "Agendar uma conversa")}
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">Perguntas frequentes</span><h2>Antes de você perguntar.</h2></div>
    {faq(col_faq)}
  </div>
</section>'''

    bt_schema = [faq_schema(bt_faq), {"@context": "https://schema.org", "@type": "SoftwareApplication", "name": "Bem-te-li", "applicationCategory": "EducationalApplication", "operatingSystem": "Web", "description": "App que treina a leitura em voz alta de crianças de 7 a 10 anos e mede a evolução com IA.", "publisher": {"@id": "https://m7automacao.com.br/#empresa"}, "offers": [{"@type": "Offer", "name": "Família mensal", "price": "39.90", "priceCurrency": "BRL"}, {"@type": "Offer", "name": "Clínica white label", "price": "199.00", "priceCurrency": "BRL"}]}]
    col_schema = [faq_schema(col_faq), {"@context": "https://schema.org", "@type": "Course", "name": "IA no Colégio", "description": "Curso extracurricular de inteligência artificial para alunos do 3º ano do fundamental ao ensino médio e para professores.", "provider": {"@type": "Organization", "name": "M7 Automação", "sameAs": "https://m7automacao.com.br"}}]
    return [
      ("bem-te-li.html", "Bem-te-li: treino de leitura com IA para crianças | M7", "App que treina a leitura em voz alta de crianças de 7 a 10 anos e mede a evolução com IA entre as sessões. White label para clínicas e lista de espera para famílias.", bt, False, bt_schema),
      ("ia-no-colegio.html", "IA no Colégio: curso de inteligência artificial para escolas | M7", "Curso extracurricular de IA dentro do colégio, do 3º ano do fundamental ao ensino médio, com trilha para professores. Agende uma conversa.", col, False, col_schema),
    ]
