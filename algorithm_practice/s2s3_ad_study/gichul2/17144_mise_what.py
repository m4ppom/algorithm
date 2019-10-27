import sys
sys.stdin = open('mise.txt', 'r')

import collections
import copy

def spread():
    pass

def purify_air():
    pass

def direction(i, j, mise):
    # 4방향보면서 확산하는데 그 값을 카피본에 저장해서 나중에 한번에 바꿔줌
    global R, C
    mun_G = mise//5
    for dir in range(4):
        ii = i+dy[dir]
        jj = j+dx[dir]
        if -1 < ii < R and -1 < jj < C:
            if base[ii][jj] != -1:
                base_copy[ii][jj] += mun_G
                base_copy[i][j] -= mun_G

def cirQulation(i, j):
    global R, C, flag
    cirq = collections.deque()
    cirq.appendleft(0)
    temp = 0
    dir = 0
    a = i
    b = j
    if flag == 0:
        while temp != -1:
            a = a +dy[dir]
            b = b +dx[dir]
            if -1 < a < R and -1 < b < C:
                cirq.append(base[a][b])
                temp = base[a][b]
            else:
                a -= dy[dir]
                b -= dx[dir]
                if dir < 3:
                    dir += 1
                else:
                    dir = 0
        cirq.pop()
        a = i
        b = j
        dir = 0
        while True:
            a = a + dy[dir]
            b = b + dx[dir]
            if -1 < a < R and -1 < b < C:
                mmm = cirq.popleft()
                if base[a][b] == -1:
                    break
                base[a][b] = mmm
            else:
                a -= dy[dir]
                b -= dx[dir]
                if dir < 3:
                    dir += 1
                else:
                    dir = 0
        flag = 1

dy = [-1, 1, 0, 0]  # 기본적인 4방향
dx = [0, 0, -1, 1]
dydy = [0, -1, 0, 1]  # 반시계 방향으로 서큘하는거
dxdx = [1, 0, -1, 0]
dydydy = []  # 시계방향으로 서큘하는거
dxdxdx = []
flag = 0  # 반시계 서큘 시계서큘인지 구분하는 플래그
R, C, T = map(int, input().split())
base = [[0]*C for _ in range(R)]
for i in range(R):
    base[i] = list(map(int, input().split()))
q = collections.deque()
mach = collections.deque()
base_copy = copy.deepcopy(base)
for i in range(R):
    for j in range(C):
        if base[i][j] > 0:
            q.append((i, j, base[i][j]))
        elif base[i][j] == -1:
            mach.append((i, j))


