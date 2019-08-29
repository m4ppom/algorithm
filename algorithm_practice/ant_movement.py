import sys
sys.stdin = open('input0828.txt', 'r')





# start[0,0]

def reflection(no, dir):
    if no == 1:
        if dir == 2:
            return 1
        elif dir == 3:
            return 0
        elif dir == 0:
            return 3
        elif dir == 1:
            return 2
    elif no == 2:
        if dir == 3:
            return 1
        elif dir == 1:
            return 3
        elif dir == 0:
            return 2
        elif dir == 2:
            return 0
#
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
def movement(i, j, dir):
    global cnt

    while i + dy[dir] != -1 and i + dy[dir] != 10 and j + dx[dir] != -1 and j + dx[dir] != 10:
        i += dy[dir]
        j += dx[dir]
        cnt += 1
        if base[i][j] != 0:
            dir = reflection(base[i][j], dir)

        if i + dy[dir] == -1 and i + dy[dir] == 10 and j + dx[dir] == -1 and j + dx[dir] == 10:
            return


tc = int(input())
for test_num in range(1, tc+1):
    cnt =0
    N = int(input())
    base = [0] * N
    for i in range(N):
        base[i] = list(map(int, input().split()))

    # print (base)
    movement(0, 0, 2)
    print('#%d %d'%(test_num, cnt))