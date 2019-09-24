import sys
sys.stdin = open('mst.txt', 'r')


def pathfinder(a):
    global N, gajungchi, link, mini
    if gajungchi > mini:
        return
    if link == N:
        if mini > gajungchi:
            mini = gajungchi
        return
    for i in range(N+1):
        if base[a][i] != 0 and visit[i] == 0:
            gajungchi += base[a][i]
            link += 1
            visit[i] = 1
            pathfinder(i)
            if link == N-1:
                for aaa in range(N+1):
                    if base[a][aaa] != 0 and visit[aaa] == 0:
                        gajungchi += base[a][aaa]
                        link += 1
                        visit[aaa] = 1
                        pathfinder(aaa)
                        link -= 1
                        visit[aaa] = 0
                        gajungchi -= base[a][aaa]
            link -= 1
            visit[i] = 0
            gajungchi -= base[a][i]


testcase = int(input())
for test_num in range(1, testcase+1):
    N, M = map(int, input().split())
    base = [[0]*(N+1)for _ in range(N+1)]
    for i in range(M):
        a, b, ga = map(int, input().split())
        base[a][b] = ga
        base[b][a] = ga
    mini = 999999
    for i in range(N+1):
        visit = [0]*(N+1)
        link = 0
        gajungchi = 0
        visit[i] = 1
        pathfinder(i)
    print('#%d %d' %(test_num, mini))