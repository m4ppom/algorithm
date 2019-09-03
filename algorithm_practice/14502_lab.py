import sys 
import copy
sys.stdin = open('inpu.txt')


def inner(row, col):
    global N, M
    if -1 < row < N and -1 < col < M:
        return True
    else:
        return False


def counting(list):
    return


def spread(row, col):
    global virus_movement
    global base_copy
    base_copy = copy.deepcopy(base)
    for i in range(4):
        if not inner(row+dy[i], col+dx[i]):
            continue
        if base_copy[row+dy[i]][col+dx[i]] == 0:
            base_copy[row+dy[i]][col+dx[i]] = 2
            virus_movement += 1
            print('momo vvivi', virus_movement)
            if virus_movement > mini_virus:
                return
            spread(row+dy[i], col+dx[i])
        else:
            continue
    if mini_virus > virus_movement:
        mini_virus = virus_movement
    return


def building(row, col):
    global N, M, cnt, virus
    if base[row][col] != 0:
        return
    if base[row][col] == 0:
        base[row][col] = 1
        cnt -= 1
        if cnt == 0:
            base_copy = copy.deepcopy(base)
            for i in range(len(virus)//2):
                spread(2*i, 2*i+1)
        base[row][col] = 0
        return
    # base[row, col] = 1
    # building(row, col+1)


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
N, M = map(int, input().split())
base = [0]*N
virus = []
cnt = 3
virus_movement = 0
mini_virus = 10000
wall = 0
for i in range(N):
    base[i] = list(map(int, input().split()))
for i in range(N):
    for j in range(M):
        if base[i][j] == 2:
            virus += [i, j]
            wall += 1


for i in range(N*M):
        building(i//M, i%M)

# for i in range(N):
#     for j in range(1, N-i):
#         linear_increase(i, j)
# def linear_increase(num1_index, num):
#     global N
#     global result
#     if num1_index + num >= N:
#         return result
#     left = num_list[num1_index] * num_list[num1_index+num]
#     if len(str(left)) == 1:
#         pass
#     else:
#         for i in range(len(str(left))-1):
#             if str(left)[i] <= str(left)[i+1]:
#                 pass
#             else:
#                 return
#     if result < left:
#         result = left
#         return

safe_area = N*M - wall - mini_virus
print(virus)
print(base)
print('ghghghg', safe_area)
