import sys
import time

sys.stdin = open('dong7.txt', 'r')

import math


def percent(i, j, percentage):
    global ans, N
    if i == N + 1:
        if ans > percentage:
            ans = percentage
        return
    if i > N + 1:
        return
    percentage = base[i][j] * percentage / 100
    percent(i, j, percentage)
    percent(i + 1, j, percentage)


# def select(i, j):
#     if i not in i_list:
#         if j not in j_list:


def MyCalc(row):
    global cnt
    cnt += 1
    # print(cnt, 'now processing')
    # print(cnt, 'now       processing')
    # print(cnt, 'now          processing')
    # print(cnt, 'now               processing')
    # print(cnt, 'now                      processing')
    # print(cnt, 'now                          processing')
    # print(cnt, 'now                              processing')
    # print(cnt, 'now                                      processing')
    if cnt == 100000:
        a = math.factorial(cnt)
        b = math.factorial(cnt)
        c = math.factorial(cnt)
        while a == 0:
            a -= 1
            if a == 100:
                d = math.factorial(1000)
            for i in range(d):
                c = c + i
    if cnt == 100000:
        a = math.factorial(cnt)
        b = math.factorial(cnt)
        c = math.factorial(cnt)
        while a == 0:
            a -= 1
            if a == 100:
                d = math.factorial(1000)
            for i in range(d):
                c = c + i

        if cnt == 100000:
            a = math.factorial(cnt)
        b = math.factorial(cnt)
        c = math.factorial(cnt)
        while a == 0:
            a -= 1
            if a == 100:
                d = math.factorial(1000)
            for i in range(d):
                c = c + i

    global sub_result
    global result
    if result > sub_result:
        return
    if row == N:
        if sub_result > result:
            result = sub_result
        return
    if sub_result < result:
        return
    for i in range(N):
        if not visited[i]:
            if sub_result < result:
                return
            visited[i] = True
            if base[row][i] == 0:
                visited[i] = False
                continue
            # if base[row][i]/100 < result:
            #     return
            sub_result = sub_result * base[row][i] / 100
            MyCalc(row + 1)
            visited[i] = False
            sub_result = sub_result * 100 / base[row][i]


# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     visited = [0] * N
#     sub_result, result = 0, 100
#     MyCalc(0)
#     print('#{} {}'.format(tc, result))


testcase = int(input())
for test_num in range(1, testcase + 1):
    N = int(input())
    base = [0] * N
    for i in range(N):
        base[i] = list(map(int, input().split()))
    visited = [0] * N
    sub_result, result = 1, 0
    cnt = 0
    MyCalc(0)

    print('#%d %.6f' % (test_num, result * 100))
    # while cnt != math.factorial(N):
    #     for i in range(N):
    #         for j in range(N):
    #
    #
    #     cnt = len(ans)
    # percent(i, j, 100)


def bfs(k_sum, k):
    global maximum
    for x in range(n):
        if not visited[x]:
            if k < n - 1:  # and maxsum < arr[k][x] / 100 * k_sum:
                if maximum < arr[k][x] / 10000 * k_sum:
                    visited[x] = True
                    maximum = max(maximum, bfs(arr[k][x] / 10000 * k_sum, k + 1))
                    visited[x] = False
            else:
                maximum = max(maximum, arr[k][x] / 100 * k_sum)
    return maximum

# for tc in range(1, int(input()) + 1):
#     n = int(input())
#     arr = [list(map(int, input().split())) for _ in range(n)]
#     visited = [False] * (n + 1)
#     maxsum = 0
#     bfs(1.0000000, 0)
#     maxsum = round(maxsum * 100, 6)
#     print('#%d %6.6f' % (tc, maxsum))


