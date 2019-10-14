import sys
sys.stdin = open('miro.txt')
sys.setrecursionlimit(100000)
# stp = 1,1  1route 0wall


def dfs(a, b):
    global mini, cnt, N, M
    if cnt >= mini:
        return
    if a == N-1 and b == M-1:
        if mini > cnt:
            mini = cnt
    for dir in range(4):
        aa = a+dy[dir]
        bb = b+dx[dir]
        if -1 < aa < N and -1 < bb < M:
            if base[aa][bb] == 1:
                cnt += 1
                base[aa][bb] = 0
                dfs(aa, bb)
                cnt -= 1
                base[aa][bb] = 1


def bfs(c, d):
    global mini, cnt, N, M
    q = []
    q.append((c, d))
    while q:
        cc, dd = q.pop(0)
        if (cc, dd) == (N-1, M-1):
            print(base[cc][dd]-1)
        for dirr in range(4):
            ccc = cc+dy[dirr]
            ddd = dd+dx[dirr]
            if -1 < ccc < N and -1 < ddd < M:
                if base[ccc][ddd] == 1:
                    q.append((ccc, ddd))
                    base[ccc][ddd] = base[cc][dd] + 1





dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
N, M = map(int, input().split())
base = [0]*N
for i in range(N):  # 미로 생성
    base[i] = list(map(int, input()))
mini = 99999
cnt = 0
# base[0][0] = 0
# dfs(0,0)
# print(mini+1)
base[0][0] = 2
bfs(0, 0)

