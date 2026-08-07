#!/usr/bin/env python3
import http.server, os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class H(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/save-mind":
            n = int(self.headers.get("Content-Length", 0))
            data = self.rfile.read(n)
            with open("targets.mind", "wb") as f:
                f.write(data)
            print(f"[saved] targets.mind {len(data)} bytes", flush=True)
            self.send_response(200); self.end_headers(); self.wfile.write(b"ok")
        else:
            self.send_response(404); self.end_headers()
    def do_GET(self):
        if self.path.startswith("/log"):
            print("[page]", self.path[7:], flush=True)
            self.send_response(200); self.end_headers(); self.wfile.write(b"ok")
            return
        super().do_GET()
    def log_message(self, *a): pass

http.server.ThreadingHTTPServer(("127.0.0.1", 8788), H).serve_forever()
