import http.server
import socketserver
import socket

PORT = 80

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        hostname = socket.gethostname()
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        message = f"Hello from pod: {hostname}\n"
        self.wfile.write(message.encode())
        print(f"Handled request, served by {hostname}")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
