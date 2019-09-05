import sys
sys.stdin = open('inpu.txt', 'r')
import copy

# def direc(direction):
#     global N
#     global base_copy
#     base_copy = copy.deepcopy(base)
#     if direction == 'up':
#         d = 0
#     elif direction == 'down':
#         d = 1
#     elif direction == 'left':
#         d = 2
#     else:  # 오른쪽
#         d = 3
#     if d == 0:  # 위 할때 합치기
#         # for i in range(N):
#         #     for j in range(N):
#         #         if -1 < i + dy[d] < N and -1 < j + dx[d] < N:
#         #             for mux in range(1, N+1):
#         #                 if not -1 < i + mux * dy[d] < N or not -1 < j + mux * dx[d] < N:
#         #                     break
#         #                 else:
#         #
#
#
#
#         for i in range(N):
#             for j in range(N):
#                 if -1 < i + dy[d] < N and -1 < j + dx[d] < N:
#                     mux = 1
#                     while 1:
#                         if not -1 < i + mux * dy[d] < N or not -1 < j + mux * dx[d] < N:
#                             break
#                         if base[i][j] == base[i + mux * dy[d]][j + mux * dx[d]] and visited[i + mux * dy[d]][
#                             j + mux * dx[d]] == 0:
#                             base_copy[i][j] = 0
#                             visited[i + mux * dy[d]][j + mux * dx[d]] = visited[i][j] = 1
#                             base_copy[i + mux * dy[d]][j + mux * dx[d]] *= 2
#                             break
#                         elif base[i + mux * dy[d]][j + mux * dx[d]] == 0 and visited[i + mux * dy[d]][j + mux * dx[d]] == 0:
#                             mux += 1
#                         else:
#                             break
#                 else:
#                     continue
#         # print(base_copy)
#         # print('ddasdasdasd')
#         for i in range(N):
#             for j in range(N):
#                 if -1 < i + dy[d] < N and -1 < j + dx[d] < N:
#                     mux = 1
#                     while 1:
#                         if not -1 < i + mux * dy[d] < N or not -1 < j + mux * dx[d] < N:
#                             break
#                         elif base_copy[i + mux * dy[d]][j + mux * dx[d]] == 0:
#                             #     visited[i + mux * dy[d]][j + mux * dx[d]] = visited[i][j] = 1
#                             a = i
#                             b = j
#                             while -1 < a + mux * dy[d] < N or not -1 < b + mux * dx[d] < N:
#                                 if base_copy[a + mux * dy[d]][b + mux * dx[d]] == 0:
#                                     base_copy[a + mux * dy[d]][b + mux * dx[d]] = base_copy[a][b]
#                                     base_copy[a][b] = 0
#                                     a += mux * dy[d]
#                                     b += mux * dx[d]
#                                     # mux += 1
#                                 else:
#                                     break
#                             break
#                         else:
#                             break
#                 else:
#                     continue
#     elif d == 2:  # left
#         for i in range(N):
#             for j in range(N):
#                 if -1 < i + dy[d] < N and -1 < j + dx[d] < N:
#                     mux = 1
#                     while 1:
#                         if not -1 < i + mux * dy[d] < N or not -1 < j + mux * dx[d] < N:
#                             break
#                         if base[i][j] == base[i + mux * dy[d]][j + mux * dx[d]] and visited[i + mux * dy[d]][
#                             j + mux * dx[d]] == 0:
#                             base_copy[i][j] = 0
#                             visited[i + mux * dy[d]][j + mux * dx[d]] = visited[i][j] = 1
#                             base_copy[i + mux * dy[d]][j + mux * dx[d]] *= 2
#                             break
#                         elif base[i + mux * dy[d]][j + mux * dx[d]] == 0 and visited[i + mux * dy[d]][j + mux * dx[d]] == 0:
#                             mux += 1
#                         else:
#                             break
#                 else:
#                     continue
#         # print(base_copy)
#         # print('ddasdasdasd')
#         for i in range(N):
#             for j in range(N):
#                 if -1 < i + dy[d] < N and -1 < j + dx[d] < N:
#                     mux = 1
#                     while 1:
#                         if not -1 < i + mux * dy[d] < N or not -1 < j + mux * dx[d] < N:
#                             break
#                         elif base_copy[i + mux * dy[d]][j + mux * dx[d]] == 0:
#                             #     visited[i + mux * dy[d]][j + mux * dx[d]] = visited[i][j] = 1
#                             a = i
#                             b = j
#                             while -1 < a + mux * dy[d] < N or not -1 < b + mux * dx[d] < N:
#                                 if base_copy[a + mux * dy[d]][b + mux * dx[d]] == 0:
#                                     base_copy[a + mux * dy[d]][b + mux * dx[d]] = base_copy[a][b]
#                                     base_copy[a][b] = 0
#                                     a += mux * dy[d]
#                                     b += mux * dx[d]
#                                     # mux += 1
#                                 else:
#                                     break
#                             break
#                         else:
#                             break
#                 else:
#                     continue
#     elif d == 3:
#         for i in range(N):
#             for j in range(N, -1, -1):
#                 if -1 < i + dy[d] < N and -1 < j + dx[d] < N:
#                     mux = 1
#                     while 1:
#                         if not -1 < i + mux * dy[d] < N or not -1 < j + mux * dx[d] < N:
#                             break
#                         if base[i][j] == base[i + mux * dy[d]][j + mux * dx[d]] and visited[i + mux * dy[d]][
#                             j + mux * dx[d]] == 0:
#                             base_copy[i][j] = 0
#                             visited[i + mux * dy[d]][j + mux * dx[d]] = visited[i][j] = 1
#                             base_copy[i + mux * dy[d]][j + mux * dx[d]] *= 2
#                             break
#                         elif base[i + mux * dy[d]][j + mux * dx[d]] == 0 and visited[i + mux * dy[d]][j + mux * dx[d]] == 0:
#                             mux += 1
#                         else:
#                             break--
#                 else:
#                     continue
#         # print(base_copy)
#         # print('ddasdasdasd')
#         for i in range(N):
#             for j in range(N, -1, -1):
#                 if -1 < i + dy[d] < N and -1 < j + dx[d] < N:
#                     mux = 1
#                     while 1:
#                         if not -1 < i + mux * dy[d] < N or not -1 < j + mux * dx[d] < N:
#                             break
#                         elif base_copy[i + mux * dy[d]][j + mux * dx[d]] == 0:
#                             #     visited[i + mux * dy[d]][j + mux * dx[d]] = visited[i][j] = 1
#                             a = i
#                             b = j
#                             while -1 < a + mux * dy[d] < N or not -1 < b + mux * dx[d] < N:
#                                 if base_copy[a + mux * dy[d]][b + mux * dx[d]] == 0:
#                                     base_copy[a + mux * dy[d]][b + mux * dx[d]] = base_copy[a][b]
#                                     base_copy[a][b] = 0
#                                     a += mux * dy[d]
#                                     b += mux * dx[d]0
#                                     # mux += 1
#                                 else:
#                                     break
#                             break
#                         else:
#                             break
#                 else:
#                     continue
#     else:
#         for i in range(N, -1, -1):
#             for j in range(N, -1, -1):
#                 if -1 < i + dy[d] < N and -1 < j + dx[d] < N:
#                     mux = 1
#                     while 1:
#                         if not -1 < i + mux * dy[d] < N or not -1 < j + mux * dx[d] < N:
#                             break
#                         if base[i][j] == base[i + mux * dy[d]][j + mux * dx[d]] and visited[i + mux * dy[d]][
#                             j + mux * dx[d]] == 0:
#                             base_copy[i][j] = 0
#                             visited[i + mux * dy[d]][j + mux * dx[d]] = visited[i][j] = 1
#                             base_copy[i + mux * dy[d]][j + mux * dx[d]] *= 2
#                             break
#                         elif base[i + mux * dy[d]][j + mux * dx[d]] == 0 and visited[i + mux * dy[d]][j + mux * dx[d]] == 0:
#                             mux += 1
#                         else:
#                             break
#                 else:
#                     continue
#         # print(base_copy)
#         # print('ddasdasdasd')
#         for i in range(N, -1, -1):
#             for j in range(N, -1, -1):
#                 if -1 < i + dy[d] < N and -1 < j + dx[d] < N:
#                     mux = 1
#                     while 1:
#                         if not -1 < i + mux * dy[d] < N or not -1 < j + mux * dx[d] < N:
#                             break
#                         elif base_copy[i + mux * dy[d]][j + mux * dx[d]] == 0:
#                             #     visited[i + mux * dy[d]][j + mux * dx[d]] = visited[i][j] = 1
#                             a = i
#                             b = j
#                             while -1 < a + mux * dy[d] < N or not -1 < b + mux * dx[d] < N:
#                                 if base_copy[a + mux * dy[d]][b + mux * dx[d]] == 0:
#                                     base_copy[a + mux * dy[d]][b + mux * dx[d]] = base_copy[a][b]
#                                     base_copy[a][b] = 0
#                                     a += mux * dy[d]
#                                     b += mux * dx[d]
#                                     # mux += 1
#                                 else:
#                                     break
#                             break
#                         else:
#                             break
#                 else:
#                     continue
#
#     # print(base_copy)
    # print('ssssssssssss')
