def MST_prim(G, s)  # 그래프. 시작정점
    key = [INF]*N
    pi = [None]*N
    visited = [False]*N
    key[s] = 0
    for _ in range(N):
        minIndex = -1
        min = INF
        for i in range(N):
            if not visited[i] and key[i] < min:
                min = key[i]
                minIndex = i
        visited[minIndex] = True
        for v, val in G[minIndex]:
            if not visited[v] and val < key[v]:
                key[v] = val

N=1
def MST_kruskal(G):
    global N
    mst = []
    for i in range(N):
        Make_Set(i)
    G.sort(key = lambda t: t[2])  # 가중치를 기준으로 정렬
    mst_cost = 0
    while len(mst
              )