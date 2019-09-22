import sys
sys.stdin = open('cony.txt', 'r')

import math
def bfs(x, y):
    global cnt
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    q = []
    q.append((x, y))
    dist = [[0]*(garo+1) for _ in range(sero+1)]
    dist[x][y] = 1
    ret = 0
    while len(q):
        (x, y) = q.pop(0)
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            ret = max(ret, dist[x][y])
            if 0 <= xx < garo+1 and 0 <= yy < sero+1:
                if base[xx][yy] == 0 and dist[xx][yy] == 0:
                    q.append((xx, yy))
                    dist[xx][yy] = dist[x][y] + 1
                elif base[xx][yy] == 1 and dist[xx][yy] == 0:
                    dist[xx][yy] = dist[x][y] + 1
                    cnt = dist[xx][yy]
                    return

    return ret - 1


garo, sero = map(int, input().split())
base = [[0]*(garo+1) for _ in range(sero+1)]
cony_cord = list(map(int, input().split()))
base[cony_cord[1]][cony_cord[0]] = 1
cnt = 0
if -1< cony_cord[0]< garo+1 or -1 < cony_cord[1] < sero + 1:
    bfs(0,0)
    a = math.factorial(cony_cord[0]+cony_cord[1])//(math.factorial(cony_cord[1])*math.factorial(cony_cord[0]))
    print(cnt-1)
    print(a)
else:
    print('fail')