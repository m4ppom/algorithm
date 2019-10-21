import sys
sys.stdin = open('bric.txt', 'r')
from collections import deque
from copy import deepcopy


def bfs(iii, jjj):
    global N, M, minnn
    q.append((iii, jjj))
    while q:
        iiii, jjjj = q.popleft()
        if basecopy[iiii][jjjj] > minnn:
            return
        for dir in range(4):
            iiiii = iiii + dy[dir]
            jjjjj = jjjj + dx[dir]
            if -1 < iiiii < N and -1 < jjjjj < M:
                if basecopy[iiiii][jjjjj] == 0:
                    q.append((iiiii, jjjjj))
                    basecopy[iiiii][jjjjj] = basecopy[iiii][jjjj]+1
                    if (iiiii, jjjjj) == (N-1, M-1):
                        if minnn > basecopy[iiiii][jjjjj]:
                            minnn = basecopy[iiiii][jjjjj]
                            return



dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
N, M = map(int,input().split())
base = [0]*N
for i in range(N):
    base[i] = list(map(int, input()))
q = deque()
minnn = 999999
basecopy = deepcopy(base)
for ii in range(N):
    for jj in range(M):
        if base[ii][jj] == 1:
            basecopy[0][0] = 1
            basecopy[ii][jj] = 0
            bfs(0, 0)
            q = deque()
            basecopy = deepcopy(base)
if minnn == 999999:
    print(-1)
else:
    print(minnn)
