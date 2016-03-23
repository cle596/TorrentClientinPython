from socket import *
from struct import *


def connectPeer(peers, hash, id):

    buf_size = 68
    pstr = "BitTorrent protocol"
    hs = pack("!B19s8x20s20s", len(pstr), pstr, hash, id)
    #msg = pack("!2B",1,0)

    #s = socket(AF_INET, SOCK_DGRAM)
    s = socket(AF_INET,SOCK_STREAM)
    s.bind(("0.0.0.0", 9000))
    print str(len(peers)) + " peers"
    x = peers[0]
    s.connect(x)
    print "connected"
    s.send(hs)
    print "sent"
    d = recv(buf_size)
    #print str(s.sendto(hs, x)) + " bytes sent"
    #d = s.recvfrom(buf_size)
    print "recvd: " + str(d)
    s.close()
