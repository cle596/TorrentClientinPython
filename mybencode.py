def bencode(file):
    buf = open(file,"rb").read()
    print(buf[:1])

bencode("abc.torrent")
