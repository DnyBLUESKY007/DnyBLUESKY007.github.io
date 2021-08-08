#include<bits/stdc++.h>

using namespace std;

const char HEX[]="0123456789ABCDEF";

int main(){
    for(int i=0;i<110;i++){
        printf("\e[0m\e[0;%dm(%d)%c\t%c",i,i," \0"[i%10==9],"\0\n"[i%10==9]);
    }
    printf("\033[0m");
    // for(int r=0;r<256;r++){
    //     for(int g=0;g<256;g++){
    //         for(int b=0;b<256;b++){
    //             printf("\e[0m\e[38;2;%d;%d;%dm(%d,%d,%d)\n",r,g,b,r,g,b);
    //         }
    //     }
    // }
    // printf("\033[0m");
    return 0;
}