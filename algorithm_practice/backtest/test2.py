def dfs(i, j):
    global cnt, mini_cnt
    cnt += 1
    for t in range(4):
        iii = dy[t]+i
        jjj = dx[t]+j
        if -1 < iii < 10 and -1 < jjj < 10:
            if base[iii][jjj] == 9 or base[iii][jjj] == 0:
                dfs(iii, jjj)
                cnt -= 1
            else:
                cnt += 1
                base[iii][jjj] = 0
                if cnt < mini_cnt:
                    mini_cnt = cnt
                return


def bfs(i, j):
    visited = [[0]*10 for _ in range(10)]
    q = []
    visited[i][j] = 1
    q. append([i, j])
    while q:
        x = q.pop(0)
        a = x[0]
        b = x[1]

        for dir in range(4):
            if -1 < a+dy[dir] < 10 and -1 < b+dx[dir] < 10:
                if visited[a+dy[dir]][b+dx[dir]] == 0:
                    visited[a + dy[dir]][b + dx[dir]] = visited[a][b] + 1
                    if base[a+dy[dir]][b+dx[dir]] == 0 or base[a+dy[dir]][b+dx[dir]] == 9:
                        q.append([a+dy[dir], b+dx[dir]])
                    else:
                        base[a+dy[dir]][b+dx[dir]] = 0
                        return visited[a][b]


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
testcase = int(input())
for test_num in range(1, testcase+1):
    num = int(input())
    base =[0] * 10
    for i in range(10):
        base[i] = list(map(int, input().split()))
    count = 0
    for i in range(10):
        for j in range(10):
            if base[i][j] == 9:
                # mini_cnt = 11999
                # cnt = 0
                base[i][j] = 0
                # bfs(i, j)
                # dfs(i, j)
                count += bfs(i, j)

    print('#%d %d' %(test_num, count))