import sys, copy

sys.stdin =open('cacaca.txt', 'r')


def dist(a, aa, b, bb):
    return abs(a-b)+abs(aa-bb)


# def bfs(st_a, st_b):
#     q = []
#     vict_list = []
#     q.append((st_a, st_b))
#     while q:
#         iii, jjj = q.pop(0)
#         for dir in range(3):
#             iiii = iii + dy[dir]
#             jjjj = jjj + dx[dir]
#             if -1 < iiii < N and -1 < jjjj < M:
#                 if base[iiii][jjjj] == 1:
#                     q.append((iiii, jjjj))


N, M, D = map(int, input().split())
base = [0]*(N+1)
for i in range(N):
    base[i] = list(map(int, input().split()))
base[N] = [0]*M
visited = [0]*M
maxi = 0
for ee in range(M):
    bases = [[0]*N for _ in range(M)]
    for qq in range(N):
        for ww in range(M):
            if base[qq][ww] == 1:
                bases[qq][ww] = dist(qq, ww, N, ee)
    base[N][ee] = bases
print(base)

for aaaa in range(M):

    for bbbb in range(N):
        for cccc in range(M):


