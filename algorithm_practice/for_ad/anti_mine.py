import sys
sys.stdin = open('mine.txt', 'r')
import collections


def bfs(i, j):
    q = collections.deque()
    q.append((i, j))
    while q:
        i, j = q.popleft()
        for d in range(4):
            ii = i+dy[d]
            jj = j+dx[d]
            if -1 < ii < N and -1 < jj < N and vst[ii][jj] == 0 and L[ii][jj] == '.':  #
                q.append((jj, ii))
                vst[ii][jj] = vst[i][j] + 1
            else:
                continue

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    L = [list(map(str, input())) for _ in range(N)]
    vst = [[0]*N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if L[i][j] == '.' and vst[i][j] == 0:
                vst[i][j] = 1
                bfs(i, j)
                cnt += 1
    print('#%d %d' % (tc, cnt))