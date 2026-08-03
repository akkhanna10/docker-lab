import http.server
import socketserver
import socket
import os

PORT = 80
GREETING = os.environ.get("GREETING", "default greeting - no env var set")

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/healthz":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"ok\n")
            return

       # if self.path == "/eatmemory":
           # hog = bytearray(200 * 1024 * 1024)  # allocate 200MB
            #self.send_response(200)
            #self.send_header("Content-type", "text/plain")
            #self.end_headers()
            #self.wfile.write(b"allocated\n")
            #return

        hostname = socket.gethostname()
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        message = f"Hello from pod: {hostname}\nGreeting: {GREETING}\n"
        self.wfile.write(message.encode())

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
