from bencode import *
import hashlib
import json
import urllib
import string
import random

def getInfoHash():

    f = open("abc.torrent")
    buf = f.read()
    obj = bdecode(buf)
    obj2 = obj

    info = obj["info"]
    info = bencode(info)

    del obj2["info"]["pieces"]
    #print obj2

    sha = hashlib.sha1()
    sha.update(info)
    info_hash = sha.digest()
    hex = sha.hexdigest()

    info_hash = urllib.quote(info_hash)
    #print(info_hash)
    #print(hex)

    f.close()

    #print(peer)``

    return info_hash

def getID():
    peer = ""
    for x in range(0,20):
        peer += random.choice(string.letters)
    peer = urllib.quote(peer)
    return peer
