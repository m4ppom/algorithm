# def enQueue(Q):
#     global rear
#     if len(Q) == ??:
#         print('Full')
#     else:
#         rear += 1
#
# def deQueue(item):
#     global front
#     if len(Q) == 0:
#         return
#     else:
#         front += 1
#         return Q[front]

# candy = 20
# list_line = [0]*(candy*2)
# line = []
# book = []
# N = 1
# while candy != 0:
#     for i in range(N):
#         if len(book) == 0:
#             line.append([i, 0])
#             line[i][1] += 1
#             candy -= 1
#             continue
#         if len(book) >= i:
#             line.append(book[i])
#         else:
#             line.append([i, 0])
#         line[i][1] += 1
#         candy -= 1
#         print('llll',line)
#     a = line.pop(0)
#     book.append(a)
#     print('bbbbb', book)
#     N += 1

# import sys
# sys.stdin = open('inpu.txt', 'r')
#
# def sum(list):
#     result = 0
#     for i in list:
#         result += i
#     return result
#
# dqwdqwdqwd = input().split(',')
# # print(dqwdqwdqwd)
# N = len(set(dqwdqwdqwd))
# # print(set(dqwdqwdqwd))
# base = [[0 for _ in range(N+1)]for _ in range(N +1)]
# # print(base)
# # print(len(base))
# while len(dqwdqwdqwd) != 0:
#     b = dqwdqwdqwd.pop()
#     # print(b)
#     a = dqwdqwdqwd.pop()
#     # print(a)
#     base[int(a)][int(b)] = 1
#     base[int(b)][int(a)] = 1
# visited = [0]*(N+1)
# print(base)
# start = 1
# while sum(visited) != N:
#     count = 0
#     visited[start] = 1
#     print(start, end='-')
#     for i in range(2, N+1):
#         if visited[i] == 1:
#             start = i
#             print(start, end='-')
#
#
#         for j in range(1, N+1):
#             if base[start][j] == 1:
#                 count += 1
#         for j in range(1, N+1):
#
#             if base[start][j] == 1 and visited[j] == 0 and count != 0:
#                 count -= 1
#                 visited[j] = 1
#                 print(start, end='-')
#                 if count == 0:
#                     break
#             if base[start][j] == 1 and visited[j] == 0:
#                 count -= 1

# def bfs(g, v):
#     visited = [0]*N  # 노드의 개수
#     queue = []  # 큐 생성
#     queue.append(v)
#     while queue:
#         t = queue.pop(0)
#         if not visited[t]:
#             visited[t] = True
#             visit(t)
#         for i in g[t]:  # 연결된 모든 선
#             if not visited[i]:
#                 queue.append(i)

def bfs(x, y):




dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
testcase = int(input())
for test_num in range(testcase):
    N, M = map(int, input().split())






