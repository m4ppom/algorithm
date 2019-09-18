import sys
sys.stdin = open('minisum.txt', 'r')


def dfs(i, j, summ):
    global min_sum, N
    if summ > min_sum:
        return

    if i == N-1 and j == N-1:
        if min_sum > summ:
            min_sum = summ
        return

    for m in range(2):
        if -1< i+dy[m] < N and -1 < j+dx[m] < N:
            summ += base[i+dy[m]][j+dx[m]]
            dfs(i+dy[m], j+dx[m], summ)
            summ -= base[i+dy[m]][j+dx[m]]


dy = [1, 0]
dx = [0, 1]
testcase = int(input())
for test_num in range(1, testcase+1):
    N = int(input())
    base = [0]*N
    for i in range(N):
        base[i] = list(map(int, input().split()))
    min_sum = 99999
    first = base[0][0]
    dfs(0, 0, first)
    print('#%d %d'%(test_num, min_sum))