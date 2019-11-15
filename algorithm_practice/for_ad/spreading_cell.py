import sys
sys.stdin = open('cell.txt', 'r')






# def spreading_bfs1(i, j, life):
#     global flag_for_q
#     q = collections.deque()
#     q.append((i, j))
#     vztd[i][j] = [life, 1]
#     while q:
#         y, x = q.popleft()
#         for dir in range(4):
#             yy = y + dy[dir]
#             xx = x + dx[dir]
#             if vztd[yy][xx][0] < vztd[y][x][0] and vztd[yy][xx][1] == 0:
#                 vztd[yy][xx] = [vztd[y][x][0], 0]
#                 if flag_for_q == 1:
#                     cell_queue2.append([vztd[y][x][0], 0, yy, xx])
#                 elif flag_for_q == 2:
#                     cell_queue.append([vztd[y][x][0], 0, yy, xx])
#             else:
#                 pass


def spreading_bfs2(i, j, life):
    for dir in range(4):
        ii = i + dy[dir]
        jj = j + dx[dir]
        if vztd[ii][jj] == 0:
            vztd[ii][jj] = life
            if flag_for_q == 1:
                cell_queue2.append([life, 0, ii, jj])
            elif flag_for_q == 2:
                cell_queue.append([life, 0, ii, jj])



dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
testnum = int(input())
for testcase in range(1, testnum+1):
    N, M, K = map(int, input().split())
    base = [0]*N
    vztd = [[0]*600 for _ in range(600)]
    cell_queue = []  # collections.deque()
    for _ in range(N):
        base[_] = list(map(int, input().split()))
        for __ in range(M):
            if base[_][__] != 0:
                cell_queue.append([base[_][__], 0, _+300, __+300])
                vztd[_+300][__+300] = base[_][__]
                # 세포정보 queue에 저장
    time = 0
    cell_queue2 = []  # collections.deque()
    dead_cell = []  # collections.deque()
    flag_for_q = 1
    for _ in range(K):
        if cell_queue:
            cell_queue.sort()
            while cell_queue:
                lf, age, iii, jjj = cell_queue.pop()
                if lf != age:
                    age += 1
                    cell_queue2.append([lf, age, iii, jjj])
                else:
                    spreading_bfs2(iii, jjj, lf)
                    dead_cell.append([lf, age, iii, jjj])
            flag_for_q = 2
        elif cell_queue2:
            cell_queue2.sort()
            while cell_queue2:
                lf, age, iii, jjj = cell_queue2.pop()
                if lf != age:
                    age += 1
                    cell_queue.append([lf, age, iii, jjj])
                else:
                    spreading_bfs2(iii, jjj, lf)
                    dead_cell.append([lf, age, iii, jjj])
            flag_for_q = 1
        for dead in range(len(dead_cell)-1, -1, -1):
            if dead_cell[dead][1] == 1:
                dead_cell.pop(dead)
            else:
                dead_cell[dead][1] -= 1



    # for i, j, life, flag in cell_queue:
    #     vztd[i][j] = [life, 0]
    # while time != K-1:
    #     # time += 1
    #     if cell_queue:
    #         cell_queue.sort()
    #         while cell_queue:
    #             temp = cell_queue.pop()
    #             if temp[1] == temp[0]-1:
    #                 vztd[temp[2]][temp[3]] = [temp[0], 1]
    #                 cell_queue2.append(temp)
    #                 temp[1] += 1
    #             elif temp[1] < temp[0]-1:
    #                 vztd[temp[2]][temp[3]] = [temp[0], 0]
    #                 cell_queue2.append(temp)
    #                 temp[1] += 1
    #             elif temp[1] == temp[0]:
    #                 temp[1] += 1
    #                 spreading_bfs(temp[2], temp[3], temp[0])
    #                 dead_cell.append(temp)
    #
    #             # elif temp[3] > temp[2]:
    #             #     dead_cell.append(temp)
    #         flag_for_q = 2
    #     elif cell_queue2:
    #         cell_queue2.sort()
    #         while cell_queue2:
    #             temp = cell_queue2.pop()
    #             if temp[1] < temp[0]:
    #                 vztd[temp[2]][temp[3]] = [temp[0], 0]
    #                 cell_queue.append(temp)
    #                 temp[1] += 1
    #             elif temp[1] == temp[0]:
    #                 temp[1] += 1
    #                 spreading_bfs(temp[2], temp[3], temp[0])
    #                 dead_cell.append(temp)
    #         flag_for_q = 1
    #     time += 1
    # dead = 0
    # # print(dead_cell)
    # for lf, age, iii, jjj in dead_cell:
    #     if age != 0:
    #         dead += 1
    #     else:
    #         pass
    dead = len(dead_cell)

    if flag_for_q == 1:
        num = len(cell_queue)
    elif flag_for_q == 2:
        num = len(cell_queue2)
    print('#%d %d' %(testcase, num+dead))