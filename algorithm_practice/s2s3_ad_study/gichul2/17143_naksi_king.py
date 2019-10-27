import sys
sys.stdin = open('einger_King.txt', 'r')

import collections
def sharkmovin():
    basecopy = [[0]*C for _ in range(R)]
    for iii in range(R):
        for jjj in range(C):
            if base[iii][jjj] != 0:



R, C, M = map(int, input().split())
base = [[0]*C for _ in range(R)]
# direction = up:1 down:2 right:3   left:4
summ = 0
for i in range(M):
    r, c, s, d, z = map(int, input().split())
    base[r][c] = [s-1, d-1, z]
while 1:
    got =0
    for man in range(C):
        for ii in range(R):
            if base[ii][C] != 0:
                summ += base[ii][C][2]
                base[ii][C] = 0
                got = 1
                break
        if got == 1:
            break
    else:
        got = 1
    sharkmovin()

