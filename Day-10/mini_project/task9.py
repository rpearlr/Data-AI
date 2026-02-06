from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import json

HOST = "localhost"
PORT = 8000

requests = {}

class SimpleAPI(BaseHTTPRequestHandler):

    def send_json(self, status, data):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_GET(self):
        ip = self.client_address[0]
        now = time.time()

        if ip not in requests:
            requests[ip] = []

        requests[ip] = [t for t in requests[ip] if now - t < 60]

        if len(requests[ip]) >= 5:
            self.send_json(429, {"message": "Too Many Requests"})
            return

        requests[ip].append(now)
        self.send_json(200, {"status": "ok"})


def run():
    server = HTTPServer((HOST, PORT), SimpleAPI)
    print(f"Server running on http://{HOST}:{PORT}")
    server.serve_forever()

if __name__ == "__main__":
    run()
