import sys
sys.stdin = open('NQ.txt', 'r')


def attacQing(i, j):
    global N
    for a in range(N):
        visited[a][j] += 1
    for a in range(N):
        visited[i][a] += 1
    while -1 < i < N and -1 < j < N:
        i += dy[0]
        j += dx[0]
        visited[i][j] += 1
    while -1 < i < N and -1 < j < N:
        i += dy[0]
        j += dx[0]
        visited[i][j] += 1
    while -1 < i < N and -1 < j < N:
        i += dy[0]
        j += dx[0]
        visited[i][j] += 1
    while -1 < i < N and -1 < j < N:
        i += dy[0]
        j += dx[0]
        visited[i][j] += 1

def fbQueen(i, j):
    for a in range(N):
        visited[a][j] -= 1
    for a in range(N):
        visited[i][a] -= 1
    while -1 < i < N and -1 < j < N:
        i += dy[0]
        j += dx[0]
        visited[i][j] -= 1
    while -1 < i < N and -1 < j < N:
        i += dy[0]
        j += dx[0]
        visited[i][j] -= 1
    while -1 < i < N and -1 < j < N:
        i += dy[0]
        j += dx[0]
        visited[i][j] -= 1
    while -1 < i < N and -1 < j < N:
        i += dy[0]
        j += dx[0]
        visited[i][j] -= 1


def queen(i, j):
    global count, N, ans
    if visited[i][j] != 0:
        return
    count += 1
    if count == N:
        ans += 1
        return
    attacQing(i, j)
    for a in range(N):
        queen(i+1, j)
        count -= 1
    fbQueen(i, j)

dy = [-1,1,-1,1]
dx = [1,-1,-1,1]
N = int(input())
visited = [[0]*N for _ in range(N)]
base = [[0]*N for _ in range(N)]
count = 0
ans = 0
for i in range(N):
    queen(0, i)
print(ans)

