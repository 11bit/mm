from http.server import BaseHTTPRequestHandler
from datetime import datetime
import shutil
from types import SimpleNamespace


FILEPATH = 'api/input.ttf'

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    with open(FILEPATH, 'rb') as f:
      self.send_response(200)
      self.send_header("Content-Type", 'application/octet-stream')
      self.send_header("Content-Disposition", 'attachment; filename="{}"'.format("output.ttf"))
      self.send_header("Content-Length", str(fs.st_size))
      self.end_headers()
      shutil.copyfileobj(f, self.wfile)
      # self.wfile.write(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')).encode())
    return