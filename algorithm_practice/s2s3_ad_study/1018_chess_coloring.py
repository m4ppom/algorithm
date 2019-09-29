import sys
sys.stdin = open('chess_color.txt', 'r')

import copy
N, M = map(int, input().split())
base = [0] * N
for tt in range(N):
    base[tt] = list(map(str, input()))
mini = 9999999
l = 1
cnt = 0
copy_base = copy.deepcopy(base)
for aaa in range(N-7):
    for bbb in range(M - 7):
        for yy in range(2):
            if yy == 0:
                l = 1
            else:
                l = 0
            for i in range(aaa, aaa+8):  # 1 검  0 화
                if l == 1:
                    l = 0
                else:
                    l = 1
                if cnt > mini:
                    base = copy.deepcopy(copy_base)
                    break
                for j in range(bbb, bbb+8):
                    if cnt > mini:
                        base = copy.deepcopy(copy_base)
                        break
                    if l == 1 and base[i][j] == 'B':
                        l =0
                        continue
                    elif l == 0 and base[i][j] == 'W':
                        l = 1
                        continue
                    if base[i][j] == 'B':
                        base[i][j] = 'W'
                        cnt += 1
                        l = 1
                    else:
                        base[i][j] = 'B'
                        cnt += 1
                        l = 0
            if mini > cnt:
                mini = cnt
            cnt = 0
            l = 0
            base = copy.deepcopy(copy_base)
print(mini)

