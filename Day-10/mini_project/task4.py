from http.server import BaseHTTPRequestHandler, HTTPServer
import json

HOST = "localhost"
PORT = 8000

notes = [
    {"id": 1, "text": "hello"},
    {"id": 2, "text": "world"}
]

class SimpleAPI(BaseHTTPRequestHandler):

    def send_json(self, status=200, data=None):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        if data:
            self.wfile.write(json.dumps(data).encode())

    def do_GET(self):
        if not self.path.startswith("/notes/"):
            self.send_json(404, {"message": "Not Found"})
            return

        try:
            note_id = int(self.path.split("/")[-1])
        except:
            self.send_json(400, {"message": "Invalid ID"})
            return

        note = [n for n in notes if n["id"] == note_id]

        if note:
            self.send_json(200, note[0])
        else:
            self.send_json(404, {"message": "Note not found"})


def run():
    server = HTTPServer((HOST, PORT), SimpleAPI)
    print(f"Server running on http://{HOST}:{PORT}")
    server.serve_forever()

if __name__ == "__main__":
    run()
