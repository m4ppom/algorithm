import sys
sys.stdin = open('rope.txt', 'r')


q = []
N = int(input())
for i in range(N):
    q.append(int(input()))
q.sort()
bigbig = 0
for i in range(N):
    big = q[i]*(N-i)
    if bigbig < big:
        bigbig = big
print(bigbig)

