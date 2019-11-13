import sys
sys.stdin = open('home.txt', 'r')
import collections


def in_it(a, b):
    global N
    if -1 < a < N and -1 < b < N:
        return True
    else:
        return False


def spread_bfs(i, j, giri):
    global N, house_count
    vztd = [[0]*N for _ in range(N)]
    q = collections.deque()
    q.append((i, j))
    vztd[i][j] = 1
    while q:
        y, x = q.popleft()
        if vztd[y][x] == giri:
            break
        for i in range(4):
            yy = y + dy[i]
            xx = x + dx[i]
            if in_it(yy, xx) and vztd[yy][xx] == 0:
                if base[yy][xx] == 1:
                    house_count += 1
                vztd[yy][xx] = vztd[y][x] + 1
                q.append((yy, xx))
            else:
                continue
    return



dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
testnumber = int(input())
for testcase in range(1, testnumber+1):
    N, M = map(int, input().split())
    base = [0]*N
    hommy_idx = 0
    hommy = [0] * 500
    # 중심을 집으로 시작할지 그냥 전체 다돌려볼지 고민
    for _ in range(N):
        base[_] = list(map(int, input().split()))
        for __ in range(N):
            if base[_][__] == 1:
                hommy[hommy_idx] = (_, __)
                hommy_idx += 1
    # 일단 집 위치정보 넣어두고 돌려볼 생각
    maxx = 0
    for i in range(N):
        for j in range(N):
    # for aa in range(hommy_idx):
    #     i, j = hommy[aa]
        # print(i,j,'----------------------')
            for k in range(1, 3*N):
                house_count = 0
                if base[i][j] == 1:
                    house_count += 1
                spread_bfs(i, j, k)
                money = (k**2) + ((k-1)**2)
                if (M*house_count) >= money:
                    # print(house_count, 'dasd', k)
                    if house_count > maxx:
                        maxx = house_count
    for i in range(N):
        for j in range(N):
            for k in range(1, 2*N):
                house_count = 0
                if base[i][j] == 1:
                    house_count += 1
                spread_bfs(i, j, k)
                money = (k**2) + ((k-1)**2)
                if (M*house_count) >= money:
                    # print(house_count, 'dasd', k)
                    if house_count > maxx:
                        maxx = house_count
    print('#%d %d' %(testcase, maxx))


