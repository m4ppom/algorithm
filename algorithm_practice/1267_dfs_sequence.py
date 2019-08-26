import sys 
sys.stdin = open("1267_dfs_sequence", "r")


def dfs(start):
    global result

    if len(result) == num_ver:
        return
    visited[start] = 1
    if start not in result:
        result += [start]
    for next in range(1, num_ver + 1):
        if True not in parent:
            return
        if start == next:
            continue
        elif link_cord[start][next] and parent[next] != 0 and not visited[next]:
            parent[next] -= 1
            if parent[next] == 0:
                result += [next]
                visited[next] = 1
                dfs(next)


test_case = 10
for number in range(1, test_case + 1):
    result = []
    num_ver, num_link = map(int, input().split())  # vortex & edge 개수
    link_cord = [[0 for _ in range(num_ver + 1)] for _ in range(num_ver + 1)]
    visited = [0] * (num_ver + 1)
    parent = [0] * (num_ver + 1)  # 미리 마쳐야 하는 vortex

    link = list(map(int, input().split()))
    while len(link) != 0:
        b = link.pop()
        a = link.pop()
        link_cord[a][b] = 1
        parent[b] += 1
    for i in range(1, num_ver + 1):
        if visited[i] == 1:
            continue
        if parent[i] == 0:
            dfs(i)
    print('#{}'.format(number), end=' ')
    for i in result:
        print('{}'.format(i), end=' ')
    print()

# def dfs(start):
#     global result
#
#     if len(result) == num_ver:
#         return
#     visited[start] = 1
#     if start not in result:
#         result += [start]
#     for next in range(1, num_ver + 1):
#         if True not in parent:
#             return
#         if start == next:
#             continue
#         elif link_cord[start][next] and parent[next] != 0 and not visited[next]:
#             parent[next] -= 1
#             if parent[next] == 0:
#                 result += [next]
#                 visited[next] = 1
#                 dfs(next)
#
#
# test_case = 1
# for number in range(1, test_case + 1):
#     result = []
#     num_ver, num_link = map(int, input().split())  # vortex & edge 개수
#     link_cord = [[0 for _ in range(num_ver + 1)] for _ in range(num_ver + 1)]
#     visited = [0] * (num_ver + 1)
#     parent = [0] * (num_ver + 1)  # 미리 마쳐야 하는 vortex
#
#     link = list(map(int, input().split()))
#     while len(link) != 0:
#         b = link.pop()
#         a = link.pop()
#         link_cord[a][b] = 1
#         # if b == 522:
#         #     print('aasdsaasasa522222222')
#         parent[b] += 1
#         # print('522pppp', parent[522])
#     # print(visited[522])
#
#     for i in range(1, num_ver + 1):
#         # if i== 522:
#         #     print('find 522::::::', i)
#         # if True not in parent:
#         #     break
#         if visited[i] == 1:
#             continue
#         if parent[i] == 0:
#             dfs(i)
#         # print('522pppp', parent[522])
#     # for i in range(1, num_ver + 1):
#     #     if i not in result:
#     #         dfs(i)
#     print('#{}'.format(number), end=' ')
#     for i in result:
#         print('{}'.format(i), end=' ')
#     print()
#     # for i in set(result):
#     #     for j in result:
#     #         if i == j:
#     #             a = result.index(j)
#     #             result.pop(a)
    #     print(result)
# import sys 
# sys.stdin = open("1267_dfs_sequence", "r")


# def dfs(start):
#     global result
#     if len(result) == num_ver:
#         return
#     visited[start] = 1
#     if not start in result:
#         result += [start]
#     for next in range(1, num_ver+1):
#         if not True in parent:
#             # print(parent)
#             return
#         # print('start', start, 'next', next)
#         # # # print('matrix', link_cord)
#         # print('parent', parent)
#         # print('result', result)
#         if start == next:
#             # print('con')
#             continue
#         # if link_cord[start][next] and not visited[start] and not parent[start]:
#         #     # visited[start] = 1
#         #     result += [start]
#         #     # print('result', result)
#         #     dfs(next)
#             # if link_cord[start][next] and not visited[next]:
#                 # print('visit', start, next)
#                 # print('vissst', visited)
#                 # # result += [next]
#                 # print('result', result)
#         elif link_cord[start][next] and parent[next] != 0 and not visited[next]:
#             parent[next] -= 1
#             if parent[next] == 0:
#                 result += [next]
#                 visited[next] = 1
#             # if len(result) > 1:
#             #     result.pop()
#                 dfs(next)
        
#             # dfs(next)

# test_case = 2
# for number in range(1, test_case + 1):
#     result = []
#     num_ver, num_link = map(int, input().split())
#     link_cord = [[0 for _ in range(num_ver + 1)]for _ in range(num_ver + 1)]
#     visited = [0] * (num_ver + 1)
#     parent = [0] * (num_ver + 1)
    
#     link = list(map(int, input().split()))
#     while len(link) != 0:
#         b = link.pop()
#         a = link.pop()
#         link_cord[a][b] = 1
#         parent[b] += 1
#         # print('a', a, 'b', b)
#     print(parent)
#     for i in range(1, num_ver + 1):
#         if not True in parent:
#             # print(parent)
#             break
#         if visited[i] == 1:
#             continue
#         if parent[i] == 0:
#             dfs(i)
#     # link_cord = [[0 for _ in range(num_ver + 1)]for _ in range(num_ver + 1)]
#     # print(link)
#     #print(result)
#     # print('visi',visited)
#     # print('parent', parent)
#     # print('link_list', link_cord)
#     #  for _ in range(num_link):


#     # print('#{} {}'.format(number, result))
#     print('#{}'.format(number), end=' ')
#     for i in result:
#         print('{}'.format(i), end=' ')
#     print()
