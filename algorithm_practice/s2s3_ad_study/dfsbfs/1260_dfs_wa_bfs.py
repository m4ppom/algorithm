import sys
sys. stdin = open('dfs_wa_bfs.txt', 'r')


def dfs(sp):
    global node_cnt
    if visitid_dfs[sp] == 0:
        visitid_dfs[sp] = 1
        for dfsdfs in range(1, node_cnt+1):
            if base_two[sp][dfsdfs] == 1:
                if visitid_dfs[dfsdfs] == 0:
                    print(dfsdfs, end=' ')
                    dfs(dfsdfs)


def bfs(spp):
    global node_cnt
    q = []
    q.append(spp)
    while q:
        a = q.pop(0)
        print(a, end=' ')
        for bbb in range(1, node_cnt+1):
            if base_two[a][bbb] == 1:
                if visitid_bfs[bbb] == 0:
                    q.append(bbb)
                    visitid_bfs[bbb] = 1



node_cnt, link_cnt, st_point = map(int, input().split())
 # 노드 수 랑 같이 만들려고하는데 ...
visitid_dfs = [0]*(node_cnt+1)
visitid_bfs = [0]*(node_cnt+1)
base_two = [[0]*(node_cnt+1) for _ in range(node_cnt+1)]
for link in range(link_cnt):
    a, b = map(int, input().split())
    base_two[a][b] = 1
    base_two[b][a] = 1  # 쌍방향
print(st_point, end=' ')
dfs(st_point)
print()
# print(st_point, end=' ')
visitid_bfs[st_point] = 1
bfs(st_point)
