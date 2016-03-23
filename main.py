from infohash import *
from tracker import *
from peer import *

myhash = getInfoHash()
myid = getID()
peers = getPeers(myhash,myid)
connectPeer(peers,myhash,myid)
