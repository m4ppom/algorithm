import sys 
sys.stdin = open("1267_dfs_sequence", "r")


# def dfs(x):
#     if x not in result and x != 0:
#         result.append(x)
#     arr = arrr[:]
#     if arr[x] and visited[x] == 0:
#         for i in range(len(arr[x])):
#             try:
#                 if visited[arr[x][i]] == 0 and point_li[arr[x][i]] == 2:
#                     point_li[arr[x][i]] -= 1
#                 elif visited[arr[x][i]] == 0 and point_li[arr[x][i]] <= 1:
#                     visited[x] = 1
#                     dfs(arr[x][i])
#             except IndexError:
#                 pass
# for tc in range(1, 11):
#     print('#%d' %tc, end=' ')
#     V, E = map(int, input().split())
#     li = list(map(int, input().split()))
#     arrr = [[] for _ in range(V+1)]
#     check_li = []
#     visited = [0]*(V+1)
#     result = []
#     point_li = [0]*(V+1)
#     for s in range(1, len(li), 2):
#         check_li.append(li[s])
#         point_li[li[s]] += 1
#     for j in range(0, len(li), 2):
#         arrr[li[j]].append(li[j+1])
#         if li[j] not in check_li or li[j] not in arrr[0]:
#             arrr[0].append(li[j])
#     dfs(0)
#     print(' '.join(map(str, result)))
#     print('v',V,len(result))

#
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
def DFS(start_node):
    stack = [start_node]
    visited = [[0]*matrix_row for _ in range(matrix_column)]
    visited[start_node[0]][start_node[1]] = 1
    count = 1
    while stack:
        a = stack.pop()
        for i in range(4):
            y = a[0]
            x = a[1]
            idy = y + dy[i]
            idx = x + dx[i]
            if 0 <= idy < matrix_column and 0 <= idx < matrix_row:
                if visited[idy][idx] == 0:
                    if matrix[idy][idx] == 0:
                        count += 1
                        visited[idy][idx] = count
                        stack.append(([y, x]))
                        stack.append([idy, idx])
                        break
    for j in visited:
        print(j)
​
​
matrix_column, matrix_row = map(int, input().split())
​
matrix = [list(map(int, input().split())) for _ in range(matrix_column)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
DFS([0, 0])