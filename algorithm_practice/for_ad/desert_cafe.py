import sys
sys.stdin = open('cafe.txt', 'r')
sys.setrecursionlimit(1101001010)


def in_it(i, j):
    if -1 < i < N and -1 < j < N:
        return True
    else:
        return False


def digging_cafe(i, j, dir):
    global st_point, flag, maxx
    print(i, j)
    if dir == 0 and flag == 1:
        if st_point == (i, j):
            print(dir_lst)
            for _ in range(len(dir_lst)):
                if dir_lst[_] == 0:
                    return
            else:
                summ = sum(bztd)
                if maxx < summ:
                    maxx = summ
        else:
            bztd[base[i][j]] = 1
            for _ in range(2):
                # if _ == 0:
                dir += _
                dir %= 4
                ii = i + dy[dir]
                jj = j + dx[dir]
                if in_it(ii, jj) and bztd[base[ii][jj]] == 0:
                    dir_lst[dir] += 1
                    bztd[base[ii][jj]] = 1
                    digging_cafe(ii, jj, dir)
                    bztd[base[ii][jj]] = 0
                    dir_lst[dir] -= 1
    else:
        flag = 1
        bztd[base[i][j]] = 1
        for _ in range(2):
            # if _ == 0:
            dir += _
            dir %= 4
            ii = i + dy[dir]
            jj = j + dx[dir]
            if in_it(ii, jj) and bztd[base[ii][jj]] == 0:
                dir_lst[dir] += 1
                bztd[base[ii][jj]] = 1
                digging_cafe(ii, jj, dir)
                bztd[base[ii][jj]] = 0
                dir_lst[dir] -= 1
            # else:
            #     dir += 1
            #     dir %= 4
            #     ii = i + dy[dir]
            #     jj = j + dx[dir]
            #     if in_it(ii, jj) and bztd[base[ii][jj]] == 0:
            #         dir_lst[dir] += 1
            #         bztd[base[ii][jj]] = 1
            #         digging_cafe(ii, jj, dir)
            #         bztd[base[ii][jj]] = 0
            #         dir_lst[dir] -= 1



dy = [1, 1, -1, -1]  # clockwise
dx = [1, -1, -1, 1]
testnum = int(input())
for testcase in range(1, testnum+1):
    N = int(input())
    base = [0]*N
    for _ in range(N):
        base[_] = list(map(int, input().split()))
    maxx = 0
    for i in range(N):
        for j in range(N):
            flag = 0
            cafe_lst = []
            bztd = [0] * 101
            dir_lst = [0]*4
            st_point = (i, j)
            digging_cafe(i, j, 0)
    print('#%d %d' %(testcase, maxx))