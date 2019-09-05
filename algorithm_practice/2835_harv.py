import sys
sys.stdin = open('inpu.txt', 'r')


def machine(row, col):
    global harv, N
    if row > N//2:
        return
    harv += base[row][col]
    for i in range(row):
        harv += base[row][col]
    count += 1


def machine2(row, col):
    global harv
    for i in range(row)
    harv += base[row][col]
    count += 1


dy1 = [1, 1, 1]
dx1 = [-1, 1, 0]

dy2 = [-1, -1, -1]
dx2 = [0, 1, -1]
testcase = int(input())
for test_num in range(1, testcase+1):
    count = 0
    harv = 0
    direc = 0
    N = int(input())
    base = [0]*N
    for i in range(N):
        base[i] = list(map(int, input()))
    machine(0, N//2)
    machine2(-1, N//2)
    print('#{} {}'.format(test_num, count))