import sys
sys.stdin = open("input0828.txt", "r")

def bfs(start):
    result = -1
    finding = -1
    # r = 0
    link = -1
    link += 1
    level[link] = start
    visited[start] = 1
    link += 1
    level[link] = -1  # 레벨의 경계선
    # print(base)
    # print(visited)

    while 1:
        finding += 1
        # print('f',finding,'r',link)
        start = level[finding]
        # print('level', level)
        # print('start',start)
        if result < start:  # 레벨값 최대 바꾸기
            result = start
        if start == -1:
            if finding == link:
                return result
            link += 1
            result = 0
            level[link] = -1
            continue

        for i in range(base[start][0]):
            if visited[base[start][i + 1]] == 0:
                visited[base[start][i + 1]] = 1
                link += 1
                level[link] = base[start][i + 1]

for testcase in range(1, 2):
    node, start = map(int, input().split())
    level = [0] * node
    visited = [0] * (node+1)
    base = [[0] * node for i in range(node+1)]
    link = list(map(int, input().split()))
    while len(link) != 0:
        b = link.pop()
        a = link.pop()
        base[a][0] += 1
        base[a][base[a][0]] = b
    print('#{} {}'.format(testcase, bfs(start)))
    # print(level)


# def dfs(start):
#     global result
#     global cnt
#
#     # if len(result) == num_ver:
#     #     return
#     visited[start] = 1
#     # if start not in result:
#     #     result += [start]
#     for next in range(1, num_ver + 1):
#         # if True not in parent:
#         #     return
#         if start == next:
#             continue
#         elif link_cord[start][next] and not visited[next]:
#             # parent[next] -= 1
#             link_cord[start][next] += visited[start]
#             # if parent[next] == 0:
#             #     result += [next]
#             visited[next] += 1
#             dfs(next)
#
#
#
# test_case = 10
# for number in range(1, test_case + 1):
#     result = 0
#     num_ver, start = map(int, input().split())  # vortex & edge 개tn
#
#     link_cord = [[0 for _ in range(num_ver + 1)] for _ in range(num_ver + 1)]
#     visited = [0] * (num_ver + 1)
#     parent = [0] * (num_ver + 1)  # 미리 마쳐야 하는 vortex
#
#     link = list(map(int, input().split()))
#     while len(link) != 0:
#         b = link.pop()
#         a = link.pop()
#         link_cord[a][b] = 1
#         parent[b] += 1
#     # for i in range(1, num_ver + 1):
#     #     if visited[i] == 1:
#     #         continue
#     #     if parent[i] == 0:
#     cnt = 1
#     dfs(start)
#     maxi = []
#     for i in range(num_ver + 1):
#         for j in range(num_ver + 1):
#             if link_cord[i][j] > result:
#                 result = link_cord[i][j]
#                 maxi += [j]
#     print(visited)
#     # print(link_cord)
#     print('#{} {}'.format(number, maxi))
#     # print('#{}'.format(number), end=' ')
#     # for i in result:
#     #     print('{}'.format(i), end=' ')
#     # print()
