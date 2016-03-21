import socket
from struct import *

def connectPeer(peers,hash,id):

    BUFFER_SIZE = 68
    pstr = "BitTorrent protocol"
    hs = pack("!B19s8x20s20s",len(pstr),pstr,hash,id)
    MSG = pack("!2B",1,0)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print (len(peers))
    x = peers[len(peers)-2]
    TCP_IP = x[0]
    TCP_PORT = x[1]
    s.connect((TCP_IP,TCP_PORT))
    s.send(hs)
    s.send(MSG)
    data = s.recv(BUFFER_SIZE)
    s.close()

    print "recv'd: ", data
