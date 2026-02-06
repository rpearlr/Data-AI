from http.server import BaseHTTPRequestHandler, HTTPServer
import json

HOST = "localhost"
PORT = 8000

notes = [
    {"id": 1, "text": "hello"}
]

class SimpleAPI(BaseHTTPRequestHandler):

    def send_json(self, status=200, data=None):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        if data:
            self.wfile.write(json.dumps(data).encode())

    def do_PUT(self):
        if not self.path.startswith("/notes/"):
            self.send_json(404, {"message": "Not Found"})
            return

        try:
            note_id = int(self.path.split("/")[-1])
        except:
            self.send_json(400, {"message": "Invalid ID"})
            return

        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length)

        try:
            data = json.loads(body)
            text = data.get("text")
        except:
            self.send_json(400, {"message": "Invalid JSON"})
            return

        for note in notes:
            if note["id"] == note_id:
                note["text"] = text
                self.send_json(200, note)
                return

        self.send_json(404, {"message": "Note not found"})


def run():
    server = HTTPServer((HOST, PORT), SimpleAPI)
    print(f"Server running on http://{HOST}:{PORT}")
    server.serve_forever()

if __name__ == "__main__":
    run()
