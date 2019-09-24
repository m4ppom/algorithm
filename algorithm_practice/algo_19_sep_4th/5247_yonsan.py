import sys
sys.stdin = open('yonsan.txt')
sys.setrecursionlimit(100000)

import collections

testcase = int(input())
for test_num in range(1, testcase + 1):
    N, M = map(int, input().split())
    visited = [0] * 1000001
    queue = collections.deque()
    queue.append(N)
    temp = 0
    de = 0
    while queue:
        de += 1
        for _ in range(len(queue)):
            c = queue.popleft()
            # print(c)
            for i in range(4):
                if i == 0:
                    temp = c + 1
                elif i == 1:
                    temp = c - 1
                elif i == 2:
                    temp = c - 10
                elif i == 3:
                    temp = c * 2
                if 0 < temp < 1000001:
                    if visited[temp] == 0:
                        if temp == M:
                            break
                        queue.append(temp)
                        visited[temp] = 1
            if temp == M:
                break
        if temp == M:
            break
    print('#{} {}'.format(test_num, de))


# def calcu(number):
#     global M, ans, cnt
#     if cnt > ans or number > M+20:
#         return
#     if number == M:
#         if ans > cnt:
#             ans = cnt
#         return
#     if number < 1:
#         return
#     if M // number > 2:
#         number *= 2
#         cnt += 1
#         calcu(number)
#         cnt -= 1
#         number //= 2
#
#     for i in range(4):
#         if i == 0:
#             number += 1
#         elif i == 1:
#             number -= 10
#         elif i == 2:
#             number *= 2
#         elif i == 3:
#             number -= 1
#         cnt += 1
#         calcu(number)
#         cnt -= 1
#         if i == 0:
#             number -= 1
#         elif i == 1:
#             number += 10
#         elif i == 2:
#             number //= 2
#         elif i == 3:
#             number += 1
#
#
# def finder(number):
#     global go
#
#     if number > 10 and go == 0:
#         number -= 10
#         go = 1
#         finder(number)
#     if M > 2*number:
#         number *= 2
#         finder(number)
#
#
# testcase = int(input())
# for test_num in range(1, testcase + 1):
#     ans = 20
#     cnt = 0
#     N, M = map(int, input().split())
#     calcu(N)
#     print('#%d %d' %(test_num,ans))
