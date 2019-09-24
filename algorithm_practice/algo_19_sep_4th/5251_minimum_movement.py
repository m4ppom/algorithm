import sys
sys.stdin=open('minimummove.txt')
def finder(start):
    global N, summ, mini
    if summ > mini:
        return
    if start == N:
        if mini > summ:
            mini = summ
        return
    for i in range(N+1):
        if base[start][i] != 0 and visited[i] == 0:
            visited[i] = 1
            summ += base[start][i]
            finder(i)
            summ -= base[start][i]
            visited[i] = 0


testcase = int(input())
for test_num in range(1, testcase + 1):
    N, M = map(int, input().split())
    base=[[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        base[a][b] = c
    mini = 20000
    visited = [0]*(N+1)
    summ = 0
    visited[0] = 1
    finder(0)
    print('#%d %d' % (test_num, mini))