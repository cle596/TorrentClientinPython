from socket import *
from struct import *

def connectPeer(peers,hash,id):

    BUFFER_SIZE = 68
    pstr = "BitTorrent protocol"
    hs = pack("!B19s8x20s20s",len(pstr),pstr,hash,id)
    MSG = pack("!2B",1,0)

    s = socket(AF_INET, SOCK_DGRAM)
    #s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    #saddr = '127.0.0.1'
    #sport = 80
    #s.bind((saddr, sport))
    #print s.getsockname()
    print (len(peers))
    x = peers[len(peers)-2]
    TCP_IP = x[0]
    TCP_PORT = x[1]
    print TCP_IP,TCP_PORT
    s.settimeout(4)
    try:
        s.connect((TCP_IP,TCP_PORT))
    except error as socketerror:
        print("Error: ", socketerror)
    #s = create_connection((TCP_IP,TCP_PORT))
    s.send(hs)
    #s.send(MSG)
    #data = s.recv(BUFFER_SIZE)
    s.close()

    print "recv'd: ", data
