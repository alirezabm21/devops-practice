from http.server import BaseHTTPRequesHandler , HTTPServer
class Handler(BaseHTTPRequestHandler):
def do_GET(self):
  self.send_response(200)
  self.send_header("content-type","tet/html")
  self.end_headers()
  self.wfile.write(
  b"<h1>Hello from Docker!</h1>"
  b"<p>DovOps practice project</p>")
  server = HTTPServer(("0.0.0.0", 80000),Handler)
  print("Server running on port 8000")
  server.server_forever()
