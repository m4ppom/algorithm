import sys
sys.stdin = open("inpu33.txt", "r")


def DFS(start):
    global result

    visited[start] = 1
    for next in range(1, node_count+1):
        if base[start][next] and not visited[next]:
            print('a',start, next)
            # print(visited)
            # print('end', end)
            # print('next', next)
            # if next == end:
            #     return
            result += 1
            # print(result)
            DFS(next)


node_count = int(input())
linked_node = int(input())
base = [[0]*(node_count+1) for _ in range(node_count+1)]
visited = [0] * (node_count+1)
for i in range(linked_node):
    start, end = map(int, input().split())
    base[start][end] = 1
    base[end][start] = 1
result = 0
# print(base)
DFS(1)
print('{}'.format(result))
