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
        parsed = urlparse(self.path)
        path = parsed.path
        query = parse_qs(parsed.query)
        params = self.get_query_params()

        name = params.get("name", [None])[0]
        max_price = params.get("max_price", [None])[0]

        
        products = [
            {"name":"iphone","price":2000},
            {"name":"samsung","price":1500},
            {"name":"oppo phone","price":700},
            {"name":"realme phone","price":500}
        ]
        
        prod = [u for u in products if name.lower() in u["name"].lower()]
        prod_1=[p for p in prod if prod["price"]<=max_price]
        self.send_json(200, {
            "data": prod_1
        })

def run():
    server = HTTPServer((HOST, PORT), SimpleAPI)
    print(f"Server running on http://{HOST}:{PORT}")
    server.serve_forever()


if __name__ == "__main__":
    run()