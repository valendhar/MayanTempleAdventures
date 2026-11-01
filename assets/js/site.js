/* Navigation (disclosure pattern), mobile menu, lightbox */
(function () {
  const desktop = window.matchMedia("(min-width: 1081px)");
  const nav = document.getElementById("main-nav");
  const menuBtn = document.querySelector(".menu-toggle");

  function setOpen(btn, open) {
    const sub = document.getElementById(btn.getAttribute("aria-controls"));
    btn.setAttribute("aria-expanded", open ? "true" : "false");
    if (sub) sub.classList.toggle("open", open);
    if (!open && sub) sub.querySelectorAll(".sub-toggle").forEach(b => setOpen(b, false));
  }

  function closeSiblings(btn) {
    const li = btn.closest(".nav-item");
    const list = li.parentElement;
    list.querySelectorAll(":scope > .nav-item > .nav-row > .sub-toggle").forEach(b => {
      if (b !== btn) setOpen(b, false);
    });
  }

  function closeAll() {
    document.querySelectorAll(".sub-toggle").forEach(b => setOpen(b, false));
  }

  document.querySelectorAll(".sub-toggle").forEach(btn => {
    btn.addEventListener("click", e => {
      e.stopPropagation();
      const open = btn.getAttribute("aria-expanded") !== "true";
      closeSiblings(btn);
      setOpen(btn, open);
    });
  });

  // On mobile, start with the branch that contains the current page opened
  function openCurrentBranch() {
    if (desktop.matches) return;
    document.querySelectorAll(".nav-item.has-sub.is-active > .nav-row > .sub-toggle").forEach(b => setOpen(b, true));
  }

  document.addEventListener("click", e => {
    if (desktop.matches && !e.target.closest(".main-nav")) closeAll();
  });

  document.addEventListener("keydown", e => {
    if (e.key !== "Escape") return;
    const openBtn = [...document.querySelectorAll('.sub-toggle[aria-expanded="true"]')].pop();
    if (openBtn) { setOpen(openBtn, false); openBtn.focus(); return; }
    if (menuBtn && menuBtn.getAttribute("aria-expanded") === "true") { toggleMenu(false); menuBtn.focus(); }
  });

  nav && nav.addEventListener("focusout", e => {
    if (desktop.matches && !nav.contains(e.relatedTarget)) closeAll();
  });

  function toggleMenu(open) {
    menuBtn.setAttribute("aria-expanded", open ? "true" : "false");
    nav.classList.toggle("open", open);
    document.body.classList.toggle("menu-open", open);
    if (open) openCurrentBranch(); else closeAll();
  }
  menuBtn && menuBtn.addEventListener("click", () => toggleMenu(menuBtn.getAttribute("aria-expanded") !== "true"));
  desktop.addEventListener("change", () => { closeAll(); if (menuBtn) toggleMenu(false); });

  // ---------------- home: the climb lights up from Floor 0 to the summit, once
  const ascent = document.querySelector(".ascent");
  const calm = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (ascent && "IntersectionObserver" in window && !calm) {
    ascent.classList.add("will-rise");
    const io = new IntersectionObserver(entries => {
      if (entries.some(e => e.isIntersecting)) { ascent.classList.add("is-lit"); io.disconnect(); }
    }, { threshold: 0.25 });
    io.observe(ascent);
  }

  // ---------------- lightbox
  const lb = document.querySelector(".lightbox");
  if (!lb) return;
  const lbImg = lb.querySelector("img");
  const lbCap = lb.querySelector("figcaption");
  let links = [], idx = 0, lastFocus = null;

  function show(i) {
    idx = (i + links.length) % links.length;
    const a = links[idx];
    lbImg.src = a.href;
    lbImg.alt = (a.querySelector("img") || {}).alt || "";
    lbCap.textContent = a.dataset.caption || "";
    const multi = links.length > 1;
    lb.querySelector(".lb-prev").hidden = !multi;
    lb.querySelector(".lb-next").hidden = !multi;
  }
  function open(a) {
    const scope = a.closest(".gallery, section, main") || document;
    links = [...scope.querySelectorAll("a.lb")];
    lastFocus = a;
    show(links.indexOf(a));
    lb.hidden = false;
    document.body.style.overflow = "hidden";
    lb.querySelector(".lb-close").focus();
  }
  function close() {
    lb.hidden = true;
    lbImg.src = "";
    document.body.style.overflow = "";
    if (lastFocus) lastFocus.focus();
  }
  document.addEventListener("click", e => {
    const a = e.target.closest("a.lb");
    if (a) { e.preventDefault(); open(a); }
  });
  lb.querySelector(".lb-close").addEventListener("click", close);
  lb.querySelector(".lb-prev").addEventListener("click", () => show(idx - 1));
  lb.querySelector(".lb-next").addEventListener("click", () => show(idx + 1));
  lb.addEventListener("click", e => { if (e.target === lb) close(); });
  document.addEventListener("keydown", e => {
    if (lb.hidden) return;
    if (e.key === "Escape") close();
    if (e.key === "ArrowLeft") show(idx - 1);
    if (e.key === "ArrowRight") show(idx + 1);
  });
})();
