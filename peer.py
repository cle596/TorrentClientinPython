import socket
from struct import *

def connectPeer(peer,hash,id):

    TCP_IP = peer[0]
    TCP_PORT = peer[1]
    BUFFER_SIZE = 68
    pstr = "BitTorrent protocol"
    hs = pack("!B19s8x20s20s",len(pstr),pstr,hash,id)
    MSG = pack("!2B",1,0)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(10)
    try:
        s.connect((TCP_IP,TCP_PORT))
    except:
        print "fail"
    s.settimeout(None)
    s.send(hs)
    s.send(MSG)
    data = s.recv(BUFFER_SIZE)
    s.close()

    print "recv'd: ", data
