from infohash import *
from tracker import *
from peer import *

hash = getInfoHash()
id = getID()
peers = getPeers(hash,id)
connectPeer(peers[0],hash,id)
