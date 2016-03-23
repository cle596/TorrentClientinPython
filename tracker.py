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

def getPeers(hash,id):

    tracker = "http://tracker.tfile.me/announce"+\
              "?info_hash="+hash+\
              "&peer_id="+id+\
              "&port=9000"+\
              "&uploaded=0"+\
              "&event=started"+\
              "&compact=1"

    r = requests.get(tracker)

    res = bdecode(r.text)
    """
    for x in res.keys():
        print(x)
    """
    peers = res["peers"]
    peers = peers.encode('utf8', 'ignore')

    no = len(peers)/6

    #print "IP"+"\t\t"+"PORT"
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
        #print ip+"\t"+str(port)
        i += 1

    return peers_list
