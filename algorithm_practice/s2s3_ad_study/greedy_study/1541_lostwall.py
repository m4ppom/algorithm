import sys
sys.stdin = open('lostwall.txt', 'r')

import collections
q = collections.deque()
a = list(map(str, input()))
n = len(a)
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
c = ''
p = []
for i in range(n):
    b = a.pop(0)
    if b in num:
        c += b
    else:
        p += [int(c)]
        p += b
        c = ''
else:
    p += [int(c)]
# print(p)
mi = ['-']
pl = ['+']
while len(p) != 1:
    for i in range(len(p)):
        if p[i] == '+':
            plus_num = p[i-1] + p[i+1]
            p[i-1] = plus_num
            p.pop(i)
            p.pop(i)
            break
    if '+' in p:
        continue
    elif '-' in p:
        for i in range(len(p)):
            if p[i] == '-':
                plus_num = p[i - 1] - p[i + 1]
                p[i - 1] = plus_num
                p.pop(i)
                p.pop(i)
                break
print(p[0])
