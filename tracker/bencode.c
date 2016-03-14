#include<stdlib.h>
#include<stdio.h>
#include<locale.h>

int main(){

    FILE* f = fopen("abc.torrent","r");
    fseek(f,0L,SEEK_END);
    long int sz = ftell(f);
    printf("%ld\n",sz);
    fseek(f,0L,SEEK_SET);
    unsigned char buf[sz];
    fread(buf,1,sz,f);
    fclose(f);

    FILE* d = fopen("dump.txt","w");
    fwrite(buf,1,sz,d);

    return 0;
}
