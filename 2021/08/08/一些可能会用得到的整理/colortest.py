import sys

def main():
    for i in (0,3,4,9,10):
        for j in range(i*10,i*10+9):
            print('\033[0m',file=sys.stderr,end='')
            print('\033[0;{num}m ({num}){sp}'.format(num=j,sp='\t\n'[1 if j%10==8 else 0]),file=sys.stderr,sep='',end='')
    print('\033[0m',file=sys.stderr,end='')

    # for r in range(256):
    #     for g in range(256):
    #         for b in range(256):
    #             print('\033[0m',file=sys.stderr,end='')
    #             print('\033[38;2;{r};{g};{b}m ({r},{g},{b})'.format(r=r,g=g,b=b),file=sys.stderr)
    # print('\033[0m',file=sys.stderr,end='')

    # print('\033[41mtest\033[92mtest\033[0m',file=sys.stderr)
    # print('check')
    # print('\033[38;2;245;197;3mtest\033[48;2;210;2;0mtest\033[0m',file=sys.stderr)
    # print('\033[1m\033[38;2;245;197;3mtest\033[48;2;210;2;0mtest\033[0m',file=sys.stderr)
    # print('\033[2m\033[38;2;245;197;3mtest\033[48;2;210;2;0mtest\033[0m',file=sys.stderr)
    # print('\033[3m\033[38;2;245;197;3mtest\033[48;2;210;2;0mtest\033[0m',file=sys.stderr)
    # print('\033[4m\033[38;2;245;197;3mtest\033[48;2;210;2;0mtest\033[0m',file=sys.stderr)
    # print('\033[5m\033[38;2;245;197;3mtest\033[48;2;210;2;0mtest\033[0m',file=sys.stderr)
    # print('\033[6m\033[38;2;245;197;3mtest\033[48;2;210;2;0mtest\033[0m',file=sys.stderr)
    # print('\033[7m\033[38;2;245;197;3mtest\033[48;2;210;2;0mtest\033[0m',file=sys.stderr)
    # print('\033[8m\033[38;2;245;197;3mtest\033[48;2;210;2;0mtest\033[0m',file=sys.stderr)
    # print('\033[9m\033[38;2;245;197;3mtest\033[48;2;210;2;0mtest\033[0m',file=sys.stderr)
    # print('\033[08;2;245;197;3mtest\033[18;2;245;197;3mtest\033[0m',file=sys.stderr)
    # print('\033[28;2;245;197;3mtest\033[58;2;245;197;3mtest\033[0m',file=sys.stderr)
    # print('\033[68;2;245;197;3mtest\033[78;2;245;197;3mtest\033[0m',file=sys.stderr)
    # print('\033[88;2;245;197;3mtest\033[98;2;245;197;3mtest\033[0m',file=sys.stderr)
    # print('\033[98;2;245;197;3mtest\033[108;2;245;197;3mtest\033[0m',file=sys.stderr)

if __name__=='__main__':
    main()