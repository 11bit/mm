from http.server import BaseHTTPRequestHandler
from datetime import datetime
import shutil
from opentype_feature_freezer import RemapByOTL
from types import SimpleNamespace

def convert():
  args = {
      'features': 'salt',
      'usesuffix': 'SC',
      "replacenames": "Charis SIL/Charix,CharisSIL/Charix",
      "inpath": "input.ttf",
      "outpath": "output.ttf",
      'script': None,
      'lang': None,
      'report': None,
      'names': None,
      'suffix': None,
      'info': None,
      'zapnames': None,
  }

  p = RemapByOTL(SimpleNamespace(**args))
  p.run()


FILEPATH = 'output.ttf'

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    convert()
    with open(FILEPATH, 'rb') as f:
      self.send_response(200)
      self.send_header("Content-Type", 'application/octet-stream')
      self.send_header("Content-Disposition", 'attachment; filename="{}"'.format("output.ttf"))
      self.send_header("Content-Length", str(fs.st_size))
      self.end_headers()
      shutil.copyfileobj(f, self.wfile)
      # self.wfile.write(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')).encode())
    return