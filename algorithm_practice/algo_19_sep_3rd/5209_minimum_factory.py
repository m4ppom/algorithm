import sys
import copy
sys.stdin = open('mini.txt', 'r')

#
# def finding_mini(deep, x):
#     global summ
#
#     summ += base[deep][x]
#
#
# testcase = int(input())
# for test_num in range(1, testcase+1):
#     N = int(input())
#     base = [0]*N
#     visit = copy.deepcopy(base)
#     for i in range(N):
#         base[i] = list(map(int, input().split()))
#
#     for i in range(N):
#         summ = 0
#         visit[i-1] = 1
#         summ += base[0][i]
#         finding_mini(0, i)
#         visit[i-1] = 0

def MyCalc(row):
    global sub_result
    global result
    if result < sub_result:
        return
    if row == N:
        if sub_result < result:
            result = sub_result
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            sub_result += arr[row][i]
            MyCalc(row + 1)
            visited[i] = False
            sub_result -= arr[row][i]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    sub_result, result = 0, 1000000
    MyCalc(0)
    print('#{} {}'.format(tc, result))