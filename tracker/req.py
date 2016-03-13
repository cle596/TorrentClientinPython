import requests
from bencode import *
import pprint 
import codecs

tracker = "http://glotorrents.com:6969/announce?"+\
          "info_hash=_%0E%9B%F4%DAX%9F%AE%8F%BE%DEh%2Ah16ff%D0%8E"+\
          ""

r = requests.get(tracker)

res = bdecode(r.text)

pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(res)

peers = res["peers"]
print type(peers)
