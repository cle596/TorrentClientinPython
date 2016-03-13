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

tracker = "http://tracker.yts.re/announce"+\
          "?info_hash=%D9%5Cy%F7U5%407%5De%9C%CC%5B%2C%A7%9D%A3%1E%B1%DF"+\
          "&peer_id=12345678901234567890"+\
          "&uploaded=0"+\
          "&event=started"+\
          "&compact=1"

r = requests.get(tracker)
print r
print (r.text)
res = bdecode(r.text)
peers = res["peers"]
peers = peers.encode("utf8")

print peers
