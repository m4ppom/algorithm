import sys
sys.stdin = open('coin.txt', 'r')

sys.setrecursionlimit(100000)

import collections
def findcoin(i, namundon):
    global cnt, N, mini
    if cnt > mini:
        return
    # print(i)
    if namundon == 0:
        if cnt < mini:
            mini = cnt
        return
    for hhhh in range(i, -1, -1):
        num = namundon // q[hhhh]
        num_nam = K % q[hhhh]
        if num == 0:
            continue
        else:
            cnt += num
            findcoin(hhhh, num_nam)
            cnt -= num


N, K = map(int, input().split())
q = collections.deque()
for i in range(N):
    q.append(int(input()))
mini = 10000000000000
cnt = 0
findcoin(N-1, K)
print(mini)