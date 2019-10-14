import sys
sys.stdin = open('organic.txt', 'r')

sys.setrecursionlimit(10000)  # 재귀 depth 초과하는거 뚫어줌
def dfs(aa, bb):  # 들어가면서 해당 칸 값을 0으로 바꿔주고 다음칸 찾아보면서 이동
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
    count = 0  # 벌레 수 
    for i in range(sero):
        for j in range(garo):
            if base[i][j] == 1:
                count += 1  # 새로운 배추지역 찾을 때 마다 벌레수 한마리씩 증가시킴
                dfs(i, j)
    print(count)
