import collections


def dfs(i, j):
    global mini_dis, distan
    if i >= 5:
        if mini_dis > distan:
            mini_dis = distan
    if mini_dis < distan:
        return
    for aaa in range(6):
        if visited[aaa] != 0:
            continue
        else:
            visited[aaa] = 1
            distan += distance[i+1][aaa]
            dfs(i+1, aaa)
            distan -= distance[i + 1][aaa]
            visited[aaa] = 0


testcase = int(input())
for test_num in range(1, testcase + 1):
    num = int(input())
    base = [0] * 10
    robo_list = collections.deque()
    cookie_list = collections.deque()
    mini_dis = 1000000
    for i in range(10):
        base[i] = list(map(int, input().split()))
    for i in range(10):
        for j in range(10):
            if base[i][j] == 9:
                base[i][j] = 0
                robo_list.append([i, j])
            elif base[i][j] != 0:
                base[i][j] = 0
                cookie_list.append([i, j])
    distance = [[0]*6 for _ in range(6)]
    for i in range(6):
        for j in range(6):
            distance[i][j] = abs(robo_list[i][0] - cookie_list[j][0]) + abs(robo_list[i][1]-cookie_list[j][1])
    for i in range(6):
        visited = [0] * 6
        visited[i] = 1
        distan = distance[0][i]
        dfs(0, i)
    print('#%d %d' %(test_num, mini_dis))

