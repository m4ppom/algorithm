import sys
sys.stdin = open('brick.txt', 'r')
import collections, copy, itertools
#
#
# def airdrop(j):
#     global H, N, counter, W, mini
#     if counter == N:
#         znum = sum(base, []).count(0)
#         numnum = H*W - znum
#         if mini > numnum:
#             mini = numnum
#         return
#     for ___ in range(H):
#         if base[___][j] == 1:
#             powpow(___, j)
#             break
#
#
# def collapse(i, j):
#     collap = []
#     for _ in range(i-1, -1, -1):
#         if base[_][j] == 0:
#
# def powpow(i, j):
#     q = collections.deque()
#     q.append((i, j))
#     visited.append((i, j))
#     while q:
#         y, x = q.popleft()
#         if base[y][x] != 0 and vztd[y][x] == 0:
#             vztd[y][x] = 1
#             for dir in range(4):
#                 for impact in range(1, base[y][x]):
#                     yy = y+dy[dir]*impact
#                     xx = x+dx[dir]*impact
#                     if base[yy][xx] != 0:
#                         q.append((yy,xx))
#                         visited.append((yy, xx))
#
#
#
#
# dy = [-1, 1, 0, 0]
# dx = [0, 0, -1, 1]
# testnum = int(input())
# for testcase in range(1, testnum+1):
#     N, W, H = map(int, input().split())
#     base = [0]*H
#     counter = 0
#     mini = 9999999
#     number = [_ for _ in range(W)]
#     numlist = list(itertools.combinations_with_replacement(number, N))
#     for _ in range(H):
#         base[_] = list(map(int, input().split()))
#     for __ in range(len(numlist)):
#         for ___ in numlist[__]:
#             vztd = [[0] * W for _____ in range(H)]
#             visited = collections.deque()
#             airdrop(___)


def copy_list():
    global L
    L = copy.deepcopy(CL)
    # for i in range(H):
    #     for j in range(W):
    #         L[i][j] = CL[i][j]
    return


def breakbricks(r, c, V):
    V[c][r] = 1
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 좌우상하

    if L[c][r] == 1:
        L[c][r] = 0
        return

    if L[c][r]:
        for d in dir:
            for i in range(L[c][r] - 1):
                rr, cc = r + d[0] + (i * d[0]), c + d[1] + (i * d[1])
                if 0 <= rr < W and 0 <= cc < H and not V[cc][rr]:
                    if L[cc][rr] > 1:
                        breakbricks(rr, cc, V)
                        L[cc][rr] = 0
                        V[cc][rr] = 1
                    else:
                        L[cc][rr] = 0
                        V[cc][rr] = 1
        L[c][r] = 0
    return


def locate(T):
    global min_bricks

    for r in T:  # 열
        V = [[0] * W for _ in range(H)]
        for c in range(H):  # 행y
            if L[c][r]:
                breakbricks(r, c, V)
                break

        for x in range(W):
            y = H - 1
            cnt = 0
            while y > 0:
                if not L[y][x]:  # 0이면
                    tmp = y
                    while not L[y - 1][x] and y >= 0:
                        y -= 1
                        cnt += 1
                    if y == 0:
                        cnt = 0
                        break
                    L[tmp][x] = L[y - 1][x]
                    L[y - 1][x] = 0
                    if cnt > 0:
                        y += cnt
                y -= 1
                cnt = 0

    bricks = 0
    for i in range(H):
        for j in range(W):
            if L[i][j]:
                bricks += 1
    if min_bricks > bricks:
        min_bricks = bricks

    copy_list()
    return


def comb(k):
    if k == N:
        locate(T)
        return

    for i in range(W):
        T[k] = P[i]
        comb(k + 1)


T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())  # 구슬, 가로(열), 세로(행)
    L = [list(map(int, input().split())) for _ in range(H)]
    # CL = [[0] * W for _ in range(H)]
    # for i in range(H):
    #     for j in range(W):
    #         CL[i][j] = L[i][j]
    CL = copy.deepcopy(L)

    min_bricks = 99999999
    T = [0] * N
    P = [i for i in range(W)]
    # number = [_ for _ in range(W)]
    # numlist = list(itertools.combinations_with_replacement(number, N))
    # for __ in range(len(numlist)):
    #     locate(numlist[__])
    comb(0)

    print('#%d %d' % (tc, min_bricks))
