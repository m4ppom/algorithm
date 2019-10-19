import sys
sys.stdin = open('gay.txt', 'r')

import itertools
import collections


def correct(numm):
    for h in range(N):
        if base[numm][h] == 1 and visited[h] == 0:
            visited[h] = 1
            

    return


N = int(input())
mann_list = list(map(int, input().split()))
base = [[0]*N for _ in range(N)]
for i in range(N):
    info = list(map(int, input().split()))
    for j in range(1, len(info)):
        jj = info[j] -1
        base[i][jj] = 1
print(base)
mini = 999999
b = sum(mann_list)
q = collections.deque()
for m in range(N):
    a = list(itertools.combinations(mann_list, m))
    for mm in range(len(a)):
        aa = sum(a[mm])
        c = abs(aa-b)
        d = abs(aa-c)
        if mini >= d:
            if mini == d:
                q.append(a[mm])
            else:
                mini = d
                q = collections.deque()
                q.append(a[mm])
print(mini)
print(q)
while q:
    lst = q.popleft()
    visited = [0]*N
    for numb in lst:
        bb = numb-1
        # correct(bb)
