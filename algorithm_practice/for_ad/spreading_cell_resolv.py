import sys
sys.stdin = open('cell.txt', 'r')


# 4 directions cell spreading
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def cell_spreading(i, j, life):
    for dir in range(4):
        search_dir_i = i + dy[dir]
        search_dir_j = j + dx[dir]
        if base[search_dir_i][search_dir_j] == 0:
            cell_info.append([life, search_dir_i, search_dir_j, life])
            base[search_dir_i][search_dir_j] = life
    return


def spreading():
    for sp in range(len(cell_info)):
        cell_info[sp][3] = cell_info[sp][3]-1
        if cell_info[sp][3] == -1:
            life = cell_info[sp][0]
            cell_spreading(cell_info[sp][1], cell_info[sp][2], life)
    return


testcase = int(input())
for testnum in range(testcase + 1 ):
    N, M, K = map(int, input().split())
    cell_info = []
    base = [[0]*(M+2*K+1) for _ in range(N+2*K+1)]
    for _ in range(N):
        temp = list(map(int, input().split()))
        for num in range(len(temp)):
            a = K+_
            b = K+num
            base[a][b] = temp[num]
            cell_info.append([temp[num], a, b, temp[num]])
    for time in range(K):
        print(cell_info)
        cell_info.sort(reverse=True)
        print(cell_info)
        spreading()



