#!/usr/bin/python3
import http.server
import socketserver
import json

PORT = 8000

handler=http.server.SimpleHTTPRequestHandler
class MyHandler(handler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type","text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(200)
            data = {"name": "John","age": 30,"city": "New York"}

            self.send_header("Content-type","application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())


        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type","text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_response(404)
            self.send_header("Content-type","text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

with socketserver.TCPServer(("",PORT),MyHandler) as httpd:
    print("server caavabi",PORT)    
    httpd.serve_forever()      
