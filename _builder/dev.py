#!/usr/bin/env python3
"""Local dev server for the design site: rebuild on change, reload the browser.

Usage:  python _builder/dev.py [--port 8765] [--host 127.0.0.1]

- Builds the site once, then serves the repository folder at http://127.0.0.1:8765/
- Watches _builder/ (pages, static css/js, build scripts, and new images in images/originals). When a file changes it
  re-runs build.py, so the site you see is exactly what gets committed and deployed.
- Every open page reloads itself after a successful build. If a build fails, the
  error is printed here and shown in a banner on the page; fix it and save again.
"""
import argparse
import http.server
import json
import os
import subprocess
import sys
import threading
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
WATCH_SUFFIXES = {".py", ".css", ".js", ".html", ".svg", ".json", ".png", ".jpg", ".jpeg", ".webp"}
POLL_SECONDS = 0.4

state = {"version": 0, "error": ""}
lock = threading.Lock()

RELOAD_SNIPPET = b"""
<script>
/* dev.py live reload: not part of the published site */
(function () {
  let seen = null, banner = null;
  async function check() {
    try {
      const s = await (await fetch("/__dev_state", { cache: "no-store" })).json();
      if (seen === null) seen = s.version;
      if (s.version !== seen) { location.reload(); return; }
      if (s.error && !banner) {
        banner = document.createElement("pre");
        banner.textContent = "Build failed (see the dev.py terminal):\\n\\n" + s.error;
        banner.style.cssText = "position:fixed;inset:auto 0 0 0;max-height:45vh;overflow:auto;margin:0;padding:14px 18px;" +
          "background:#3a0d0d;color:#ffd9d0;font:13px/1.45 ui-monospace,Consolas,monospace;z-index:99999;white-space:pre-wrap";
        document.body.appendChild(banner);
      } else if (!s.error && banner) { banner.remove(); banner = null; }
    } catch (e) { /* server restarting */ }
    setTimeout(check, 600);
  }
  check();
})();
</script>
"""


def snapshot():
    files = {}
    for p in HERE.rglob("*"):
        if p.is_file() and p.suffix in WATCH_SUFFIXES and "__pycache__" not in p.parts and p.name != "dev.py":
            try:
                files[p] = p.stat().st_mtime_ns
            except OSError:
                pass
    return files


def build():
    started = time.time()
    env = {**os.environ, "PYTHON_COLORS": "0", "NO_COLOR": "1"}  # plain tracebacks for the page banner
    proc = subprocess.run([sys.executable, str(HERE / "build.py")], cwd=ROOT, capture_output=True, text=True, env=env)
    took = time.time() - started
    with lock:
        if proc.returncode == 0:
            state["version"] += 1
            state["error"] = ""
            print(f"[dev] built in {took:.1f}s  ->  reloading pages", flush=True)
        else:
            state["error"] = (proc.stderr or proc.stdout).strip()[-4000:]
            print(f"[dev] BUILD FAILED\n{state['error']}\n", flush=True)


def watch():
    last = snapshot()
    while True:
        time.sleep(POLL_SECONDS)
        now = snapshot()
        if now != last:
            changed = sorted({p.relative_to(ROOT).as_posix() for p in set(now) ^ set(last)} |
                             {p.relative_to(ROOT).as_posix() for p in now if p in last and now[p] != last[p]})
            print(f"[dev] changed: {', '.join(changed[:5])}{' …' if len(changed) > 5 else ''}", flush=True)
            time.sleep(0.15)  # let editors finish writing
            last = snapshot()
            build()


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def log_message(self, fmt, *args):
        pass  # keep the terminal for build output

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def do_GET(self):
        if self.path.startswith("/__dev_state"):
            with lock:
                body = json.dumps(state).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        path = Path(self.translate_path(self.path))
        if path.is_dir():
            path = path / "index.html"
        if path.suffix == ".html" and path.is_file():
            html = path.read_bytes()
            html = html.replace(b"</body>", RELOAD_SNIPPET + b"</body>", 1)
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(html)))
            self.end_headers()
            self.wfile.write(html)
            return
        super().do_GET()


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--port", type=int, default=8765)
    ap.add_argument("--host", default="127.0.0.1")
    args = ap.parse_args()

    build()
    threading.Thread(target=watch, daemon=True).start()
    server = http.server.ThreadingHTTPServer((args.host, args.port), Handler)
    print(f"[dev] serving http://{args.host}:{args.port}/  (watching _builder/, Ctrl+C to stop)", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[dev] stopped")


if __name__ == "__main__":
    main()
