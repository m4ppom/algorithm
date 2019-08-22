import sys
sys.stdin = open("inpu.txt", "r")

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def vila_dfs(x, y):
    global result
    base[y][x] += comple
    for i in range(4):
        if y + dy[i] > 0 and y + dy[i] < size and x + dx[i] > 0 and x + dx[i] < size:
            if base[y+dy[i]][x+dx[i]] == 1:
                return
            vila_dfs(x+dx[i], y+dy[i])



size = int(input())
base = [0]*size
for i in range(7):
    base[i] = list(map(int, input()))
print(base)
comple = 1