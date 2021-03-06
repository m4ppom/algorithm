import sys

sys.stdin = open('inpu.txt', 'r')
sys.setrecursionlimit(1000000000)
# a = random.sample(range(10),2)
# print(a)
import time

st_time = time.time()

#
# import random
#
# def dfs(row, col):
#     global lele
#     if row == -1 or col ==-1 or row ==4 or col ==4:
#         return
#     lele.append(base[row][col])
#     if len(lele) == 7:
#         result.append(lele)
#         lele = []
#         # print(result)
#         return
#     else:
#         for i in random.sample(range(4), 1):
#             dfs(row + dy[i], col + dx[i])
#     return
#
#
# dy = [-1, 1, 0, 0]
# dx = [0, 0, -1, 1]
# testcase = int(input())
# for test_num in range(1, testcase+1):
#     base = [list(map(str, input().split()))for _ in range(4)]
#     result = []
#     timee = 0
#     while timee != 15000:
#         timee += 1
#         for i in range(4):
#             for j in range(4):
#                 lele = []
#                 dfs(i, j)
#         # print(result)
#     rere =[]
#     for i in range(len(result)):
#         a = ' '.join(result[i])
#         rere.append(a)
#     print('#{} {}'.format(test_num, len(set(rere))))

'''
def move(x, y, k, strin):
    global num_list, maze
    if k == 7:
        num_list.add(strin)
    else:
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < 4 and 0 <= new_y < 4:
                new_strin = strin + maze[new_x][new_y]
                move(new_x, new_y, k + 1, new_strin)


for tc in range(int(input())):
    maze = [list(map(str, input().split())) for _ in range(4)]
    num_list = set()  # 생성된 숫자들을 append
    for i in range(4):
        num_str = str()  # 붙인 숫자들을 이어줄 스트링
        for j in range(4):
            k = 0  # 카운트 후 7이 될 경우 출력
            # 숫자를 뺄 때마다 0으로 바뀌기에 하나를 복사해놓는다.
            move(i, j, k, num_str)

    print('#%d %d' % (tc + 1, len(num_list)))
'''


def dfs(x, y, k, n):
    global cnt
    global tc
    if k == 7:
        if visit[n] != tc:
            cnt += 1
            visit[n] = tc
        return

    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if tx < 0 or tx >= 4 or ty < 0 or ty >=  4:
            continue
        dfs(tx, ty, k + 1, n * 10 + data[tx][ty])


def dfs2(x, y, k, n):
    global cnt
    global tc
    if k == 7:
        if visit[n] != tc:
            cnt += 1
            visit[n] = tc
        return
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if tx == -1 or tx == 4 or ty == -1 or ty == 4:
            continue
        dfs(tx, ty, k+1, n*10+data[tx][ty])

T = int(input())
visit = [0] * 10000000
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for tc in range(1, T+1):
    data = [[0 for _ in range(4)] for _ in range(4)]
    cnt = 0
    for i in range(4):
        data[i] = list(map(int, input().split()))

    for i in range(4):
        for j in range(4):
            dfs(i, j, 1, data[i][j])

    print("#{} {}".format(tc, cnt))
print(time.time() - st_time)