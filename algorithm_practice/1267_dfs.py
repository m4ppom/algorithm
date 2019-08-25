import sys 
sys.stdin = open("1267_dfs_sequence", "r")

def is_start(graph, point):
    for point2 in graph:
        if point[0] == point2[1]:
            return False
    return True
 
T = 1
for t in range(1, T+1):
    V, E = map(int, input().split())
    temp = list(map(int, input().split()))
    graph = [temp[i:i+2] for i in range(0, len(temp), 2)]
    path = []
    stack = []
 
    for point in graph:
        if is_start(graph, point):
            stack.append(point)
 
    while graph:
        cur = stack.pop(-1)
        graph.pop(graph.index(cur))
 
        if cur[0] not in path:
            path.append(cur[0])
 
        for point in graph:
            if cur[1] == point[0] and is_start(graph, point):
                stack.append(point)
 
    for i in range(1, V+1):
        if i not in path:
            path.append(i)
            
    print(len(set(path)))
    path = ' '.join(list(map(str, path)))
    print('#{} {}'.format(t, path))
    