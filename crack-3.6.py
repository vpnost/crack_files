import urllib.request
import shutil

down_url = "https://raw.githubusercontent.com/vpnost/crack_files/master/pyovpn-2.0-py3.6.egg"
file_name = "/usr/local/openvpn_as/lib/python/pyovpn-2.0-py3.6.egg"

with urllib.request.urlopen(down_url) as response, open(file_name, 'wb') as out_file:
    shutil.copyfileobj(response, out_file)
