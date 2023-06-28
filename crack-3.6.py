import urllib.request
import shutil
import os

#os.system("apt-get install --only-upgrade -y openvpn-as")

down_url = "https://raw.githubusercontent.com/vpnost/crack_files/master/pyovpn-2.0-py3.6.egg"

with urllib.request.urlopen(down_url) as response, open("/usr/local/openvpn_as/lib/python/pyovpn-2.0-py3.6.egg", 'wb') as out_file:
    shutil.copyfileobj(response, out_file)
