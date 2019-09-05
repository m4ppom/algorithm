import sys
import copy
sys.stdin = open('inpu.txt', 'r')

dx = [0, 1]
dy = [-1, 0]
testcase = int(input())
for test_num in range(1, testcase + 1):
    N, K = map(int, input().split())
    base = [0]*N
    count = 0
    for i in range(N):
        base[i] = list(map(int, input().split()))
    base_copy = copy.deepcopy(base)
    count_c = 0
    count_r = 0
    for i in range(N):
        for j in range(N):
            a = i
            c = i
            b = j
            d = j
            if base[i][j] == 1:
                cnt_x = 0
                cnt_y = 0
                while -1 < a < N and -1 < b < N:
                    if base[a][b] == 1:
                        base[a][b] = 0
                        cnt_x += 1
                        b += 1
                    else:
                        break
                if cnt_x == K:
                    count_r += 1
                # while -1 < c < N and -1 < d < N:
                #     if base_copy[c][d] == 1:
                #         base_copy[c][d] = 0
                #         cnt_y += 1
                #         c += 1
                #     else:
                #         break
                # if cnt_y == K:
                #     count_c += 1
            else:
                pass
    for i in range(N):
        for j in range(N):
            c = i
            d = j
            if base_copy[i][j] == 1:
                cnt_x = 0
                cnt_y = 0
                while -1 < c < N and -1 < d < N:
                    if base_copy[c][d] == 1:
                        base_copy[c][d] = 0
                        cnt_y += 1
                        c += 1
                    else:
                        break
                if cnt_y == K:
                    count_c += 1
    # print('rrrrr',count_r, 'ccccc', count_c)
    count = count_r + count_c
    print('#{} {}'.format(test_num, count))
