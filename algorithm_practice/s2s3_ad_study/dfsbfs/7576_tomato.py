import sys
sys.stdin = open('ez_tomato.txt')
from collections import deque


temque = deque()
que = deque()
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
garo, sero = map(int, input().split())
base = [0]*sero
for se in range(sero):
    base[se] = list(map(int, input().split()))
visited = [[0]*garo for _ in range(sero)]

maxx = garo*sero
one = 0
empty = 0
zero = 0
for q in range(sero):
    for w in range(garo):
        if base[q][w] == 1:
            one += 1
            que.append((q, w))
        elif base[q][w] == 0:
            zero += 1
        elif base[q][w] == -1:
            empty += 1

phase = 0   # 회차 정보
temp = 999
kuku = 0
# base_copy = deepcopy(base)
if zero == maxx:    # 이미 최대일 때
    print(-1)
elif maxx == one + empty:
    print(0)
else:
    while que:  # 최대아닐때 회차 돌아감.
        phase += 1
        yai, ex = que.popleft()
        if que:
        visited[yai][ex] = 1
        spread(yai, ex)
        visited = [[0] * garo for _ in range(sero)]
    if maxx == one + empty:
        print(phase)
    else:
        print(-1)
