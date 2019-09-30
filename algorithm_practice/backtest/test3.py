import sys
sys.stdin = open('test3.txt', 'r')


import itertools
import collections


testcase = int(input())
for test_num in range(1, testcase+1):
    N, M, C = map(int, input().split())
    base = [0] * N
    for i in range(N):
        base[i] = list(map(int, input().split()))
    max_mineral = 0
    sp = 0
    mineral_list = collections.deque()
    for i in range(N):
        for j in range(M):
            if base[i][j] == 1:
                base[i][j] = 0
                sp = [i, j]
    for i in range(N):
        for j in range(M):
            if base[i][j] != 0:
                dist = 2*(abs(i-sp[0])+abs(j-sp[1]))
                mine = base[i][j]
                mineral_list.append([dist, mine])
    for i in range(1, len(mineral_list)+1):
        a = list(map(list, itertools.combinations(mineral_list, i)))
        for i in range(len(a)):
            tot_mineral = 0
            tot_charge = 0
            for j in range(len(a[i])):
                tot_charge += a[i][j][0]
                if tot_charge <= C:
                    tot_mineral += a[i][j][1]
                else:
                    break
            else:
                if max_mineral < tot_mineral:
                    max_mineral = tot_mineral
    print('#%d %d' %(test_num, max_mineral))

