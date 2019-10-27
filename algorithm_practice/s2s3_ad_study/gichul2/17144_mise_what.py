import sys
sys.stdin = open('mise.txt', 'r')

import collections
import copy


def spreading(i, j, mise):
    # 4방향보면서 확산하는데 그 값을 카피본에 저장해서 나중에 한번에 바꿔줌
    # 바로바로 그냥 베이스에 바꿔주면 값 오류나니까. 동시에 확산된다고 생각
    global R, C
    mun_G = mise//5
    # 소수점 아래 없으니까 몫으로 구함
    for dir in range(4):
        ii = i+dy[dir]
        jj = j+dx[dir]
        if -1 < ii < R and -1 < jj < C:
            if base[ii][jj] != -1:
                base_copy[ii][jj] += mun_G
                base_copy[i][j] -= mun_G

def cirQulation(i, j):
    # flag가 0일 때 반시계방향 1일때 시계방향으로 사이드 돌아감
    global R, C, flag
    cirq = collections.deque()  # 사이드 도는 서클큐
    cirq.appendleft(0)
    temp = 0
    dir = 0
    a = i
    b = j
    if flag == 0:
        while temp != -1:
            a = a +dydy[dir]
            b = b +dxdx[dir]
            if -1 < a < R and -1 < b < C:  # 큐에 사이드 값 저장하고 한칸씩 밀어서 다시 저장
                cirq.append(base[a][b])
                temp = base[a][b]
            else:
                a -= dydy[dir]
                b -= dxdx[dir]
                if dir < 3:
                    dir += 1
                else:
                    dir = 0
        cirq.pop()
        a = i
        b = j
        dir = 0
        while True: # 위에서 구한 사이드값  넣어주는거 break로 멈춰줌
            a = a + dydy[dir]
            b = b + dxdx[dir]
            if -1 < a < R and -1 < b < C:
                mmm = cirq.popleft()
                if base[a][b] == -1:
                    break
                base[a][b] = mmm
            else:
                a -= dydy[dir]
                b -= dxdx[dir]
                if dir < 3:
                    dir += 1
                else:
                    dir = 0
        flag = 1  # 다음에 이 함수 들어올때는 반대방향으로 돌아야하니까 플래그
    else:
        while temp != -1:
            a = a +dydydy[dir]
            b = b +dxdxdx[dir]
            if -1 < a < R and -1 < b < C:
                cirq.append(base[a][b])
                temp = base[a][b]
            else:
                a -= dydydy[dir]
                b -= dxdxdx[dir]
                if dir < 3:
                    dir += 1
                else:
                    dir = 0
        cirq.pop()
        a = i
        b = j
        dir = 0
        while True:
            a = a + dydydy[dir]
            b = b + dxdxdx[dir]
            if -1 < a < R and -1 < b < C:
                mmm = cirq.popleft()
                if base[a][b] == -1:
                    break
                base[a][b] = mmm
            else:
                a -= dydydy[dir]
                b -= dxdxdx[dir]
                if dir < 3:
                    dir += 1
                else:
                    dir = 0
        flag = 0


dy = [-1, 1, 0, 0]  # 기본적인 4방향
dx = [0, 0, -1, 1]
dydy = [0, -1, 0, 1]  # 반시계 방향으로 서큘하는거
dxdx = [1, 0, -1, 0]
dydydy = [0, 1, 0, -1]  # 시계방향으로 서큘하는거
dxdxdx = [1, 0, -1, 0]
flag = 0  # 반시계 서큘 시계서큘인지 구분하는 플래그
R, C, T = map(int, input().split())
base = [[0]*C for _ in range(R)]
for i in range(R):
    base[i] = list(map(int, input().split()))
q = collections.deque()
time = 0
mach = collections.deque()
while time != T:
    base_copy = copy.deepcopy(base)
    mach = collections.deque()
    for i in range(R):
        for j in range(C):
            if base[i][j] > 0:
                if base[i][j] >= 5:
                    # 5보다 작으면 어차피 확산 안일어나니까 그만큼 안돌아도됨
                    spreading(i, j, base[i][j])
            elif base[i][j] == -1 and len(mach) != 2:
                # 가습기 크기만큼 잡아줌.
                mach.append((i, j))
                mach.append((i+1, j))
    else:
        base = base_copy  # 위에서 구한 값 베이스에 저장하고 서큘레이터 돌려줌
        qu, ququ = mach.popleft()
        cirQulation(qu, ququ)
        qu, ququ = mach.popleft()
        cirQulation(qu, ququ)
        time += 1
summ = 0
for nnn in range(R):
    summ += sum(base[nnn])
print(summ+2)
