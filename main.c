//3

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

  printf("Light Torrent\n");

  int sock = socket(AF_INET,SOCK_STREAM,0);
  struct sockaddr_in addr;
  addr.sin_family = AF_INET;
  addr.sin_addr.s_addr = htonl(INADDR_LOOPBACK);
  addr.sin_port = htons(8000);
  int ret = connect(sock,(struct sockaddr*)&addr,sizeof(struct sockaddr));
  //printf("%d\n",ret);
  char* req = "GET / HTTP 1.1\r\nHost: localhost:8000\r\nConnection: keep-alive\r\naccept: */*\r\nuser-agent: changhan\r\n\r\n";
  int sent = send(sock,req,strlen(req),0);
  printf("sent: %d\n",sent);
  int recv_len = 1000;
  char buf[recv_len];
  bzero(buf,strlen(buf));
  printf("buf: %s\n",buf);
  int len = recv(sock,buf,recv_len-1,0);
  printf("received length: %d\n",len);
  buf[recv_len-1]='\0';
  printf("received msg:\n%s\n",buf);
  close(sock);

  return 0;
}
