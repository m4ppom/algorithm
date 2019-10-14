import sys
sys.stdin=open('virus.txt', 'r')


def dfs(sp):
    global computer_cnt
    visited[sp] = 1
    for aaa in range(1, computer_cnt+1):
        if base[sp][aaa] == 1 and visited[aaa] == 0:
            dfs(aaa)


computer_cnt = int(input())
link_cnt = int(input())
base = [[0]*(computer_cnt+1) for _ in range(computer_cnt+1)]
for _ in range(link_cnt):
    a, b = map(int, input().split())
    base[a][b] = 1
    base[b][a] = 1
visited = [0]*(computer_cnt+1)
dfs(1)
print(sum(visited)-1)