import sys
sys.stdin = open('ladder.txt', 'r')
# 세로선이 사실상 가로수 가로선이 사실상 세로 높

import copy, collections




def pathfinder(iii, jjj):
    global Hgarosun, num
    goal = iii
    go = iii
    while True:
        for nn in range(1, Hgarosun+1):
            if go-2 > 0:
                if base[go-2][nn] == 1:

            if go+2 < num:
                if base[go + 2][nn] == 1:
        pass


def canMakeBridge(ii, jj):
    global num
    if ii == 1 and base[ii][jj] == 0:
        if base[ii+2][jj] == 1:
            return
        else:
            hubo.append((ii, jj))
    elif ii == num-1 and base[ii][jj] == 0:
        if base[ii - 3][jj] == 1:
            return
        else:
            hubo.append((ii, jj))
    else:
        if base[ii][jj] == 0:
            if base[ii-2][jj] == 0 and base[ii+2][jj] == 0:
                hubo.append((ii, jj))


def confirm():
    pass


Nserosun, Mgaesu, Hgarosun = map(int, input().split())
base = [[0]*(Hgarosun+1)for _ in range(Nserosun*2+1)]
print(base)
if Mgaesu == 0:
    print(0)
else:
    num = 0
    for gilmandulgui in range(Nserosun):
        base[num] = [1]*(Hgarosun+1)
        num += 2
    print(base)
    for _ in range(Mgaesu):
        a, b = map(int, input().split())
        base[(b-1)*2+1][a] = 1
    # print(base)
    hubo = []
    for vv in range(Nserosun):
        w = (vv * 2) + 1
        for uu in range(1, Hgarosun+1):
            if base[w][uu] == 0:
                canMakeBridge(w, uu)
    print(hubo)

