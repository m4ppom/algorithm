import sys
sys.stdin = open('desum.txt','r')


import collections

# N = int(input())
# number = collections.deque()
# nunu = N
# cnt = 0
# while nunu != 0:
#     cnt += 1
#     a = nunu % 10
#     nunu = nunu // 10
#     number.appendleft(a)
# print(number)
# print(cnt)
# leng = len(number)
# for i in range(1, cnt*9 + 1):
#     a = N - i
#     for j in range(leng):
N = str(input())
leng = len(N)
intN = int(N)
numq = collections.deque()
result = 0
if leng == 1:
    for i in range(0, intN):
        a = intN - i
        if 2*a == intN:
            result = a
else:
    for i in range(leng*9+1, 0, -1):
        a = intN - i
        if a < 0:
            continue
        stra = str(a)
        if len(stra) == leng:
            for i in stra:
                numq.append(int(i))
        else:
            for i in stra:
                numq.append(int(i))
            numq.appendleft(0)
        if a + sum(numq) == intN:
            result = a
            break
        else:
            numq = collections.deque()
print(result)
#
#
# N = str(input())
# leng = len(N)
# intN = int(N)
# numq = []
# result = 0
# for i in range(leng*9+1, 0, -1):
#     a = intN - i
#     stra = str(a)
#     for i in stra:
#         numq.append(int(i))
#     if a + sum(numq) == intN:
#         result = a
#         break
#     else:
#         numq = []
# print(result)
#

