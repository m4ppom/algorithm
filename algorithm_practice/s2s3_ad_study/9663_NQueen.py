import sys
sys.stdin = open('NQ.txt', 'r')


def attacQing(i, j):
    global N
    for a in range(N):
        visited[a][j] += 1
    for a in range(N):
        visited[i][a] += 1
    while -1 < i+dy[0] < N and -1 < j+dx[0] < N:
        i += dy[0]
        j += dx[0]
        visited[i][j] += 1
    while -1 < i+dy[1] < N and -1 < j+dx[1] < N:
        i += dy[1]
        j += dx[1]
        visited[i][j] += 1
    while -1 < i+dy[2] < N and -1 < j+dx[2] < N:
        i += dy[2]
        j += dx[2]
        visited[i][j] += 1
    while -1 < i+dy[3] < N and -1 < j+dx[3] < N:
        i += dy[3]
        j += dx[3]
        visited[i][j] += 1

def fbQueen(i, j):
    for a in range(N):
        visited[a][j] -= 1
    for a in range(N):
        visited[i][a] -= 1
    while -1 < i + dy[0] < N and -1 < j + dx[0] < N:
        i += dy[0]
        j += dx[0]
        visited[i][j] -= 1
    while -1 < i + dy[1] < N and -1 < j + dx[1] < N:
        i += dy[1]
        j += dx[1]
        visited[i][j] -= 1
    while -1 < i + dy[2] < N and -1 < j + dx[2] < N:
        i += dy[2]
        j += dx[2]
        visited[i][j] -= 1
    while -1 < i + dy[3] < N and -1 < j + dx[3] < N:
        i += dy[3]
        j += dx[3]
        visited[i][j] -= 1


def queen(i, j):
    global count, N, ans
    if count == N:
        ans += 1
        return
    for a in range(N):
        if visited[i+1][a] == 0:
            count += 1
            if count == N:
                ans += 1
                break
            attacQing(i+1, a)
            queen(i+1, a)
            count -= 1
            fbQueen(i+1, a)

dy = [-1,1,-1,1]
dx = [1,-1,-1,1]
N = int(input())
visited = [[0]*N for _ in range(N)]
base = [[0]*N for _ in range(N)]
ans = 0
for i in range(N):
    count = 1
    attacQing(0, i)
    queen(0, i)
    fbQueen(0, i)
print(ans)

