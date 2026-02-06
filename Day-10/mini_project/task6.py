from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = "localhost"
PORT = 8000

notes = [{"id": 1, "text": "hello"}]

class SimpleAPI(BaseHTTPRequestHandler):

    def do_DELETE(self):
        if not self.path.startswith("/notes/"):
            self.send_response(404)
            self.end_headers()
            return

        try:
            note_id = int(self.path.split("/")[-1])
        except:
            self.send_response(400)
            self.end_headers()
            return

        for note in notes:
            if note["id"] == note_id:
                notes.remove(note)
                self.send_response(204)
                self.end_headers()
                return

        self.send_response(404)
        self.end_headers()


def run():
    server = HTTPServer((HOST, PORT), SimpleAPI)
    print(f"Server running on http://{HOST}:{PORT}")
    server.serve_forever()

if __name__ == "__main__":
    run()
