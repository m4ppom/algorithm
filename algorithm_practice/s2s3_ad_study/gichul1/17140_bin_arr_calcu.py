import sys
sys.stdin = open('binbin.txt', 'r')
import collections


def R():
    global lenro, lenco, counter
    lenro = len(base)
    lenco = len(base[0])
    maxx = 0
    for ii in range(lenro):  # R정렬
        visited = [0] * 999
        q = collections.deque()
        qq = []
        for jj in range(lenco):
            if visited[base[ii][jj]] == 0 and base[ii][jj] != 0:
                q.append(base[ii][jj])
                visited[base[ii][jj]] += 1
            else:
                visited[base[ii][jj]] += 1
        lenq = len(q) * 2
        if lenq > maxx:
            if lenq >= 100:
                maxx = 100
            else:
                maxx = lenq
        while q:
            num = q.popleft()
            qq.append([visited[num], num])
        qq.sort()
        base[ii] = []
        numm = 0
        while qq:
            numm += 1
            if numm == 100:
                break
            soso = qq.pop(0)
            base[ii].append(soso[1])
            base[ii].append(soso[0])
    else:  # 0 붙이기
        for iii in range(lenro):
            lenbase = len(base[iii])
            if lenbase < maxx:
                nu = maxx - lenbase
                for _ in range(nu):
                    base[iii].append(0)
        counter += 1


def trans():
    global base, lenro, lenco
    lenro = len(base)
    lenco = len(base[0])
    base2 = [[0] * lenro for _ in range(lenco)]
    for ee in range(lenro):
        for rr in range(lenco):
            base2[rr][ee] = base[ee][rr]
    base = base2


r, c, k = map(int, input().split())
base = [0]*3
counter = 0
for i in range(3):
    base[i] = list(map(int, input().split()))
while counter < 101:
    lenro = len(base)
    lenco = len(base[0])
    if lenro-1 >= r-1 and lenco-1 >= c-1:
        if base[r-1][c-1] == k:
            break
    if lenro >= lenco:
        R()
    else:
        lenro = len(base)
        lenco = len(base[0])
        trans()
        lenro = len(base)
        lenco = len(base[0])
        R()
        if counter == 101:
            break
        lenro = len(base)
        lenco = len(base[0])
        trans()
        lenro = len(base)
        lenco = len(base[0])
        if lenro - 1 >= r - 1 and lenco - 1 >= c - 1:
            if base[r - 1][c - 1] == k:
                break
    lenro = len(base)
    lenco = len(base[0])
    if lenro-1 >= r-1 and lenco-1 >= c-1:
        if base[r-1][c-1] == k:
            break
    lenro = len(base)
    lenco = len(base[0])
    if lenro >= lenco:
        pass
    else:
        trans()
        R()
        if counter == 101:
            break
        trans()
        lenro = len(base)
        lenco = len(base[0])
        if lenro - 1 >= r - 1 and lenco - 1 >= c - 1:
            if base[r - 1][c - 1] == k:
                break
if counter > 100:
    print(-1)
else:
    print(counter)
