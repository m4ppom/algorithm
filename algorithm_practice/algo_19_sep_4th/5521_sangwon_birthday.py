import sys
sys.stdin = open('birth.txt', 'r')


def bfs(start):
    global ans
    q = []
    q.append(start)
    visited = [0]*(N+1)
    visited[start] = 1
    cnt = 1
    while q:
        a = q.pop(0)
        for i in range(1, N+1):
            if base[a][i] and visited[i] == 0:
                q.append(i)
                visited[i] += cnt
                cnt += 1
                ans += 1
                if cnt == 3:
                    cnt = 0
    return


def dfs(s):
    global cnt, ans
    if cnt == 3:
        return
    if v[s] == 0:
        ans += 1
        v[s] = 1
    # for i in range(1, N+1):
    for i in range(1, 501):
        if base[s][i] == 1:
            cnt += 1
            dfs(i)
            cnt -= 1

import copy
# bases = [[0]*501for _ in range(501)]
# visited = [0]*501
testcase = int(input())
for test_num in range(1, testcase+1):
    N, M = map(int, input().split())
    base = [[0] * 501 for _ in range(501)]
    # base = [[0]*(N+1)for _ in range(N+1)]
    for i in range(M):
        a, b = map(int, input().split())
        base[a][b] = 1
        base[b][a] = 1
    v = [0] * 501
    # v = [0]*(N+1)
    cnt = 0
    ans = -1
    dfs(1)
    print('#%d %d' %(test_num, ans))


