import sys
sys.stdin = open('jose.txt', 'r')

from collections import deque
N, M = map(int, input().split())
q = deque()
for i in range(1, N+1):
    q.append(i)
idx = 0
ans = deque()
cnt = 0
while len(ans) != N:
    a = q.popleft()
    cnt += 1
    if cnt == M:
        ans.append(a)
        cnt = 0
    else:
        q.append(a)
print('<', end='')
for f in range(N):
    if f == N-1:
        print('%d' % ans[f], end='')
    else:
        print('%d' % ans[f], end=', ')
print('>')