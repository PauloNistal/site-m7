/* Home v2 — partículas que se reorganizam em formas (M7, empresa, casa, prédio) e o diagrama vivo do cérebro M7. */
(function () {
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- HERO: morph de partículas ---------- */
  const hero = document.querySelector(".x-hero");
  const cv = document.getElementById("swarm");
  const rotWord = document.getElementById("rot-word");
  const dots = [...document.querySelectorAll(".x-rot .dots span")];
  const STAGES = [
    { word: "Na sua empresa.", shape: "chat" },
    { word: "Na sua casa.", shape: "house" },
    { word: "No seu prédio.", shape: "building" },
    { word: "Feito pela M7.", shape: "m7" },
  ];

  const LP = hero && hero.classList.contains("lp");
  const SEQ = hero && hero.dataset.shapes ? hero.dataset.shapes.split(",").map((s) => ({ shape: s })) : STAGES;
  const CASA = document.body.classList.contains("casa");
  const C1 = CASA ? [240, 220, 176] : [158, 180, 213], C2 = CASA ? [196, 140, 70] : [238, 69, 83];
  if (cv && hero) {
    const ctx = cv.getContext("2d");
    let W = 0, H = 0, DPR = 1, parts = [], shapes = {}, stage = 0;
    const mouse = { x: -9999, y: -9999 };
    const mobile = () => W < 900;

    function sample(draw, n) {
      const S = 220, off = document.createElement("canvas");
      off.width = off.height = S;
      const o = off.getContext("2d");
      o.fillStyle = "#fff"; o.strokeStyle = "#fff";
      draw(o, S);
      const d = o.getImageData(0, 0, S, S).data, pts = [];
      for (let y = 0; y < S; y += 2) for (let x = 0; x < S; x += 2) if (d[(y * S + x) * 4 + 3] > 140) pts.push([x / S - .5, y / S - .5]);
      for (let i = pts.length - 1; i > 0; i--) { const j = (Math.random() * (i + 1)) | 0; [pts[i], pts[j]] = [pts[j], pts[i]]; }
      const out = [];
      for (let i = 0; i < n; i++) out.push(pts[i % pts.length]);
      return out;
    }
    const icon = (path, fill, lw) => (o, S) => {
      o.save(); o.translate(S * .08, S * .08); o.scale(S * .84 / 24, S * .84 / 24);
      const p = new Path2D(path);
      o.lineWidth = lw; o.lineJoin = "round"; o.lineCap = "round";
      if (fill) o.fill(p, "evenodd"); else o.stroke(p);
      o.restore();
    };
    function buildShapes(n) {
      shapes.chat = sample((o, S) => {
        icon("M21 11.5a8.5 8.5 0 0 1-12.3 7.6L3.5 20.5l1.4-4.8A8.5 8.5 0 1 1 21 11.5Z", true)(o, S);
        o.globalCompositeOperation = "destination-out";
        [8, 12.2, 16.4].forEach((x) => { o.beginPath(); o.arc(S * (.08 + .84 * x / 24), S * (.08 + .84 * 11.5 / 24), S * .045, 0, 7); o.fill(); });
        o.globalCompositeOperation = "source-over";
      }, n);
      shapes.cap = sample(icon("M5 13.2v4L12 21l7-3.8v-4L12 17ZM12 3 1 9l11 6 9-4.9V17h2V9Z", true), n);
      shapes.house = sample(icon("M12 2.5 1.8 11.2h2.9V21.5h5.8v-6.2h3v6.2h5.8V11.2h2.9Z", true), n);
      shapes.building = sample((o, S) => {
        icon("M5 22V4.5L12 2l7 2.5V22Z", true)(o, S);
        o.globalCompositeOperation = "destination-out";
        icon("M8.5 7h2v2h-2ZM13.5 7h2v2h-2ZM8.5 11h2v2h-2ZM13.5 11h2v2h-2ZM8.5 15h2v2h-2ZM13.5 15h2v2h-2ZM10.5 19h3v3h-3Z", true)(o, S);
        o.globalCompositeOperation = "source-over";
      }, n);
      shapes.m7 = sample((o, S) => {
        o.font = "800 " + (S * .62) + "px Syne, 'Space Grotesk', sans-serif";
        o.textAlign = "center"; o.textBaseline = "middle";
        o.fillText("M7", S / 2, S * .53);
      }, n);
    }

    function layout() {
      const r = hero.getBoundingClientRect();
      DPR = Math.min(window.devicePixelRatio || 1, 2);
      W = r.width; H = r.height;
      cv.width = W * DPR; cv.height = H * DPR;
      ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
    }
    function geo() {
      if (LP) return mobile() ? { cx: W * .5, cy: 170, s: Math.min(W * .8, 320) } : { cx: W * .7, cy: H * .5, s: Math.min(H * 1.35, W * .72, 1100) };
      if (mobile()) return { cx: W * .5, cy: 190, s: Math.min(W * .78, 330) };
      return { cx: W * .73, cy: H * .5, s: Math.min(H * .78, W * .42, 620) };
    }
    function init() {
      layout();
      const n = LP ? (mobile() ? 900 : 1900) : (mobile() ? 1300 : 2600);
      buildShapes(n);
      parts = [];
      for (let i = 0; i < n; i++) parts.push({ x: Math.random() * W, y: Math.random() * H, vx: 0, vy: 0, t: i, j: Math.random() * Math.PI * 2, sz: Math.random() < .1 ? 2.6 : 1.7 });
    }
    function setStage(i) {
      stage = i;
      if (rotWord && STAGES[i]) { rotWord.textContent = STAGES[i].word; rotWord.classList.remove("swap"); void rotWord.offsetWidth; rotWord.classList.add("swap"); }
      dots.forEach((d, k) => d.classList.toggle("on", k === i));
    }
    let time = 0;
    function frame() {
      time += 1;
      const { cx, cy, s } = geo();
      const pts = shapes[SEQ[stage].shape];
      ctx.clearRect(0, 0, W, H);
      ctx.globalCompositeOperation = "lighter";
      for (const p of parts) {
        const tp = pts[p.t];
        const tx = cx + tp[0] * s + Math.cos(time * .02 + p.j) * 1.4;
        const ty = cy + tp[1] * s + Math.sin(time * .018 + p.j) * 1.4;
        p.vx += (tx - p.x) * .012; p.vy += (ty - p.y) * .012;
        const dx = p.x - mouse.x, dy = p.y - mouse.y, d2 = dx * dx + dy * dy;
        if (d2 < 12000) { const f = (12000 - d2) / 12000 * 2.4; const d = Math.sqrt(d2) || 1; p.vx += dx / d * f; p.vy += dy / d * f; }
        p.vx *= .86; p.vy *= .86;
        p.x += p.vx; p.y += p.vy;
        const k = Math.min(1, Math.max(0, (p.x - (cx - s * .5)) / s));
        const speed = Math.min(1, Math.hypot(p.vx, p.vy) / 6);
        const r = C1[0] + (C2[0] - C1[0]) * k, g = C1[1] + (C2[1] - C1[1]) * k, b = C1[2] + (C2[2] - C1[2]) * k;
        ctx.fillStyle = `rgba(${r | 0},${g | 0},${b | 0},${.78 + speed * .22})`;
        ctx.fillRect(p.x, p.y, p.sz, p.sz);
      }
      ctx.globalCompositeOperation = "source-over";
      if (!reduce) requestAnimationFrame(frame);
    }

    const start = () => {
      init();
      setStage(0);
      if (reduce) {
        const last = SEQ.length - 1; setStage(last);
        for (const p of parts) { const { cx, cy, s } = geo(); const tp = shapes[SEQ[last].shape][p.t]; p.x = cx + tp[0] * s; p.y = cy + tp[1] * s; }
        frame();
        return;
      }
      frame();
      if (SEQ.length > 1) setInterval(() => setStage((stage + 1) % SEQ.length), LP ? 4200 : 3600);
    };
    (document.fonts && document.fonts.ready ? document.fonts.ready : Promise.resolve()).then(start);

    let rt;
    window.addEventListener("resize", () => { clearTimeout(rt); rt = setTimeout(() => { const old = parts; layout(); if (reduce) start(); }, 150); });
    hero.addEventListener("pointermove", (e) => { const r = hero.getBoundingClientRect(); mouse.x = e.clientX - r.left; mouse.y = e.clientY - r.top; });
    hero.addEventListener("pointerleave", () => { mouse.x = mouse.y = -9999; });
  }

  /* ---------- CÉREBRO M7: pulsos viajando pelos fios ---------- */
  const svg = document.getElementById("brain");
  const feed = document.getElementById("feed");
  if (svg && feed) {
    const NS = "http://www.w3.org/2000/svg";
    const INS = ["WhatsApp", "Site", "E-mail", "Sensores"];
    const OUTS = ["CRM", "Agenda", "Orçamento", "Iluminação", "Clima", "Segurança"];
    const inY = [90, 183, 277, 370], outY = [55, 129, 203, 277, 351, 425];
    const CX = 500, CY = 230;
    const wiresIn = [], wiresOut = [];
    const gW = svg.querySelector("#wires"), gN = svg.querySelector("#nodes"), gP = svg.querySelector("#pulses");
    function wire(x1, y1, x2, y2) {
      const p = document.createElementNS(NS, "path");
      const mx = (x1 + x2) / 2;
      p.setAttribute("d", `M${x1} ${y1} C ${mx} ${y1}, ${mx} ${y2}, ${x2} ${y2}`);
      p.setAttribute("class", "wire"); gW.appendChild(p); return p;
    }
    function node(x, y, label, kind, cls) {
      const g = document.createElementNS(NS, "g"); g.setAttribute("class", "node " + cls);
      g.innerHTML = `<rect x="${x - 70}" y="${y - 24}" width="140" height="48" rx="14"/><text class="k" x="${x - 56}" y="${y - 5}">${kind}</text><text x="${x - 56}" y="${y + 13}">${label}</text>`;
      gN.appendChild(g); return g;
    }
    const inNodes = INS.map((l, i) => { wiresIn.push(wire(150, inY[i], CX - 62, CY)); return node(80, inY[i], l, "ENTRADA", "in"); });
    const outNodes = OUTS.map((l, i) => { wiresOut.push(wire(CX + 62, CY, 850, outY[i])); return node(920, outY[i], l, "AÇÃO", "out"); });

    const EVENTS = [
      [0, 2, "Cliente pediu orçamento no WhatsApp às 22h. Proposta enviada com os seus preços.", false],
      [0, 1, "Paciente remarcou a consulta sozinho e recebeu lembrete.", false],
      [1, 0, "Visitante do site qualificado e registrado no CRM com o histórico.", false],
      [2, 0, "E-mail de fornecedor lido e pedido lançado no sistema.", false],
      [2, 1, "Reunião confirmada e convite enviado para a equipe.", false],
      [3, 3, "Morador chegou: cena \"Chegar\" ativada na sala e na cozinha.", true],
      [3, 4, "Sala a 27 °C: ar-condicionado ajustado para 23 °C.", true],
      [3, 5, "Casa vazia há 10 min: alarme armado e câmeras ativas.", true],
      [0, 0, "Lead sem resposta há 2 dias: follow-up enviado pela IA.", false],
    ];
    let ei = 0;
    const clock = () => new Date().toLocaleTimeString("pt-BR", { hour: "2-digit", minute: "2-digit", second: "2-digit" });

    function travel(path, color, dur) {
      return new Promise((res) => {
        const c = document.createElementNS(NS, "circle");
        c.setAttribute("r", "5"); c.setAttribute("fill", color); c.setAttribute("class", "pulse"); c.style.color = color;
        gP.appendChild(c);
        const L = path.getTotalLength(); const t0 = performance.now();
        (function step(now) {
          const k = Math.min(1, (now - t0) / dur), e = k < .5 ? 2 * k * k : 1 - Math.pow(-2 * k + 2, 2) / 2;
          const pt = path.getPointAtLength(e * L); c.setAttribute("cx", pt.x); c.setAttribute("cy", pt.y);
          if (k < 1) requestAnimationFrame(step); else { c.remove(); res(); }
        })(t0);
      });
    }
    async function fire() {
      const [a, b, txt, home] = EVENTS[ei++ % EVENTS.length];
      inNodes[a].classList.add("hot");
      await travel(wiresIn[a], home ? "#9eb4d5" : "#ee4553", 900);
      inNodes[a].classList.remove("hot");
      await travel(wiresOut[b], home ? "#d6e3f5" : "#ff7884", 800);
      outNodes[b].classList.add("hot");
      setTimeout(() => outNodes[b].classList.remove("hot"), 900);
      const li = document.createElement("li");
      if (home) li.className = "home-ev";
      li.innerHTML = `<small>${clock()} · ${INS[a]} → ${OUTS[b]}</small><span></span>`;
      li.querySelector("span").textContent = txt;
      feed.prepend(li);
      while (feed.children.length > 5) feed.lastElementChild.remove();
    }
    // estado inicial já preenchido (página completa em repouso)
    for (let i = 0; i < 4; i++) {
      const [a, b, txt, home] = EVENTS[i + 5 > EVENTS.length - 1 ? i : i + 4];
      const li = document.createElement("li"); if (home) li.className = "home-ev";
      li.innerHTML = `<small>agora · ${INS[a]} → ${OUTS[b]}</small><span></span>`; li.querySelector("span").textContent = txt; feed.appendChild(li);
    }
    if (!reduce) { (async function loop() { await fire(); setTimeout(loop, 700); })(); }
  }

  /* ---------- Entrada suave das seções ---------- */
  if (!reduce && "IntersectionObserver" in window) {
    const io = new IntersectionObserver((es) => es.forEach((e) => { if (e.isIntersecting) { e.target.classList.add("anim"); io.unobserve(e.target); } }), { rootMargin: "0px 0px -10% 0px" });
    document.querySelectorAll(".reveal").forEach((el) => { if (el.getBoundingClientRect().top > innerHeight) io.observe(el); });
  }
})();
