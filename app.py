from http.server import SimpleHTTPRequestHandler, HTTPServer

HOST = "0.0.0.0"
PORT = 8080

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"App is running on port 8080\n")

if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), Handler)
    print(f"Starting server on {HOST}:{PORT}")
    server.serve_forever()
