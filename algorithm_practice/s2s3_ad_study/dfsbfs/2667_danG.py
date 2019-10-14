import sys
sys.stdin=open('danG.txt', 'r')


def dfs(a, b):
    global cnt, num, rocol
    base[a][b] = cnt
    num += 1
    for dir in range(4):
        aa = a+dy[dir]
        bb = b+dx[dir]
        if -1 < aa < rocol and -1 < bb < rocol:
            if base[aa][bb] == 1:
                dfs(aa, bb)


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
rocol = int(input())
base = [0]*rocol
cnt = 1
num = 0
num_list = []
for i in range(rocol):
    base[i] = list(map(int, input()))
for ii in range(rocol):
    for jj in range(rocol):
        if base[ii][jj] == 1:
            cnt += 1
            dfs(ii, jj)
            num_list.append(num)
            num = 0
print(cnt-1)
num_list.sort()
for nn in range(len(num_list)):
    print(num_list[nn])