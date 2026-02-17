#!/usr/bin/python3
'''
Docstring for restful-api.task_03_http_server
'''

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

PORT = 8000


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            datas = json.dumps(data)
            self.wfile.write(datas.encode())

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"ok")

        else:
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()


server = HTTPServer(("", PORT), Handler)
print(f"Serveur lancé sur http://localhost:{PORT}")
server.serve_forever()
