import sys
sys.stdin = open('gamC.txt', 'r')

# 1번은 한쪽 2번 일자로 2방향 3번 직각2방향 4번 3방향 5번 4방향
# 씨씨티비 회전가능 벽통과할 수 없음 사각지대
# 회전 항상 90도 6은 벽
# 이전에 사냥꾼 느낌으로 하될듯. 사각지대 최소일 때
# 1 버젼 4개 2 = 2개 3=4개 4  4개 5=1개
# 팝말고 인덱스로 
import collections, copy

def cctv1(i, j, ggu):
    global row, col

    if ggu == 0:  # up
        for a in range(i, -1, -1):
            if base[a][j] == 0:
                if base[a][j] == 6:
                    break
                base[a][j] = 7
    elif ggu == 1:  # right
        for a in range(j, col):
            if base[i][a] == 6:
                break
            if base[i][a] == 0:
                base[i][a] = 7
    elif ggu == 2:  # down
        for a in range(i, row):
            if base[a][j] == 0:
                if base[a][j] == 6:
                    break
                base[a][j] = 7
    elif ggu == 3:  # left
        for a in range(j, -1, -1):
            if base[i][a] == 6:
                break
            if base[i][a] == 0:
                base[i][a] = 7


def cctv2(i, j, ggu):
    global row, col

    if ggu == 0:  # up down
        for a in range(i, -1, -1):
            if base[a][j] == 0:
                if base[a][j] == 6:
                    break
                base[a][j] = 7
        for a in range(i, row):
            if base[a][j] == 0:
                if base[a][j] == 6:
                    break
                base[a][j] = 7

    elif ggu == 1:  # right left
        for a in range(j, col):
            if base[i][a] == 6:
                break
            if base[i][a] == 0:
                base[i][a] = 7
        for a in range(j, -1,-1):
            if base[i][a] == 6:
                break
            if base[i][a] == 0:
                base[i][a] = 7


def cctv3(i, j, ggu):
    global row, col

    if ggu == 0:  # up right
        for a in range(i, -1, -1):
            if base[a][j] == 0:
                if base[a][j] == 6:
                    break
                base[a][j] = 7
        for a in range(j, col):
            if base[i][a] == 6:
                break
            if base[i][a] == 0:
                base[i][a] = 7

    elif ggu == 1:  # right down
        for a in range(j, col):
            if base[i][a] == 6:
                break
            if base[i][a] == 0:
                base[i][a] = 7
        for a in range(i, row):
            if base[a][j] == 0:
                if base[a][j] == 6:
                    break
                base[a][j] = 7
    elif ggu == 2:  # down left
        for a in range(i, row):
            if base[a][j] == 0:
                if base[a][j] == 6:
                    break
                base[a][j] = 7
        for a in range(j, -1, -1):
            if base[i][a] == 6:
                break
            if base[i][a] == 0:
                base[i][a] = 7
    elif ggu == 3:  # left up
        for a in range(j, -1, -1):
            if base[i][a] == 6:
                break
            if base[i][a] == 0:
                base[i][a] = 7
        for a in range(i, -1, -1):
            if base[a][j] == 0:
                if base[a][j] == 6:
                    break
                base[a][j] = 7


def cctv4(i, j, ggu):
    global row, col

    if ggu == 0:  # up right down
        for a in range(i, -1, -1):
            if base[a][j] == 0:
                if base[a][j] == 6:
                    break
                base[a][j] = 7
        for a in range(j, col):
            if base[i][a] == 6:
                break
            if base[i][a] == 0:
                base[i][a] = 7
        for a in range(i, row):
            if base[a][j] == 0:
                if base[a][j] == 6:
                    break
                base[a][j] = 7

    elif ggu == 1:  # right down left
        for a in range(j, col):
            if base[i][a] == 6:
                break
            if base[i][a] == 0:
                base[i][a] = 7
        for a in range(i, row):
            if base[a][j] == 0:
                if base[a][j] == 6:
                    break
                base[a][j] = 7
        for a in range(j, -1, -1):
            if base[i][a] == 6:
                break
            if base[i][a] == 0:
                base[i][a] = 7

    elif ggu == 2:  # down left up
        for a in range(i, row):
            if base[a][j] == 0:
                if base[a][j] == 6:
                    break
                base[a][j] = 7
        for a in range(j, -1, -1):
            if base[i][a] == 6:
                break
            if base[i][a] == 0:
                base[i][a] = 7
        for a in range(i, -1, -1):
            if base[a][j] == 0:
                if base[a][j] == 6:
                    break
                base[a][j] = 7

    elif ggu == 3:  # left up right
        for a in range(j, -1, -1):
            if base[i][a] == 6:
                break
            if base[i][a] == 0:
                base[i][a] = 7
        for a in range(i, -1, -1):
            if base[a][j] == 0:
                if base[a][j] == 6:
                    break
                base[a][j] = 7
        for a in range(j, col):
            if base[i][a] == 6:
                break
            if base[i][a] == 0:
                base[i][a] = 7


def cctv5(i, j):
    global row, col
    for a in range(i, row):
        if base[a][j] == 0:
            if base[a][j] == 6:
                break
            base[a][j] = 7
    for a in range(i, -1, -1):
        if base[a][j] == 0:
            if base[a][j] == 6:
                break
            base[a][j] = 7
    for a in range(j, col):
        if base[i][a] == 6:
            break
        if base[i][a] == 0:
            base[i][a] = 7
    for a in range(j, -1, -1):
        if base[i][a] == 6:
            break
        if base[i][a] == 0:
            base[i][a] = 7



def cctv_info(number, a, b):
    global base
    if number == 1:
        for i in range(4):
            bc = copy.deepcopy(base)
            cctv1(a, b, i)
            dream()
            base = bc
    elif number == 2:
        for i in range(2):
            bc = copy.deepcopy(base)
            cctv2(a, b, i)
            dream()
            base = bc
    elif number == 3:
        for i in range(4):
            bc = copy.deepcopy(base)
            cctv3(a, b, i)
            dream()
            base = bc
    elif number == 4:
        for i in range(4):
            bc = copy.deepcopy(base)
            cctv4(a, b, i)
            dream()
            base = bc
    elif number == 5:
        cctv5(a, b)
        dream()

def dream():
    global cnt, leng, minnn, cctv
    if cctv:
        a, b = cctv.pop()
        cctv_info(base[a][b], a, b)
        cnt += 1
    else:
        num = 0
        for iii in range(row):
            for jjj in range(col):
                if base[iii][jjj] == 0:
                    num += 1
        if num < minnn:
            minnn = num
            cctv = ct
        return

# 안에 함수 와일 팝 안에 함수와일 팝 안에 함수 와일
row, col = map(int,input().split())
base = [0]*row
for i in range(row):
    base[i] = list(map(int, input().split()))
cctv = []
for ii in range(row):
    for jj in range(col):
        if base[ii][jj] != 0 and base[ii][jj] != 6:
            cctv.append((ii, jj))
ct = copy.deepcopy(cctv)
leng = len(cctv)
cnt = 0
minnn = 999999
dream()
print(minnn)

