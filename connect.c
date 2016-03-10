#include <stddef.h>
#include <stdio.h>
#include <errno.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <sys/un.h>
#include <unistd.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <netdb.h>

struct sockaddr_in make_addr(){
    struct sockaddr_in addr;
    addr.sin_family = AF_INET;
    addr.sin_addr.s_addr = htonl(INADDR_LOOPBACK);
    addr.sin_port = htons(8000);
    return addr;
}

int make_socket(){   
    int sock = socket(AF_INET,SOCK_STREAM,0);
    return sock;
}

void make_request(int sock){
    char* req =
	"GET / HTTP 1.1\r\n"
	"Host: https://tracker.avistaz.to/b3d5d3a8e6c1bae53d9834c08076d7aa/announce\r\n"
	//"Host: localhost:8000\r\n"
	"Accept: */*\r\n"
	"User-Agent: light-torrent\r\n"
	"Connection: close\r\n\r\n";
   int sent = send(sock,req,strlen(req),0);
}

void get_response(int sock){
    int recv_len = 1000;
    char buf[recv_len];
    bzero(buf,sizeof(buf));
    int len = recv(sock,
		   buf,
		   sizeof(buf)-1,
		   0);
    if (len>0){
	printf("%s\n",buf);
    }
}
