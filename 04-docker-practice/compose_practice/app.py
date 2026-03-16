from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps({"status": "healthy"}).encode())
        elif self.path == "/api/hello":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps({"status": "Hello from API!"}).encode())
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        pass

print("API is running on port 8000")
HTTPServer(("", 8000), Handler).serve_forever()