#include "connect.h"

int main(){

    printf("Welcome to Light Torrent :)\n\n");

    int sock = make_socket();
    struct sockaddr_in addr = make_addr();
    
    int ret = connect(sock,
		      (struct sockaddr*)&addr,
		      sizeof(struct sockaddr));

    make_request(sock);
    get_response(sock);
    
    close(sock);

    return 0;
}
 
 
