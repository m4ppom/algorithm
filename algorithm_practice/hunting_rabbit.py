# from collections import deque
# d = deque('adasd')
# print(d)
#
# print(d[1])

import sys
from collections import deque
sys.stdin = open('input0828.txt', 'r')

# dy = deque([1,-1,0,0,1,-1,1,-1])
dy = [1,-1,0,0,1,-1,1,-1]
dx = [0,0,1,-1,1,-1,-1,1]
# print(dy)
# dx = deque(0,0,1,-1,1,-1,-1,1)
def hunting(i, j):
    global cnt
    time = 0
    while time < 100:
        time+=1
        for a in range(8):
            y = i
            x = j
            if i + dy[a] == -1 or j + dx[a] == -1 or i + dy[a] == 10 or j + dx[a] == 10:
                continue
            while y + dy[a] != -1 and x + dx[a] != -1 and y + dy[a] != 10 and x + dx[a] != 10:
                y += dy[a]
                x += dx[a]
                if base[y][x] == 1:
                    base[y][x] = 0
                    cnt += 1
                    print(cnt)
                elif base[y][x] == 2:
                    break

tc = 1
for test_num in range(1, tc + 1):
    cnt = 0
    base = [0] * 10  # for _ in range(10)
    for i in range(10):
        base[i] = list(map(int, input().split()))
    for i in range(10):
        for j in range(10):
            if base[i][j] == 3:
                hunting(i, j)
    print(base)
    print(cnt)

