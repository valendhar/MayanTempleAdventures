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

  // ---------------- story reader: progress bar, text size, paper/night (remembered in this browser)
  const reader = document.querySelector("[data-reader]");
  if (reader) {
    const store = {
      get(k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
      set(k, v) { try { localStorage.setItem(k, v); } catch (e) { /* storage blocked: settings just aren't kept */ } }
    };
    const sizes = [1.06, 1.14, 1.24, 1.36, 1.5];
    let size = parseInt(store.get("reader-size"), 10);
    if (isNaN(size) || size < 0 || size >= sizes.length) size = 2;
    const themeBtn = reader.querySelector("[data-theme-toggle]");
    const applySize = () => reader.style.setProperty("--size", sizes[size] + "rem");
    const applyTheme = night => {
      reader.dataset.theme = night ? "night" : "paper";
      if (themeBtn) {
        themeBtn.setAttribute("aria-pressed", night ? "true" : "false");
        themeBtn.textContent = night ? (document.documentElement.lang === "de" ? "Papier" : "Paper")
                                     : (document.documentElement.lang === "de" ? "Nacht" : "Night");
      }
    };
    if (store.get("reader-size") !== null) applySize();
    applyTheme(store.get("reader-theme") === "night");
    reader.querySelectorAll("[data-size]").forEach(b => b.addEventListener("click", () => {
      size = Math.min(sizes.length - 1, Math.max(0, size + parseInt(b.dataset.size, 10)));
      applySize(); store.set("reader-size", String(size));
    }));
    themeBtn && themeBtn.addEventListener("click", () => {
      const night = reader.dataset.theme !== "night";
      applyTheme(night); store.set("reader-theme", night ? "night" : "paper");
    });
    const bar = document.querySelector(".reader-progress span");
    const text = reader.querySelector(".reader-text");
    const onScroll = () => {
      if (!bar || !text) return;
      const r = text.getBoundingClientRect();
      const done = Math.min(1, Math.max(0, (innerHeight * 0.6 - r.top) / r.height));
      bar.style.width = (done * 100).toFixed(1) + "%";
    };
    addEventListener("scroll", onScroll, { passive: true });
    addEventListener("resize", onScroll);
    onScroll();
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
