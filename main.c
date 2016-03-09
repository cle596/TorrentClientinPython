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

int main(){

  printf("Light Torrent\n\n");

  int sock = socket(AF_INET,SOCK_STREAM,0);
  struct sockaddr_in addr;
  addr.sin_family = AF_INET;
  addr.sin_addr.s_addr = htonl(INADDR_LOOPBACK);
  addr.sin_port = htons(8000);

  int ret = connect(sock,(struct sockaddr*)&addr,sizeof(struct sockaddr));

  char* req = "GET / HTTP 1.1\r\nHost: localhost:8000\r\nAccept: */*\r\nUser-Agent: curl/7.43.0\r\nConnection: close\r\n\r\n";  
  int sent = send(sock,req,strlen(req),0);
  
  int recv_len = 1000;
  char buf[recv_len];
  bzero(buf,sizeof(buf));
  int len = recv(
		 sock,
		 buf,
		 sizeof(buf)-1,
		 0
		 );
  if (len>0){
    printf("%s\n",buf);
  }

  close(sock);

  return 0;
}
 
