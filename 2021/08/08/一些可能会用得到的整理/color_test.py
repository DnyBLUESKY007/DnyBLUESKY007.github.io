import sys, os

try:
    from ctypes import *
    from win32con import *
except:
    pass

GetStdHandle=windll.kernel32.GetStdHandle
SetConsoleTextAttribute=windll.kernel32.SetConsoleTextAttribute

STD_OUTPUT_HANDLE=-11

def main():
    handle=GetStdHandle(STD_OUTPUT_HANDLE)
    for i in range(16):
        for j in range(16):
            SetConsoleTextAttribute(handle,i*16+j)
            print('({1})'.format(hex(i*16+j)),end='');

if __name__=='__main__':
    main()