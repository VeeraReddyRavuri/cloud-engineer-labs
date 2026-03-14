from http.server import HTTPServer, BaseHTTPRequestHandler
import requests
import sys

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello from multi-stage Docker!")
    def log_message(self, format, *args):
        pass
    
print(f"Python version: {sys.version}")
print("Server running on port 8000")
HTTPServer(("", 8000), Handler).serve_forever()