import http.server
import socketserver
import socket
import os

PORT = 80
GREETING = os.environ.get("GREETING", "default greeting - no env var set")

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        hostname = socket.gethostname()
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        message = f"Hello from pod: {hostname}\nGreeting: {GREETING}\n"
        self.wfile.write(message.encode())

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
