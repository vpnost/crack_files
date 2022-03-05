import urllib2

down_url = "https://raw.githubusercontent.com/vpnost/crack_files/master/pyovpn-2.0-py3.6.egg"
filedata = urllib2.urlopen(down_url)
f = open("/usr/local/openvpn_as/lib/python/pyovpn-2.0-py3.6.egg", "wb")
f.write(filedata.read())
f.close()
