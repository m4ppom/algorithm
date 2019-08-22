import  sys
sys.stdin = open("inpu.txt", "r")


def DFS(start):
    global result

    visited[start] = 1
    for next in range(1, v+1):
        if base[start][next] and not visited[next]:
            if next == end_node:
                result = 1
                return
            DFS(next)


testcase = int(input())
for num in range(1, testcase + 1):
    v, e = map(int, input().split())
    base = [[0]*(v+1) for _ in range(v+1)]
    visited = [0] * (v+1)
    for i in range(e):
        start, end = map(int, input().split())
        base[start][end] = 1
    start_node, end_node = map(int, input().split())
    result = 0
    DFS(start_node)
    print('#{} {}'.format(num, result))
