from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import json

HOST = "localhost"
PORT = 8000

class SimpleAPI(BaseHTTPRequestHandler):

    def send_json(self, status, data):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_POST(self):
        if self.path != "/shutdown":
            self.send_json(404, {"message": "Not Found"})
            return

        if self.client_address[0] != "127.0.0.1":
            self.send_json(403, {"message": "Forbidden"})
            return

        self.send_json(200, {"message": "Shutting down"})
        threading.Thread(target=self.server.shutdown).start()


def run():
    server = HTTPServer((HOST, PORT), SimpleAPI)
    print(f"Server running on http://{HOST}:{PORT}")
    server.serve_forever()

if __name__ == "__main__":
    run()
