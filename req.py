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

peers = bdecode(r.text)["peers"]
peers = peers.encode('utf8', 'ignore')

no = len(peers)/6

print "IP"+"\t\t"+"PORT"
peers_list = []
i=0
offset = 0
while i < no:
    ip = struct.unpack_from("!i",peers,offset)[0]
    ip = socket.inet_ntoa(struct.pack("!i", ip))
    offset += 4
    port = struct.unpack_from("!H",peers,offset)[0]
    offset += 2
    peers_list.append((ip,port))
    print ip+"\t"+str(port)
    i += 1
