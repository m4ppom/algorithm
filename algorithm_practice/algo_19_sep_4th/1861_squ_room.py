import sys
import copy
sys.stdin=open('squ_room.txt', 'r')
sys.setrecursionlimit(10000)

import copy


def pathfinder(i, j):
    global maximum, cnt, temp, starting_point

    for a in range(4):
        ii = i+dy[a]
        jj = j+dx[a]
        if -1 < ii < N and -1 < jj < N:
            if base[i][j]+1 == base[ii][jj]:
                cnt += 1
                pathfinder(ii, jj)
                cnt -= 1
    else:
        if maximum == cnt:
            bb = copy.deepcopy(temp)
            starting_point.append(bb)
        if maximum < cnt:
            starting_point = []
            bb = copy.deepcopy(temp)
            starting_point.append(bb)
            maximum = cnt


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
testcase = int(input())
for test_num in range(1, testcase+1):
    N = int(input())
    base = [0]*N
    for i in range(N):
        base[i] = list(map(int, input().split()))
        coco = copy.deepcopy(base)
    visited = [[0]*N for _ in range(N)]
    maximum = 0
    cnt = 0
    starting_point = []
    for i in range(N):
        for j in range(N):
            coco = copy.deepcopy(base)
            temp = base[i][j]
            pathfinder(i, j)
    a = sorted(starting_point)
    print('#%d %d %d' %(test_num, a[0], maximum+1))