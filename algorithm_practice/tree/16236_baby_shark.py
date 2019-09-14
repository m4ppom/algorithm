import sys
sys.stdin = open('inpu.txt', 'r')
import copy


def cnt():
    global count, shark_size
    count += 1
    if count == shark_size:
        shark_size += 1
        count = 0
        return


def eating(lst):
    global baby_cord, time
    if lst:
        x, y = baby_cord
        base[x][y] = 0
        if len(lst)==1:
            x, y, time_tem = lst.pop()
            baby_cord = (x, y)
        else:
            new = sorted(lst)
            for i in range(len(new)-1):
                for j in range(i+1, len(new)):
                    if new[i][1] < new[j][1] and new[i][0] == new[j][0]:
                        new[i] , new[j] = new[j], new[i]
                        print(new)
            x, y, time_tem = lst.pop(0)
            baby_cord =(x, y)
        time += time_tem
        cnt()
    else:
        return



def bfs(x, y):
    global shark_size
    q = []
    q.append((x, y))
    base_copy[x][y] = 1
    ret = 0
    while len(q):
        (x, y) = q.pop(0)
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < N and 0 <= yy < N:
                if 0< base[xx][yy] < shark_size  and base_copy[xx][yy] == 0:
                    vict.append((xx, yy, ret))
                    base_copy[xx][yy] = base_copy[x][y] + 1
                elif base[xx][yy] == 0 or base[xx][yy] == shark_size:
                    if base_copy[xx][yy] == 0 and not vict:
                        q.append((xx, yy))
                        base_copy[xx][yy] = base_copy[x][y] + 1
    eating(vict)
    return


dy = [-1, 1 ,0 ,0]
dx = [0, 0, -1, 1]

# 처음 상어크기 2,,,, 1초에 1 크기 작은거만 먹을 수 있음 같은거 지나가기는 가능
# 없으면 엄마부 가장 가까운 물고기 먹으러감
# 가장위 제일 왼쪽
# 자기 수 만큼 먹으면 크기 1증가

testcase = int(input())
for test_num in range(1, testcase+1):
    N = int(input())
    time = 0
    base = [0] * N
    shark_size = 2
    count = 0
    baby_cord = 0
    vict = []
    for i in range(N):
        base[i] = list(map(int, input().split()))
    base_copy = [[0 for _ in range(N)]for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if base[i][j] == 9:
                baby_cord = (i, j)
                break
        if baby_cord:
            break
    brrr = 0
    while brrr != 1:
        x, y = baby_cord
        bfs(x, y)
        # print(time)
        num = 0
        for i in range(N):
            for j in range(N):
                if shark_size >= base[i][j] or base[i][j] == 0:
                    num += 1
        if num == N**2:
            brrr = 1