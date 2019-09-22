import sys
sys.stdin = open('brown.txt', 'r')


N = int(input())
bus = list(map(int, input().split()))
maxi = 0
cnt = 0
for i in range(len(bus)):
    if bus[i] == 0:
        cnt += 1
    else:
        if maxi < cnt:
            maxi = cnt
print(maxi//2)