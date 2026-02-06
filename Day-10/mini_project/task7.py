from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import json

HOST = "localhost"
PORT = 8000

notes = [
    {"id": 1, "text": "Hello World"},
    {"id": 2, "text": "Python server"}
]

class SimpleAPI(BaseHTTPRequestHandler):

    def send_json(self, status=200, data=None):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_GET(self):
        parsed = urlparse(self.path)
        params = parse_qs(parsed.query)
        search = params.get("search", [""])[0].lower()

        if parsed.path == "/notes":
            result = [n for n in notes if search in n["text"].lower()]
            self.send_json(200, result)
        else:
            self.send_json(404, {"message": "Not Found"})


def run():
    server = HTTPServer((HOST, PORT), SimpleAPI)
    print(f"Server running on http://{HOST}:{PORT}")
    server.serve_forever()

if __name__ == "__main__":
    run()
