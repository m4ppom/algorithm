import sys
sys.stdin = open('divgr.txt', 'r')


def finder(i):
    if visit[i] == 0:
        visit[i] = num
    for a in range(1, N+1):
        if base[i][a] == 1 and visit[a] == 0:
            finder(a)


testcase = int(input())
for test_num in range(1, testcase+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    base = [[0]*(N+1) for _ in range(N+1)]
    while lst:
        a = lst.pop(0)
        b = lst.pop(0)
        base[a][b] = 1
        base[b][a] = 1
    num = 1
    visit = [0]*(N+1)
    for i in range(1, N+1):
        finder(i)
        num += 1
    print('#%d %d' %(test_num, len(set(visit))-1))
