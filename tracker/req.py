import requests
from bencode import *
import pprint 
import codecs
import binascii
import unicodedata
import base64

tracker = "http://glotorrents.com:6969/announce"+\
          "?info_hash=_%0E%9B%F4%DAX%9F%AE%8F%BE%DEh%2Ah16ff%D0%8E"+\
          "&peer_id=12345678901234567890"+\
          "&uploaded=0"+\
          "&event=started"+\
          "&compact=1"

r = requests.get(tracker)

res = bdecode(r.text)

peers = res["peers"]

print len(peers)
