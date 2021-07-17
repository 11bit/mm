from http.server import BaseHTTPRequestHandler
import shutil
from opentype_feature_freezer import RemapByOTL
from types import SimpleNamespace
import os
import sys
from urllib.parse import urlparse, parse_qs

def convert(output, features):
  args = {
      'features': features,
      'usesuffix': 'SC',
      "replacenames": "TestCustomizer-Regular/TestCustomizer-Regular-Subset",
      "inpath": "api/TestCustomizer-Regular.otf",
      "outpath": output,
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

AVAILABLE_FEATURES = ['liga', 'zero']
VALUES = ["0", "1"]

class handler(BaseHTTPRequestHandler):
  def do_GET(self):
    query = urlparse(self.path).query
    params = parse_qs(query)

#
    features = ",".join([
      '{}'.format(name)
      for name, val in params.items()
      if name in AVAILABLE_FEATURES and val[0] == "1"
    ])
    print(features)

    self.send_response(200)
    self.send_header("Content-Type", 'application/octet-stream')
    self.send_header("Content-Disposition", 'attachment; filename="{}-{}.otf"'.format("TestCustomizer-Regular", 'features'))
    # self.send_header("Content-Length", str(fs.st_size))
      # self.wfile.write(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')).encode())
    self.end_headers()

    convert(self.wfile, features)


# import http.server
# import socketserver

# PORT = 8000
# with socketserver.TCPServer(("", PORT), handler) as httpd:
#     print("serving at port", PORT)
#     httpd.serve_forever()