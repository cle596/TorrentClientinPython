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

    printf("%d\n",ntohl(addr.sin_addr.s_addr));
    printf("%s\n",inet_ntoa(addr.sin_addr));

    struct addrinfo* result;
    int err = getaddrinfo("avistaz.to",
			  NULL,
			  NULL,
			  &result);
    struct sockaddr_in* res = (struct sockaddr_in*)result->ai_addr;
    printf("avistaz addr %s\n",inet_ntoa(res->sin_addr));
    
    close(sock);
    
    return 0;
}
 
 
