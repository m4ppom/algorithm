import sys
sys.stdin = open('bridge2.txt', 'r')
from copy import deepcopy
import itertools
from collections import deque
def bfs(iii, jjj, num):
    q = []
    q.append((iii, jjj))
    while q:
        (a, b) = q.pop()
        base_copy[a][b] = num
        for i in range(4):
            delta_i = a + dy[i]
            delta_j = b + dx[i]
            if -1< delta_i <N and -1<delta_j<M:
                if base[delta_i][delta_j]==1 and base_copy[delta_i][delta_j]==0:
                    q.append((delta_i,delta_j))


def making_bridge(iiii, jjjj):
    start = base_copy[iiii][jjjj]
    for dir in range(4):
        a = iiii
        b = jjjj
        cnt = 0
        if -1<iiii+dy[dir]<N and -1<jjjj+dx[dir]<M:
            while base_copy[iiii+dy[dir]][jjjj+dx[dir]] == 0:
                a += dy[dir]
                b += dx[dir]
                if -1 < a < N and -1 < b < M:
                    if base_copy[a][b] != 0:
                        end = base_copy[a][b]
                        if bridge_info[start][end] > cnt and cnt != 1:
                            bridge_info[start][end] = cnt
                            bridge_info[end][start] = cnt
                        cnt = 0
                        break
                    else:
                        cnt += 1
                else:
                    break


def correct(lst):
    global num
    li = deepcopy(lst)
    vivi = [0]*len(lst)
    visited = [0]*num
    visited[lst[0][0]] = 1
    visited[lst[0][1]] = 1
    vivi[0] = 1
    long = []
    long.append(lst[0][0])
    long.append(lst[0][1])
    for gg in range(len(li)):
        if li[gg][0] == long[0]:  # or li[gg][0] == long[1]:
            long.append(0, li[gg[0]])
        elif li[gg][0] == long[1]:
            long.append(-1, li[gg[0]])
        if li[gg][1] == long[0]:  # or li[gg][0] == long[1]:
            long.append(0, li[gg[1]])
        elif li[gg][1] == long[1]:
            long.append(-1, li[gg[1]])



    if sum(visited) == num-1:
        return num-1
    else:
        return False


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
N, M = map(int, input().split())
base = [[i for i in list(map(int, input().split()))]for _ in range(N)]
# print(base)
num = 1
base_copy = [[0]*M for _ in range(N)]
for ii in range(N):
    for jj in range(M):
        if base[ii][jj] == 1 and base_copy[ii][jj] == 0:
            bfs(ii,jj,num)
            num += 1
bridge_info = [[100]*(num+1) for _ in range(num+1)]
for iiii in range(N):
    for jjjj in range(M):
        if base[iiii][jjjj] == 1:
            making_bridge(iiii, jjjj)
# print(bridge_info)
mmm = list(itertools.combinations(range(1,num), 2))
# print(mmm)
nnn = list(itertools.combinations(mmm, num-2))
# print(nnn)
ssss = 0
mmmiiinniii = 9999
info = []
mnmn = []
lolo = []
for i in range(len(nnn)):
    cbt = 0
    ssss = 0
    # for kkk in range(len(set(nnn[i]))):
    #     tt,kk = nnn[i][kkk]
    #     info.append(tt)
    #     info.append(kk)
    # info = len(set(info))
    for kkk in range(len(set(nnn[i]))):
        tt,kk = nnn[i][kkk]
        lolo.append([tt, kk])
    # print(lolo)
    info = correct(lolo)
    lolo = []
    if info == False:
        continue
    elif info == num-1:
        for j in range(num-2):
            x, y = nnn[i][j]
            if bridge_info[x][y] == 100:
                break
            elif bridge_info[x][y] > 1:
                ssss += bridge_info[x][y]
                cbt += 1
        else:
            if mmmiiinniii > ssss and cbt == num-2:
                mmmiiinniii = ssss
                mnmn = nnn[i]
    info = []
# print(mnmn)
if mmmiiinniii == 9999:
    print(-1)
else:
    print(mmmiiinniii)
