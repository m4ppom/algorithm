import sys
sys.stdin = open('input0828.txt', 'r')

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]


def detoxi(i, j):
    global leng
    cntcol = 1
    cntrow = 1
    dircnt = [0]*4
    base[i][j] = 0
    ret = 0
    while ret != 1:
        for a in range(4):
            while base[i+dy[a]][j+dx[a]] != 0:
                i += dy[a]
                j += dx[a]
                base[i][j] = 0
                if dircnt[0] == 0 and a == 0:
                    cntrow += 1
                elif dircnt[1] == 0 and a == 1:
                    cntcol += 1
            dircnt[a] = 1
        for a in range(4):
            if base[i+dy[a]][j+dx[a]] == 0:
                ret = 0
            else:
                break
        else:
            ret = 1
    leng += 1
    return cntrow, cntcol


testcase = int(input())
for test_num in range(1, testcase+1):
    result = []
    leng = 0
    N = int(input())
    base = [0] * N
    for ggg in range(N):
        base[ggg] = list(map(int, input().split()))
    for i in range(N):
        for j in range(N):
            if base[i][j] != 0:
                a, b = detoxi(i, j)
                result.append([a, b])
    reresult = []
    for cnt in range(len(result)):
        num = int(result[cnt][0]) * int(result[cnt][1])
        result[cnt].append(num)
    for i in range(len(result)-1):
        for j in range(i+1, len(result)):
            if result[i][2] > result[j][2]:
                result[i], result[j] = result[j], result[i]
            if result[i][2] == result[j][2]:
                if result[i][0] > result[j][0]:
                    result[i], result[j] = result[j], result[i]

    print('#{}'.format(test_num), end='')
    print(' {}'.format(leng), end='')
    for i in range(len(result)):
        print(' {} {}'.format(result[i][0], result[i][1]), end= '')
    print()
