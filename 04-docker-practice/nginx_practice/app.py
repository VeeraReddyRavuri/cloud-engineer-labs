from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/api"):
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            response = {
                "message": "Hello from FastAPI!",
                "path": self.path,
                "forwarded_for": self.headers.get("X-Forwarded-For", "not set"),
                "real_ip": self.headers.get("X-Real-IP", "not set")
            }
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        pass

print("API running on port 8000")
HTTPServer(("", 8000), Handler).serve_forever()