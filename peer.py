import socket

def connectPeer(peer,hash,id):

    TCP_IP = peer[0]
    TCP_PORT = peer[1] 
    BUFFER_SIZE = 1024
    HANDSHAKE = chr(19) + "BitTorrent protocol" + 8 * chr(0) + hash + id
    MSG = "6"

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print TCP_IP, TCP_PORT
    s.connect((TCP_IP,TCP_PORT))

    s.send(HANDSHAKE)
    data = s.recv(BUFFER_SIZE)
    s.close()

    print "recv'd: ", data
