import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

from labapp import __version__


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = json.dumps({
            "app": "labapp",
            "version": __version__,
            "env": os.environ.get("ENV_NAME"),
            "db_host": os.environ.get("DB_HOST"),
            "greeting": os.environ.get("APP_GREETING"),
        }, indent=2).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(body)


def main():
    HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
