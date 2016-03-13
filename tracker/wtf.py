from bencode import *
import hashlib
import json
import urllib
import string
import random

f = open("damn.torrent")
buf = f.read()
obj = bdecode(buf)
obj2 = obj

info = obj["info"]
info = bencode(info)

del obj2["info"]["pieces"]
print obj2

sha = hashlib.sha1()
sha.update(info)
info_hash = sha.digest()
hex = sha.hexdigest()

info_hash = urllib.quote(info_hash)
print(info_hash)
print(hex)

f.close()

peer = "DE1312"
for x in range(0,14):
    peer += random.choice(string.letters)
peer = urllib.quote(peer)

print(peer)
