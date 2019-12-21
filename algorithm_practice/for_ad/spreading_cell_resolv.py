import sys
sys.stdin = open('cell.txt', 'r')


# 4 directions cell spreading
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
def cell_spreading(i, j):
    for dir in range(4):
        search_dir_i = i + dy[dir]
        search_dir_j = j + dx[dir]
        if base[search_dir_i][search_dir_j] == 0:
    return


testcase = int(input())
for testnum in range(testcase + 1 ):
    N, M, K = int(input().split())
    base =[0]*N

