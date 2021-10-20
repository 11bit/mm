from plumbum import local
from lxml import etree
import os
import tempfile
import shutil
from fontTools.ttLib import TTFont

cmd_ttx = local['ttx']
cmd_rm = local['rm']

def swap_symbol(src, dst, replacements):
    with open(src, encoding="utf-8") as f:
        fnt = etree.parse(f)

        for name_from, name_to in replacements:
            symbol_from = fnt.xpath("//CharString[@name='{}']".format(name_from))
            symbol_to = fnt.xpath("//CharString[@name='{}']".format(name_to))

            symbol_from[0].text = symbol_to[0].text

        with open(dst, 'wb') as res:
            fnt.write(res, xml_declaration=True, encoding='utf-8')

def to_binary(ttx_file):
    cmd_ttx(ttx_file)
    cmd_rm(ttx_file)

def makeFonts(dir, result_file):
    with tempfile.TemporaryDirectory() as dest_dir:
        for root, dirs, files in os.walk(dir):
            for file in files:
                if file.endswith('.ttx'):
                    source = os.path.join(root, file)
                    dest = os.path.join(dest_dir, file)

                    print(source, dest)

                    swap_symbol(source, dest, [['percent', 'percent.cv02']])
                    to_binary(dest)

        print("TMP DEST:", dest_dir)
        shutil.make_archive(result_file, 'zip', dest_dir)

class handler(BaseHTTPRequestHandler):
  def do_GET(self):
    makeFonts('api/fonts/otf', 'public/result')
    self.send_response(200)
    self.end_headers()

#makeFonts('./fonts/otf', './res/result')
