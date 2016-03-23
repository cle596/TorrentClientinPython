from socket import *
from struct import *

def connectPeer(peers,hash,id):

    BUFFER_SIZE = 68
    pstr = "BitTorrent protocol"
    hs = pack("!B19s8x20s20s",len(pstr),pstr,hash,id)
    #hs = chr(19)+pstr+(8*chr(0))+hash+id
    MSG = pack("!2B",1,0)

    s = socket(AF_INET, SOCK_DGRAM)
    s.bind(("127.0.0.1",9000))
    print (len(peers))
    x = peers[len(peers)-2]
    s.sendto(hs, x)
    print "sent"
    d,a = s.recvfrom(1024)
    print "recvd"
    print d,a
    s.close()
