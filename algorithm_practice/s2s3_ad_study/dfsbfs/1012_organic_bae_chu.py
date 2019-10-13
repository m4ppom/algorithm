import sys
sys.stdin = open('organic.txt', 'r')

sys.setrecursionlimit(10000)
def dfs(aa, bb):
    global garo, sero
    base[aa][bb] = 0
    for dir in range(4):
        aaa = aa + dy[dir]
        bbb = bb + dx[dir]
        if -1 < aaa < sero and -1 < bbb < garo:
            if base[aaa][bbb] == 1:
                dfs(aaa, bbb)


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
testcase = int(input())
for test_num in range(testcase):
    garo, sero, baechu = map(int, input().split())
    base = [[0]*garo for i in range(sero)]
    for _ in range(baechu):
        a, b = map(int, input().split())
        base[b][a] = 1
    count = 0
    for i in range(sero):
        for j in range(garo):
            if base[i][j] == 1:
                count += 1
                dfs(i, j)
    print(count)
