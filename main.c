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

#include "connect.h"

int main(){

    printf("Welcome to Light Torrent :)\n\n");

    int sock = make_socket();
    
    int ret = connect(sock,
		      (struct sockaddr*)&addr,
		      sizeof(struct sockaddr));

    make_request();
    get_response();
    
    close(sock);

    return 0;
}
 
 
