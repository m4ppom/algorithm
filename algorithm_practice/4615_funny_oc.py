import sys
sys.stdin = open('input0902.txt', 'r')


def stone(row, col, color):
    global N
    for i in range(8):
        mul = 1
        if row+dy[i] == -1 or row+dy[i] == N or col+dx[i] == -1 or col+dx[i] == N:
            continue
        if color + base[row+dy[i]][col+dx[i]] == 3:
            while 1:
                mul += 1
                if mul == N:
                    break
                if row + mul*dy[i] <= -1 or row + mul*dy[i] >= N or col + mul*dx[i] <= -1 or col + mul*dx[i] >= N:
                    # base[row + dy[i]][col + dx[i]] = color
                    break
                if base[row+mul*dy[i]][col+mul*dx[i]] == 0:
                    break
                else:
                    if color == base[row+mul*dy[i]][col+mul*dx[i]]:
                        for aa in range(1, mul+1):
                            base[row + aa*dy[i]][col + aa*dx[i]] = color
                        break


# 2 백 1 흑
dx = [0, 0, -1, 1, 1, 1, -1, -1]
dy = [-1, 1, 0, 0, 1, -1, -1, 1]
testcase = int(input())
for test_num in range(1, testcase+1):
    N, M = map(int, input().split())
    # Ncase 468
    if N == 4:
        base = [[0 for _ in range(4)] for _ in range(4)]
        base[1][1] = base[2][2] = 2
        base[1][2] = base[2][1] = 1
    elif N == 6:
        base = [[0 for _ in range(6)] for _ in range(6)]
        base[2][2] = base[3][3] = 2
        base[2][3] = base[3][2] = 1
    else:
        base = [[0 for _ in range(8)] for _ in range(8)]
        base[3][3] = base[4][4] = 2
        base[3][4] = base[4][3] = 1
    for i in range(M):
        col, row, color = map(int, input().split())
        col -= 1
        row -= 1
        base[row][col] = color
        stone(row, col, color)
        # print('rrr',row,'ccc',col,base)
    cnt_black = 0
    cnt_white = 0
    for i in range(N):
        for j in range(N):
            if base[i][j] == 1:
                cnt_black += 1
            elif base[i][j] == 2:
                cnt_white += 1
    # 흑 백
    # print(base)
    print('#{} {} {}'.format(test_num, cnt_black, cnt_white))

