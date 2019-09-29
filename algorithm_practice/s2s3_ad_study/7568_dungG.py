import sys
sys.stdin = open('dungG.txt', 'r')

import collections
rank = collections.deque()
N = int(input())
people = [0]*N
fight = [[0]*N for _ in range(N)]
for i in range(N):
    people[i] = list(map(int, input().split()))
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        else:
            if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
                fight[i][j] = 1
for i in range(N):
    rank.append(sum(fight[i]))
ranking = 1
visited = [0]*N
cnt = 0
for i in range(N):
    print(rank[i]+1, end=' ')


