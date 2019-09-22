import sys
sys.stdin = open('res_room.txt', 'r')


N = int(input())
base = [0]*N
for i in range(N):
    base[i] = list(map(int, input().split()))
    base[i].sort(reverse = True)
base.sort(reverse = True)
res_room = [[0]*151 for _ in range(N)]
num = 0
stop = 0
for i in range(len(base)):
    stop = 0
    while stop != 1:
        for j in range(base[i][0], base[i][1], -1):
            if res_room[num][j] == 0:
                if j == base[i][1]+1:
                    for k in range(base[i][0], base[i][1], -1):
                        res_room[num][k] += 1
                    num = 0
                    stop = 1
                continue
            elif res_room[num][j] != 0:
                num += 1
                break
cnt = 0
for i in range(len(res_room)):
    if sum(res_room[i]) != 0:
        cnt += 1
    else:
        break
print(cnt)