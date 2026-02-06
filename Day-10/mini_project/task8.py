from http.server import BaseHTTPRequestHandler, HTTPServer
import json

HOST = "localhost"
PORT = 8000
API_KEY = "mykey123"

class SimpleAPI(BaseHTTPRequestHandler):

    def send_json(self, status, data):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_GET(self):
        if self.path != "/secret":
            self.send_json(404, {"message": "Not Found"})
            return

        key = self.headers.get("X-API-Key")

        if key != API_KEY:
            self.send_json(401, {"message": "Unauthorized"})
            return

        self.send_json(200, {"secret": "you are authenticated"})


def run():
    server = HTTPServer((HOST, PORT), SimpleAPI)
    print(f"Server running on http://{HOST}:{PORT}")
    server.serve_forever()

if __name__ == "__main__":
    run()
