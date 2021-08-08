#include<bits/stdc++.h>
#include<windows.h>

using namespace std;

const char HEX[]="0123456789ABCDEF";

int main(){
    auto handle=GetStdHandle(STD_OUTPUT_HANDLE); // auto = HANDLE
    for(int i=0;i<16;i++){
        for(int j=0;j<16;j++){
            SetConsoleTextAttribute(handle,(i<<4)|j); // 0xi[0-f]j[0-f]
            printf("(%c%c)",HEX[i],HEX[j]);
        }
        printf("\n");
    }
    SetConsoleTextAttribute(handle,0x07);
    return 0;
}