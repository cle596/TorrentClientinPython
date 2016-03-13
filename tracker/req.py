import requests
from bencode import *
import pprint 
import codecs
import binascii
import unicodedata
import base64
import urllib
import struct
import socket

tracker = "http://tracker.flashtorrents.org:6969/announce"+\
          "?info_hash=_%0E%9B%F4%DAX%9F%AE%8F%BE%DEh%2Ah16ff%D0%8E"+\
          "&peer_id=12345678901234567890"+\
          "&uploaded=0"+\
          "&event=started"+\
          "&compact=1"

r = requests.get(tracker)
print r
peers = bdecode(r.text)["peers"]
print type(peers)

print (len(peers))
#peers = str(peers)
#print type(peers)
peers=peers.encode('ascii', 'ignore')

ip = struct.unpack_from("!i",peers,0)[0]
ip = socket.inet_ntoa(struct.pack("!i", ip))

print ip
