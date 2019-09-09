import sys
sys.stdin = open('inpu.txt', 'r')
import copy
​
#
# def dfs(y, x):
#     global cnt, dircnt
#     visited[y][x] = 1
#     cnt += 1
#     for direc in range(4):
#         dircnt += 1
#         if -1< y+dy[direc] < row and -1 < x+dx[direc] < col:
#             if base[y+dy[direc]][x+dx[direc]] == 'L' and visited[y+dy[direc]][x+dx[direc]] == 0:
#                 dfs(y+dy[direc], x+dx[direc])
#     a.append([dircnt, cnt])
#     visited[y][x] = 0
#     cnt -= 1
#     dircnt -= 1
#     return
#
#
# dy = [-1, 1, 0, 0]
# dx = [0, 0, -1, 1]
# row, col = map(int, input().split())
# base = [0]*row
# a = []
# re = []
# for i in range(row):
#     base[i] = list(map(str, input()))
# for i in range(row):
#     for j in range(col):
#         visited = [[0 for _ in range(col)] for _ in range(row)]
#         dircnt = 0
#         cnt = 0
#         if base[i][j] == 'L':
#             print(i,j)
#             dfs(i, j)
#             maxi = 0
#             print(a)
#             for aaa in range(len(a)):
#                 if maxi < a[aaa][1]:
#                     maxi = a[aaa][1]
#                     print(maxi, 'aaa',a[aaa][1])
#             re.append(maxi)
#             a = []
#
# print(re)
# print(a)
# print(maxi+1)
def BFS(x, y):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    q = []
    q.append((x, y))
    dist = [[0] * M for i in range(N)]
    dist[x][y] = 1
    ret = 0
    while len(q):
        (x, y) = q.pop(0)
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            ret = max(ret, dist[x][y])
            if 0 <= xx < N and 0 <= yy < M:
                if G[xx][yy] == 'L' and dist[xx][yy] == 0:
                    q.append((xx, yy))
                    dist[xx][yy] = dist[x][y] + 1
    return ret - 1
​
​
N, M = map(int, input().split())
G = [input() for i in range(N)]
​
ans = 0
for i in range(N):
    for j in range(M):
        if G[i][j] == 'L':
            ans = max(ans, BFS(i, j))
print(ans)