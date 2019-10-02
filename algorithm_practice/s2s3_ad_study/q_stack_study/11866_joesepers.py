import sys
sys.stdin = open('jose.txt', 'r')

import collections
N, M = map(int, input().split())
q = []
for i in range(1, N+1):
    q.append(i)
idx = 0
ans = collections.deque()
while q:
    idx += M - 1
    while idx >= len(q):
        idx -= len(q)-1
    print(idx)
    if idx >= len(q):
        idx -= len(q)
        a = q.pop(idx)
        ans.append(a)
    else:
        a = q.pop(idx)
        ans.append(a)
print(ans)