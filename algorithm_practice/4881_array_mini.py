import sys
sys.stdin = open('inpu.txt', 'r')


def ezwall(x):
    global N
    if x > N-1:
        return False
    return 1


def dfs(i, j):
    global cnt
    global meme
    global summing
    summing += base[i][j]
    print('asdadasd',base[i][j])
    cnt += 1
    dx = [1, -1, 1, -1]
    dy = [1, -1, -1, 1]
    for a in range(4):
        if ezwall(i+dy[a]) == True and ezwall(j+dx[a]) == True:
            # print('ez', i+dy[a], j+dx[a])
            meme = [[0,0] for _ in range(N)]
            meme[cnt-1] = [i, j]
            for nnn in range(N):
                for mmm in range(nnn, N):
                    if meme[nnn][0] == meme[mmm][0] or meme[nnn][1] == meme[mmm][1]:
                        continue
                    else:
                        dfs(i+dy[a], j+dx[a])


    # global N
    # global cnt
    # global summing
    # print('새로운 시작 new era',i, j)
    # visited[i][j] = 1
    # for mm in range(N):
    #     visited[mm][j] = 1
    #     visited[i][mm] = 1
    # cnt += 1
    # print(cnt,'<--카운트 더하는주우우우웅')
    # summing += base[i][j]
    # if cnt == N:
    #     cnt = 0
    #     print('3333333333333333333333')
    #     return
    # # cnt += 1
    # # print('더하는주우우우웅')
    # # summing += base[i][j]
    # for a in range(N):
    #     for b in range(N):
    #         if visited[a][b] == 1:
    #             continue
    #         else:
    #             print(a, b)
    #             dfs(a, b)


testcase = int(input())
for test_num in range(1, testcase + 1):
    result = 1000
    summing = 0
    N = int(input())
    # visited = [[[0 for _ in range(N)]for _ in range(N)]for _ in range(N)]
    base = [0] * N
    cnt = 0
    for i in range(N):
        base[i] = list(map(int, input().split()))
    for i in range(N):
        for j in range(N):
            summing = 0
            cnt = 0
            dfs(i, j)
            if summing < result:
                # print(i,j)
                # print('rrrrr',result,'sssss',summing)
                result = summing
                summing = 0
                # visited = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(N)]
    print('#{} {}'.format(test_num, result))
    # print(visited)