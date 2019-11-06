import sys
sys.stdin = open('gamC.txt', 'r')

# 1번은 한쪽 2번 일자로 2방향 3번 직각2방향 4번 3방향 5번 4방향
# 씨씨티비 회전가능 벽통과할 수 없음 사각지대
# 회전 항상 90도 6은 벽
# 이전에 사냥꾼 느낌으로 하될듯. 사각지대 최소일 때
# 1 버젼 4개 2 = 2개 3=4개 4  4개 5=1개

def cctv1(i, j, dir):
    return


def cctv2(i, j, dir):
    return

def cctv3(i, j, dir):
    return


def cctv4(i, j, dir):
    return


def cctv5(i, j, dir):
    global row, col
    for a in range(i, row):
        if base[a][j] == 0:
            if base[a][j] == 6:
                break
            base[a][j] = 7
    for a in range(i, -1):
        if base[a][j] == 0:5;lpp
            if base[a][j] == 6:
                break
            base[a][j] = 7
    for a in range(j, col):
        if base[i][a] == 6:
            break
        if base[i][a] == 0:
            base[i][a] = 7
    for a in range(j, -1):
        if base[i][a] == 6:
            break
        if base[i][a] == 0:
            base[i][a] = 7

# 안에 함수 와일 팝 안에 함수와일 팝 안에 함수 와일 팝
row, col = map(int,input().split())
base = [0]*row
for i in range(row):
    base[i] = list(map(int, input().split()))
cctv = []
for ii in range(row):
    for jj in range(col):
        if base[ii][jj] != 0 and base[ii][jj] != 6:
            cctv.append((ii, jj))

