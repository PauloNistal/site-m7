// IA no Colégio: contadores, chat do hero e lousa animada.
(() => {
  const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const onView = (el, fn, th = 0.35) => {
    if (!("IntersectionObserver" in window)) return fn();
    const io = new IntersectionObserver((es) => es.forEach((e) => { if (e.isIntersecting) { io.disconnect(); fn(); } }), { threshold: th });
    io.observe(el);
  };

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

  // lousa: escreve "É proibido usar IA", apaga e desenha a rede de IA, em loop enquanto está na tela
  document.querySelectorAll("[data-lousa]").forEach((box) => {
    if (reduce) return;
    let timer = null, visible = false;
    const cycle = () => {
      box.classList.remove("play", "out"); void box.offsetWidth; box.classList.add("play");
      timer = setTimeout(() => { box.classList.add("out"); timer = setTimeout(() => (visible ? cycle() : (timer = null)), 700); }, 12500);
    };
    const io = new IntersectionObserver((es) => es.forEach((e) => { visible = e.isIntersecting; if (visible && !timer) cycle(); }), { threshold: 0.35 });
    io.observe(box);
  });
})();
