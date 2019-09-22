import sys
sys.stdin = open('mes_input.txt', 'r')


mes_num, consumer = map(int, input().split())
base = [0]*mes_num
base_con = [0] * consumer
for i in range(mes_num):
    base[i] = int(input())
time = 0
while 1:
    time += 1
    for i in range(len(base)):
        for j in range(len(base_con)):
            if base_con[j] == 0:
                base_con[j] = base.pop(0)
        break
    for i in range(len(base_con)):
        if base_con[i] == 0:
            continue
        base_con[i] -= 1
    if sum(base_con) == 0:
        break
print(time)