def direc(base):
    global direction
    # base_copy = copy.deepcopy(base)
    if direction == 'up':  # 계산
        for i in range(N):
            for j in range(N):
                multi = 1
                # if -1 < i + multi*dy[0] < N:
                while -1 < i + multi*dy[0] < N:
                    if base[i + multi*dy[0]][j] == base[i][j] and visited[i][j] == 0:
                        base[i + multi*dy[0]][j] *= 2
                        visited[i][j] = 1
                        base[i][j] = 0
                        break
                    if base[i + multi*dy[0]][j] == 0:
                        multi += 1
                    else:
                        break
        base_copy = copy.deepcopy(base)
        print(base_copy)
        for i in range(N):
            for j in range(N):
                if base_copy[i][j] == 0:
                    continue
                else:
                    multi = 1
                    while -1 < i + multi * dy[0] < N:
                        if base_copy[i + multi * dy[0]][j] == 0:
                            base_copy[i + multi * dy[0]][j] = base_copy[i + (multi-1) * dy[0]][j]
                            base_copy[i + (multi - 1) * dy[0]][j] = 0
                            multi += 1
                        else:
                            break
        print('basesa',base_copy)
        

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
testcase = int(input())
for test_num in range(1, testcase+1):
    N, direction = map(str, input().split())
    N = int(N)
    base = [0]*N
    base_copy = []
    visited = [[0 for _ in range(N)]for _ in range(N)]
    for i in range(N):
        base[i] = list(map(int, input().split()))
    # print(base)
    direc(base)
    # print(base_copy)
    print('#{}'.format(test_num))
    for i in range(len(base_copy)):
        for j in range(N):
            print(base_copy[i][j],end=' ')
        print()
