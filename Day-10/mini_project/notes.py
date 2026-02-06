# search products using queryparams

# GET /product?name=phone&max_price=500
# name=partial match
# max_price=optional
# return empty if nothing found

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse, parse_qs
HOST = "localhost"
PORT = 8000
note = []
class SimpleAPI(BaseHTTPRequestHandler):
    def get_query_params(self):
        parsed_url = urlparse(self.path)
        return parse_qs(parsed_url.query)
    def send_json(self, status=200, data=None):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        if data is not None:
            self.wfile.write(json.dumps(data).encode())
    def do_GET(self) :
        if len(note)>0 :
            self.send_json(200, {
                "data": note
            })
        else :
            self.send_json(400, {
                "Message" : "No notes availible"
            })
    def do_POST(self) :
        length = int(self.headers.get("Content-Length", 0))
        if length == 0:
            return {}
        body = self.rfile.read(length)
        data= json.loads(body)
        note.append(data)
        self.send_json(201, note)
            

def run():
    server = HTTPServer((HOST, PORT), SimpleAPI)
    print(f"Server running on http://{HOST}:{PORT}")
    server.serve_forever()


if __name__ == "__main__":
    run()