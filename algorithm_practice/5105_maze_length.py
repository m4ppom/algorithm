import sys
sys.stdin = open('input0902.txt', 'r')


dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]


def dfs(y, x):
    global cnt
    global end
    t = 0

    while t != 100000:
        t += 1
        bzted[y][x] = 1
        for i in range(4):
            if y+dy[i] == N or x+dx[i] == N or x+dx[i] < 0 or y+dy[i] < 0 or bzted[y+dy[i]][x+dx[i]] == 1 or end == 1:
                continue
            elif base[y+dy[i]][x+dx[i]] == 3:
                cnt_list.append(cnt)
                cnt = 0
                end = 1
                return
            elif base[y+dy[i]][x+dx[i]] == 0 and bzted[y+dy[i]][x+dx[i]] == 0:
                cnt += 1
                bzted[y+dy[i]][x+dx[i]] = 1
                dfs(y+dy[i], x+dx[i])
        if end == 1 and base[y+dy[3]][x+dx[3]] == 1 and base[y+dy[2]][x+dx[2]] == 1 and base[y+dy[0]][x+dx[0]] == 1 and base[y+dy[1]][x+dx[1]] == 1:
            return
        else:
            cnt = 0
            return
        # print(cnt)


dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
testcase = int(input())
for test_num in range(1, testcase+1):
    N = int(input())
    base = [0] * N
    for i in range(N):
        base[i] = list(map(int, input()))
    for i in range(N):
        for j in range(N):
            if base[i][j] == 2:
                y = i
                x = j
    bzted = [[0 for _ in range(N)]for _ in range(N)]
    end = 0
    cnt_list = []
    cnt = 0
    dfs(y, x)
    # print(cnt_list)
    if cnt_list:
        print('#{} {}'.format(test_num, min(cnt_list)))
    else:
        print('#{} {}'.format(test_num, cnt))