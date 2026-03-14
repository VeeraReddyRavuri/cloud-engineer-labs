from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello from inside Docker!")
    
print("Server running on port 8000")
HTTPServer(("", 8000), Handler).serve_forever()