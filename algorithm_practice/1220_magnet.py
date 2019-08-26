import sys
sys.stdin = open('inpu.txt', 'r')

def mag_st(i, j):
    global result
    if i < 99:
        if base[i][j] == 1 and base[i+1][j] == 2:
            result += 1
    return
def magnet_movement(i, j):
    global result
    dy = [1, -1]
    y = i
    if base[i][j] == 1:
        while (y + dy[0]) < 99:
            if base[y + dy[0]][j] == 0:
                # print(y)
                base[y][j] = 0
                # print('base',y + dy[0], j)
                base[y + dy[0]][j] = 1
                y += dy[0]
            else:
                break
    elif base[i][j] == 2:
        while base[y + dy[1]][j] == 0 and y + dy[1] > 0:
            base[y][j] = 0
            base[y + dy[1]][j] = 1
            y += dy[1]

testcase = 10
for tcnum in range(1, testcase + 1):
    stst = []
    result = 0
    base_len = int(input())
    base = [0] * 100
    for i in range(100):
        base[i] = list(map(int, input().split()))

    for i in range(100):
        for j in range(100):
            magnet_movement(i, j)
    for i in range(100):
        for j in range(100):
            mag_st(i, j)




    print('#{} {}'.format(tcnum, result))