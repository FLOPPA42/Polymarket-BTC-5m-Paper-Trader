#!/usr/bin/env python3
"""
Polymarket Paper Trading - Local Proxy Server
Serves the HTML frontend and proxies API calls to Polymarket.
"""
import http.server
import socketserver
import urllib.request
import urllib.error
import json
import ssl
import os
import sys

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

# Allow reuse of the port immediately
class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

class ProxyHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def log_message(self, format, *args):
        # Clean log
        print(f"[SERVER] {args[0]}")

    def do_GET(self):
        # Static files
        if not self.path.startswith('/api/'):
            return super().do_GET()

        # Proxy API calls
        if self.path.startswith('/api/gamma/'):
            remote = "https://gamma-api.polymarket.com/" + self.path[11:]
        elif self.path.startswith('/api/clob/'):
            remote = "https://clob.polymarket.com/" + self.path[10:]
        else:
            self.send_error(404)
            return

        try:
            ctx = ssl.create_default_context()
            req = urllib.request.Request(remote, headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)',
                'Accept': 'application/json',
            })
            with urllib.request.urlopen(req, timeout=10, context=ctx) as resp:
                body = resp.read()
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.send_header('Cache-Control', 'no-cache')
                self.end_headers()
                self.wfile.write(body)
        except urllib.error.HTTPError as e:
            print(f"[PROXY ERROR] {e.code} for {remote}")
            self.send_response(e.code)
            self.end_headers()
        except Exception as e:
            print(f"[PROXY ERROR] {e} for {remote}")
            self.send_response(502)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode())

if __name__ == "__main__":
    print(f"""
╔══════════════════════════════════════════════════╗
║  Polymarket BTC 5m Paper Trader - Servidor Local ║
╠══════════════════════════════════════════════════╣
║  Abre en tu navegador:                           ║
║  👉  http://localhost:{PORT}                      ║
║                                                  ║
║  Presiona Ctrl+C para detener el servidor.       ║
╚══════════════════════════════════════════════════╝
""")
    with ReusableTCPServer(("", PORT), ProxyHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n[SERVER] Servidor detenido.")
            sys.exit(0)
