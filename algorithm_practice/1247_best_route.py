import sys
import time
import copy
sys.setrecursionlimit(100000)

sys.stdin = open('inpu.txt', 'r')

st_time = time.time()

#
# def bfs(row, col):
#     global cl_num, count
#     q = []
#     if cl_num == client-1:
#         min1 = 100
#         idx1 = 0
#         min2 = 100
#         idx2 = 0
#         for i in range(client):
#             re1 = abs(sort_client_list[i][0] - start[0])
#             re2 = abs(sort_client_list[i][0] - end[0])
#             if re1 < min1:
#                 min1 = re1
#                 idx1 = i
#             if re2 < min2:
#                 min2 = re2
#                 idx2 = i
#         q.append(start)
#         base = [[0 for _ in range(101)] for _ in range(101)]
#         base[start[0]][start[1]] = 1
#         while len(q) != 0:
#             a = q.pop(0)
#             for i in range(4):
#                 row2 = a[0] + dy[i]
#                 col2 = a[1] + dx[i]
#                 if a[0] <= row2 <= sort_client_list[idx1][0] and a[1] <= col2 <= sort_client_list[idx1][1]:
#                     if base[row2][col2] == 0:
#                         q.append([row2, col2])
#                         base[row2][col2] = base[a[0]][a[1]] + 1
#                         continue
#                 if a[0] == sort_client_list[idx1][0] and a[1] == sort_client_list[idx1][1]:
#                     cl_num += 1
#                     count += base[row2][col2]
#             break
#         while len(q) != 0:
#             a = q.pop(0)
#             for i in range(4):
#                 row2 = a[0] + dy[i]
#                 col2 = a[1] + dx[i]
#                 if a[0] <= row2 <= sort_client_list[idx2][0] and a[1] <= col2 <= sort_client_list[idx2][1]:
#                     if base[row2][col2] == 0:
#                         q.append([row2, col2])
#                         base[row2][col2] = base[a[0]][a[1]] + 1
#                         continue
#                 if a[0] == sort_client_list[idx2][0] and a[1] == sort_client_list[idx2][1]:
#                     cl_num += 1
#                     count += base[row2][col2]
#             return
#
#     q.append([row, col])
#     base = [[0 for _ in range(101)] for _ in range(101)]
#     base[row][col] = 1
#     while len(q) != 0:
#         a = q.pop(0)
#         for i in range(4):
#             row2 = a[0] + dy[i]
#             col2 = a[1] + dx[i]
#             if row <= row2 <= sort_client_list[cl_num+1][0] and col <= col2 <= sort_client_list[cl_num+1][1]:
#                 if base[row2][col2] == 0:
#                     q.append([row2, col2])
#                     base[row2][col2] = base[a[0]][a[1]]+1
#             if a[0] == sort_client_list[cl_num+1][0] and a[1] == sort_client_list[cl_num+1][1]:
#                 cl_num += 1
#                 count += base[row2][col2]
#                 print('cccc', count)
#                 return
#     return


# def find_close(list):
#     global close1_index, close2_index
#     mini1 = 100
#     mini2 = 200
#     for i in range(client):
#         dis1 = abs(start[0] - sort_client_list[i][0]) + abs(start[1] - sort_client_list[i][1])
#         if dis1 < mini1:
#             mini1 = dis1
#             close1_index = i
#         dis2 = abs(end[0] - sort_client_list[i][0]) + abs(end[1] - sort_client_list[i][1])
#         if dis2 < mini2:
#             mini2 = dis2
#             close2_index = i
#     distance(start, sort_client_list[close1_index])
#     distance(end, sort_client_list[close2_index])
#     return


# def distance(cord1, cord2):
#     global count
#     # count += \
#     return abs(cord1[0] - cord2[0]) + abs(cord1[1] - cord2[1])
#
#
# def sorting(start):
#     global index, mini
#     mini = 200
#     # visited = [0 for _ in range(client)]
#     for a in range(len(client_list)):
#         # for j in range(i+1, client):
#         aa = distance(client_list[a], start)
#         if mini > aa:
#             mini = aa
#             index = a
#         # visited[index1] += 1
#
# dy = [-1, 1, 0, 0]
# dx = [0, 0, -1, 1]
# testcase = int(input())
# for test_num in range(1, testcase+1):
#     base = [[0 for _ in range(101)]for _ in range(101)]
#     client = int(input())
#     info = list(map(int, input().split()))
#     start = [info.pop(1), info.pop(0)]
#     end = [info.pop(0), info.pop(0)]
#     client_list = []
#     count = 0
#     index = 0
#     mini = 0
#     result = 0
#     for i in range(client):
#         client_list.append([info[2*i], info[2*i+1]])
#     while len(client_list):
#         sorting(start)
#         start = client_list.pop(index)
#         result += mini
#     result += distance(start, end)
#     print(result)

# sort_client_list = sorted(client_list)
# find_close(sort_client_list)
# for i in range(client-1):
#     distance(sort_client_list[i], sort_client_list[i+1])
# sorting(client_list)
# # print(client_list)
# print(sort_client_list)
# print(count)
# cl_num = 0
# while cl_num != client-1:
#     # cl_num += 1
#     bfs(sort_client_list[cl_num][0], sort_client_list[cl_num][1])
#     print(cl_num)
# print(count)


def distance(cord1, cord2):
    return abs(cord1[0] - cord2[0]) + abs(cord1[1] - cord2[1])


def dfs(start, end):
    global mini, cnt, result, client_number
    if visited[start][end] == 1 or start == end or end <= start or vivi[start] == 1:
        return
    visited[start][end] = 1
    # vivi[end] = 1
    result += base[start][end]
    cnt += 1
    if cnt == client_number+1:
        if mini > result:
            mini = result
            result -= base[start][end]
            cnt -= 1
            vivi[start] = 0
            return
    for i in range(client_number):
        dfs(end, i)
    result -= base[start][end]
    cnt -= 1
    return


testcase = int(input())
for test_num in range(1, testcase+1):
    client_number = int(input())
    info = list(map(int, input().split()))
    client_list = []
    for i in range(client_number+2):
        client_list.append([info[2*i], info[2*i+1]])
    print(client_list)
    base = [[0]*(client_number+2) for i in range(client_number+2)]
    for i in range(client_number+2):
        for j in range(client_number+2):
            base[i][j] = distance(client_list[i], client_list[j])
    result = 0
    mini = 10000
    cnt = 0
    visited = [[0]*(client_number+2) for _ in range(client_number+2)]
    vivi = [0]*(client_number+2)
    for i in range(client_number+2):
        for j in range(client_number+2):
            dfs(i, j)
            print(mini)
    # print(base)
print(time.time() - st_time)