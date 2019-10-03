import sys
sys.stdin = open('jose.txt', 'r')

import collections
N, M = map(int, input().split())
q = []
for i in range(1, N+1):
    q.append(i)
idx = 0
ans = collections.deque()
cnt = 0
while q:
    idx += 1
    cnt += 1
    if len(q) == 1:
        a = q.pop()
        ans.append(a)
        break
    if idx == len(q):
        idx = 0
    elif idx == len(q)+1:
        idx = 1
    if cnt == M-1:
        a = q.pop(idx)
        ans.append(a)
        cnt = 0
    # idx += M-1
    # if idx >= len(q):
    #     idx -= len(q)-1
print('<', end='')
for f in range(N):
    if f == N-1:
        print('%d' % ans[f], end='')
    else:
        print('%d' % ans[f], end=', ')
print('>')