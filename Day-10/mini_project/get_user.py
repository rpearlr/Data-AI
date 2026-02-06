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
        params = self.get_query_params()
        print(params)
        id = params.get("id", [None])[0]
        print(id)
        users = [
            {"name":"jane","id":1},
            {"name":"john","id":2},
            {"name":"tom","id":3},
            {"name":"mary","id":4}
        ]
        user = [u for u in users if int(id)==u["id"]]
        if user :
            self.send_json(200, {
                "data": user
            })
        elif not user :
             self.send_json(404, {
                "Message" : "User is not found"
            })
        else :
            self.send_json(400, {
                "Message" : "ID is not valid"
            })
            

def run():
    server = HTTPServer((HOST, PORT), SimpleAPI)
    print(f"Server running on http://{HOST}:{PORT}")
    server.serve_forever()


if __name__ == "__main__":
    run()