import sys
sys.stdin = open('colorpap.txt', 'r')
import copy
def turning_red():
    return


def square(a, b, color, dir):
    global white, blue, N, size , garo, sero
    if -1 < a < N and -1 < b < N:
        aa = a+dy[dir]
        bb = b+dx[dir]
        while base[aa][bb] == base[a][b]:
            aa = aa + dy[dir]
            bb = bb + dx[dir]
        dir = 1
        aa = aa + dy[dir]
        bb = bb + dx[dir]
        while base[aa][bb] == base[a][b]:
            aa = aa + dy[dir]
            bb = bb + dx[dir]

    else:
        return

dy = [-1, 0]
dx = [0, 1]
N = int(input())
base = [[i for i in list(map(int, input().split()))]for i in range(N)]
print(base)
# yulim:chipmunk: 5:39 PM
# L = [[1, 2, 3, 4, 5], [0, 0, 0, 0, 0]]
# print(sum(L, []).count(0))
blue = 0  # 1
white = 0  # 0
for iii in range(N):
    for jjj in range(N):
        dir = 0
        size = 0
        sero = 0
        garo = 0
        if base[iii][jjj] == 1:
            square(iii, jjj, 1, 0)
        elif base[iii][jjj] == 0:
            square(iii, jjj, 0, 0)
        else:
            pass