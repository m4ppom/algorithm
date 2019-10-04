import sys
sys.stdin = open('printer_q.txt', 'r')

import collections
testcase = int(input())
for test_num in range(1 , testcase+1):
    N, M = map(int, input().split())
    visited = collections.deque()
    q = [0]
    for i in range(1, N+1):
        visited.append(i)
    # q = collections.deque()
    for j in list(map(int, input().split())):
        q.append(j)
    cnt = 1
    while visited:
        a = visited.popleft()
        for number in q:
            if number > q[a]:
                visited.append(a)
                break
        else:
            if a == M + 1:
                print(cnt)
                break
            else:
                cnt += 1
                q[a] = 0