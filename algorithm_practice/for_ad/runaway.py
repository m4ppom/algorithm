import sys
sys.stdin = open('runrun.txt', 'r')
import collections


def in_it(i, j):
    global Nsero, Mgaro
    if -1< i < Nsero and -1 < j < Mgaro:
        return True
    else:
        return False


def run_bfs(i, j):
    global Nsero, Mgaro, mx, cnt, time
    q = collections.deque()
    q.append((i, j))
    vztd = [[0]*Mgaro for _ in range(Nsero)]
    vztd[i][j] = 1
    while q:
        y, x = q.popleft()
        if vztd[y][x] == time+1: # 몇시간했는지 카운트 맥스바꿔줌. 나중에 만들어 줘야함.
            break
        cnt += 1
        if base[y][x] == 1:  # 4방
            for dir in range(4):
                yy = y + dy[dir]
                xx = x + dx[dir]
                if in_it(yy, xx) and vztd[yy][xx] == 0:
                    if dir == 0:
                        if base[yy][xx] == 1 or base[yy][xx] == 2 or base[yy][xx] == 5 or base[yy][xx] == 6:
                            vztd[yy][xx] = vztd[y][x] + 1
                            q.append((yy, xx))
                    elif dir == 1:
                        if base[yy][xx] == 1 or base[yy][xx] == 2 or base[yy][xx] == 4 or base[yy][xx] == 7:
                            vztd[yy][xx] = vztd[y][x] + 1
                            q.append((yy, xx))
                    elif dir == 2:
                        if base[yy][xx] == 1 or base[yy][xx] == 3 or base[yy][xx] == 4 or base[yy][xx] == 5:
                            vztd[yy][xx] = vztd[y][x] + 1
                            q.append((yy, xx))
                    elif dir == 3:
                        if base[yy][xx] == 1 or base[yy][xx] == 3 or base[yy][xx] == 6 or base[yy][xx] == 7:
                            vztd[yy][xx] = vztd[y][x] + 1
                            q.append((yy, xx))
                else:
                    continue

        elif base[y][x] == 2: # 위 아래
            for dir in [0, 1]:
                yy = y + dy[dir]
                xx = x + dx[dir]
                if in_it(yy, xx) and vztd[yy][xx] == 0:
                    if dir == 0:
                        if base[yy][xx] == 1 or base[yy][xx] == 2 or base[yy][xx] == 5 or base[yy][xx] == 6:
                            vztd[yy][xx] = vztd[y][x] + 1
                            q.append((yy, xx))
                    elif dir == 1:
                        if base[yy][xx] == 1 or base[yy][xx] == 2 or base[yy][xx] == 4 or base[yy][xx] == 7:
                            vztd[yy][xx] = vztd[y][x] + 1
                            q.append((yy, xx))
                else:
                    continue

        elif base[y][x] == 3:  # 좌우
            for dir in [2, 3]:
                yy = y + dy[dir]
                xx = x + dx[dir]
                if in_it(yy, xx) and vztd[yy][xx] == 0:
                    if dir == 2:
                        if base[yy][xx] == 1 or base[yy][xx] == 3 or base[yy][xx] == 4 or base[yy][xx] == 5:
                            vztd[yy][xx] = vztd[y][x] + 1
                            q.append((yy, xx))
                    elif dir == 3:
                        if base[yy][xx] == 1 or base[yy][xx] == 3 or base[yy][xx] == 6 or base[yy][xx] == 7:
                            vztd[yy][xx] = vztd[y][x] + 1
                            q.append((yy, xx))
                else:
                    continue

        elif base[y][x] == 4:  # 상우
            for dir in [0, 3]:
                yy = y + dy[dir]
                xx = x + dx[dir]
                if in_it(yy, xx) and vztd[yy][xx] == 0:
                    if dir == 0:
                        if base[yy][xx] == 1 or base[yy][xx] == 2 or base[yy][xx] == 5 or base[yy][xx] == 6:
                            vztd[yy][xx] = vztd[y][x] + 1
                            q.append((yy, xx))
                    elif dir == 3:
                        if base[yy][xx] == 1 or base[yy][xx] == 3 or base[yy][xx] == 6 or base[yy][xx] == 7:
                            vztd[yy][xx] = vztd[y][x] + 1
                            q.append((yy, xx))
                else:
                    continue

        elif base[y][x] == 5:  # 하우
            for dir in [1, 3]:
                yy = y + dy[dir]
                xx = x + dx[dir]
                if in_it(yy, xx) and vztd[yy][xx] == 0:
                    if dir == 1:
                        if base[yy][xx] == 1 or base[yy][xx] == 2 or base[yy][xx] == 4 or base[yy][xx] == 7:
                            vztd[yy][xx] = vztd[y][x] + 1
                            q.append((yy, xx))
                    elif dir == 3:
                        if base[yy][xx] == 1 or base[yy][xx] == 3 or base[yy][xx] == 6 or base[yy][xx] == 7:
                            vztd[yy][xx] = vztd[y][x] + 1
                            q.append((yy, xx))
                else:
                    continue


        elif base[y][x] == 6:  # 하좌
            for dir in [1, 2]:
                yy = y + dy[dir]
                xx = x + dx[dir]
                if in_it(yy, xx) and vztd[yy][xx] == 0:
                    if dir == 1:
                        if base[yy][xx] == 1 or base[yy][xx] == 2 or base[yy][xx] == 4 or base[yy][xx] == 7:
                            vztd[yy][xx] = vztd[y][x] + 1
                            q.append((yy, xx))
                    elif dir == 2:
                        if base[yy][xx] == 1 or base[yy][xx] == 3 or base[yy][xx] == 4 or base[yy][xx] == 5:
                            vztd[yy][xx] = vztd[y][x] + 1
                            q.append((yy, xx))
                else:
                    continue

        elif base[y][x] == 7:  # 상좌
            for dir in [0, 2]:
                yy = y + dy[dir]
                xx = x + dx[dir]
                if in_it(yy, xx) and vztd[yy][xx] == 0:
                    if dir == 0:
                        if base[yy][xx] == 1 or base[yy][xx] == 2 or base[yy][xx] == 5 or base[yy][xx] == 6:
                            vztd[yy][xx] = vztd[y][x] + 1
                            q.append((yy, xx))
                    elif dir == 2:
                        if base[yy][xx] == 1 or base[yy][xx] == 3 or base[yy][xx] == 4 or base[yy][xx] == 5:
                            vztd[yy][xx] = vztd[y][x] + 1
                            q.append((yy, xx))
                else:
                    continue


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
testnum = int(input())
for testcase in range(1, testnum+1):
    Nsero, Mgaro, Rman, Cman, time = map(int, input().split())
    base = [0]*Nsero
    for _ in range(Nsero):
        base[_] = list(map(int, input().split()))
    #  1 4방,  2 위아래 , 3 좌우 , 4 상우,  5 하우,  6 좌하,  7 좌상
    # bfs로 spread하는데 파이프 모양에 따라 움직임.
    cnt = 0
    mx = 0
    run_bfs(Rman, Cman)
    print('#%d %d' %(testcase, cnt))