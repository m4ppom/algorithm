import sys
sys.stdin = open('totoma.txt')

from copy import deepcopy
# e_gum == 1//anni_gum=0 // up_um==-1


def spread(i, j, k):
    global cnt, maxx, sangjaKugi_garo, no_p
    # print(i, j, k)
    visited[k][i][j] = 1
    if cnt == maxx:
        return
    for dir in range(4):
        if -1 < i+dy[dir] < sangjaKugi_sero and -1 < j+dx[dir] < sangjaKugi_garo:
            if base[k][i+dy[dir]][j+dx[dir]] == 0 and visited[k][i + dy[dir]][j + dx[dir]] == 0:
                cnt += 1
                base_copy[k][i + dy[dir]][j + dx[dir]] = 1
                visited[k][i + dy[dir]][j + dx[dir]] = 1
    for we_arr in range(2):
        if -1 < k+dz[we_arr] < no_p:
            if base[k+dz[we_arr]][i][j] == 0 and visited[k+dz[we_arr]][i][j] == 0:
                cnt += 1
                base_copy[k + dz[we_arr]][i][j] = 1
                visited[k + dz[we_arr]][i][j] = 1


sangjaKugi_garo, sangjaKugi_sero, no_p = map(int, input().split())
# 위 아래 +4방향
dz = [-1, 1] # 위 아래 4방향
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
base = [[0]*sangjaKugi_sero for i in range(no_p)]
for nope in range(no_p):  # 3차원으로 상자 선언
    for se in range(sangjaKugi_sero):
        base[nope][se] = list(map(int, input().split()))
# print(base)  # 못가는곳 빼고 갈 수 있는 모든 곳 계산.
base_copy = deepcopy(base) # 한 회차 반영하기위해 deepcopy
visited = [[[0]*sangjaKugi_garo for __ in range(sangjaKugi_sero)]for _ in range(no_p)]
maxx = sangjaKugi_garo * sangjaKugi_sero
for ii in range(no_p):
    empty = sum(base[ii], []).count(-1)
    zero = sum(base[ii], []).count(0)
maxx = sangjaKugi_garo * sangjaKugi_sero * no_p - empty
cnt = 0  # 이게 최대랑 같으면 끝.
temp = 10
phase = 0
if zero != 0:
    while 1: #cnt != temp:
        # print(cnt)
        # temp = cnt
        phase += 1
        for kkk in range(no_p):
            for iii in range(sangjaKugi_sero):
                for jjj in range(sangjaKugi_garo):
                    if base[kkk][iii][jjj] == 1 and visited[kkk][iii][jjj] == 0:
                        cnt += 1
                        spread(iii, jjj, kkk)
                    if cnt == maxx:
                        break
                if cnt == maxx:
                    break
            if cnt == maxx:
                break
        else:
            if cnt == temp:
                break
            temp = cnt
            base = deepcopy(base_copy)
            base_copy = deepcopy(base)
'''
no p 한바퀴 == 한사이클
'''
if cnt == maxx or phase == 0:
    # if phase != 0:
    #     print(phase-2)
    # else:
    print(phase)
else:
    print(-1)


