def pathfinder(i, j, h):
    global mini, mini_height, mini_list
    summ = 0
    for aaa in range(N):
        summ += abs(base[i][aaa] - h)
    for bbb in range(N):
        summ += abs(base[bbb][j] - h)
    summ -= abs(base[i][j] - h)
    summ = abs(summ)
    if mini > summ:
        mini_list = []
        mini = summ
        mini_list.append(h)
    if mini == summ:
        mini_list.append(h)

testcase = int(input())
for test_num in range(1, testcase+1):
    N = int(input())
    base = [0] * N
    for i in range(N):
        base[i] = list(map(int, input().split()))
    mini = 9999999
    mini_height = 999999
    mini_list = []
    for i in range(N):
        for j in range(N):
            for h in range(1, 6):  # 1~5까지 높이일떄 다계산
                pathfinder(i, j, h)
    mini_height = min(mini_list)
    print('#%d %d %d' %(test_num, mini, mini_height))