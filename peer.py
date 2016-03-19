import socket

def connectPeer():

    TCP_IP = '196.152.62.17'
    TCP_PORT = 50077
    BUFFER_SIZE = 1024
    MSG = (chr(19) + \
        "BitTorrent protocol" + \
        8 * chr(0) + \
        self.getInfoHash(torrentCont) + \
        self.peer_id)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP,TCP_PORT))
    s.send(MSG)
    data = s.recv(BUFFER_SIZE)
    s.close()

    print "recv'd: ", data
