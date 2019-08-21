# import sys
# sys.stdin = open("input.txt", "r")

def push(x):
    global top
    top += 1
    stack[top] = x

def pop():
    global top
    if top == -1 :
        return 0
    x = stack[top]
    top -= 1
    return x

def findnext(v):
    for i in range(1, 8):
        if G[v][i] and not visited[i]:
            return i
    return 0

def DFS(v):
    print(v, end=" ")
    visited[v] = True
    while v != 0:

        for i in range(1, 8):
            if G[v][i] and visited[i] == 0:
                w = i
        w = 0
        if w != 0:
            stack.append(v)
        while w != 0:
            print(w, end=" ")
            visited[w] = True
            stack.append(v)
            v = w
            for i in range(1, 8):
                if G[v][i] and visited[i] == 0:
                    w = i
            w = 0
        v = pop()

def DFSr(v):  #recursive DFS
     print(v, end=" ")
     visited[v] = True

     for i in range(1, 8):
         if G[v][i] and not visited[i]:
             DFSr(i)


edges = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
visited = [0] * (8)
G = [[0]* (len(set(edges))) for _ in range(8)]
stack = [0] * 10
top = -1

for i in range(0, len(edges), 2):
    G[edges[i]][edges[i+1]] = 1
    G[edges[i+1]][edges[i]] = 1
v = 1
print(v, end=" ")
visited[v] = True
while v != 0:
    for i in range(1, 8):
        if G[v][i] and visited[i] == 0:
            w = i
    w = 0
    if w != 0:
        stack.append(v)
    while w != 0:
        print(w, end=" ")
        visited[w] = True
        stack.append(v)
        v = w
        for i in range(1, 8):
            if G[v][i] and visited[i] == 0:
                w = i
        w = 0
    v = pop()

# DFS(1)

visited = [0] * 8
G = [[0] * 8 for _ in range(8)]
print("\n=== recursive DFS ===")
for i in range(0, len(edges), 2):
     G[edges[i]][edges[i+1]] = 1
     G[edges[i+1]][edges[i]] = 1

DFSr(1)