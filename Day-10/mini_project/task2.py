from http.server import BaseHTTPRequestHandler, HTTPServer
import json

HOST = "localhost"
PORT = 8000

notes = []

class SimpleAPI(BaseHTTPRequestHandler):

    def send_json(self, status=200, data=None):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        if data:
            self.wfile.write(json.dumps(data).encode())

    def do_POST(self):
        if self.path != "/notes":
            self.send_json(404, {"message": "Not Found"})
            return

        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length)

        try:
            data = json.loads(body)
            text = data.get("text")
        except:
            self.send_json(400, {"message": "Invalid JSON"})
            return

        if not text:
            self.send_json(400, {"message": "Text missing"})
            return

        note = {"id": len(notes) + 1, "text": text}
        notes.append(note)

        self.send_json(201, note)


def run():
    server = HTTPServer((HOST, PORT), SimpleAPI)
    print(f"Server running on http://{HOST}:{PORT}")
    server.serve_forever()

if __name__ == "__main__":
    run()
