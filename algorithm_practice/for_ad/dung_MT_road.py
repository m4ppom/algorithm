import sys
sys.stdin = open('MT_road.txt', 'r')


def in_it(x, y):
    if -1< x < N and -1 < y < N:
        return True
    else:
        return False


def is_max(num):
    global maxx
    if num > maxx:
        maxx = num


def pathfinderdfs(i, j):
    global num
    y = i
    x = j
    for dir in range(4):
        yy = y + dy[dir]
        xx = x + dx[dir]
        if in_it(yy, xx):  # 벽안에 있는지
            if base[yy][xx] < base[y][x]:
                vztd[yy][xx] = vztd[y][x] + 1
                pathfinderdfs(yy, xx)
                num = vztd[yy][xx]
                vztd[yy][xx] = 0
            else:
                continue
        else:
            continue
    is_max(num)


# bfs로 갈 수 있는 거리 가장 최대인거 출력 생각해보니까 이러면 안될듯 dfs로 바꿔야겠음
# def pathfinderbfs(i, j):
#     global num
#     q = []
#     num = 0
#     vztd = [[0]*N for _ in range(N)]
#     q.append((i, j))
#     vztd[i][j] = 1
#     while q:
#         y, x = q.pop()
#         for dir in range(4):
#             yy = y + dy[dir]
#             xx = x + dx[dir]
#             if in_it(yy, xx):  # 벽안에 있는지
#                 if base[yy][xx] < base[y][x]:
#                     vztd[yy][xx] = vztd[y][x] + 1
#                     q.append((yy, xx))
#                     num = vztd[yy][xx]
#                 else:
#                     continue
#             else:
#                 continue
#     is_max(num)


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
testnum = int(input())
for testcase in range(1, testnum+1):
    N, K = map(int, input().split())
    base = [0]*N
    st_point = [0]*5
    idxidx = 0
    maxx = 0
    bong_uri = 0
    for _ in range(N):
        base[_] = list(map(int, input().split()))
        # 9인 지점 위치 찾기 xxx 그냥 가장높은게 봉우리임
        for __ in range(N):
            if base[_][__] > bong_uri:
                idxidx = 0
                bong_uri = base[_][__]
                st_point[idxidx] = (_, __)
                idxidx += 1
            elif base[_][__] == bong_uri:
                st_point[idxidx] = (_, __)
                idxidx += 1
            elif base[_][__] < bong_uri:
                pass

    # bf로 다돌아보기 최대 공사가능깊이 하나하나 다해보면서 ==> 시간초과날듯
    for garo in range(N):
        for sero in range(N):
            for ddangPaGi in range(1, K+1):
                base[garo][sero] = base[garo][sero] - ddangPaGi
                for i in range(5):  # 봉우리좌표돌리기
                    if st_point[i] != 0:
                        i, j = st_point[i]
                        if base[i][j] != bong_uri:
                            continue
                        else:
                            # print(i, j)
                            num = 0
                            vztd = [[0] * N for _ in range(N)]
                            vztd[i][j] = 1
                            pathfinderdfs(i, j)
                            vztd[i][j] = 0
                base[garo][sero] = base[garo][sero] + ddangPaGi
    # print('#', testcase,' ', maxx)
    print('#%d %d' % (testcase, maxx))