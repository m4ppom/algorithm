import sys
import collections
import copy
sys.stdin = open('reward.txt', 'r')

import copy
def moneymoney(list):
    money = 0
    for i in range(len(list)-1, -1, -1):
        money += list[i] * (10**(len(list)-1-i))
    return money


def swapswap(i, j):
    # print(maximoney)
    global cntcnt, maximoney, remember, absolute, cnt
    if maximoney == absolute:
        # cnt.append(cntcnt)
        return
    if cntcnt > M:
        return
    b[i], b[j] = b[j], b[i]
    for eoeoeo in range(len(b)):
        if b[eoeoeo] > remember[eoeoeo]:
            money = moneymoney(b)
            if maximoney <= money:
                maximoney = money
                if maximoney == absolute:
                    cnt = cntcnt
                remember = copy.deepcopy(b)
                break
        elif b[eoeoeo] == remember[eoeoeo]:
            pass
        else:
            break
    for x in range(len(b)):
        for y in range(len(b)):
            if x != y:
                cntcnt += 1
                swapswap(x, y)
                cntcnt -= 1
    b[i], b[j] = b[j], b[i]


testcase = int(input())
for test_num in range(1, testcase+1):
    N, M = list(map(int, input().split()))
    b = list(map(int, str(N)))
    # print(b)
    c = sorted(b, reverse=True)
    absolute = moneymoney(c)
    maximoney = moneymoney(b)
    remember = [0]*len(b)
    cnt = 0
    for i in range(len(b)):
        for j in range(len(b)):
            if i == j:
                continue
            cntcnt = 0
            cntcnt += 1
            swapswap(i, j)
            cntcnt -= 1
    # print(cnt)
    if cnt != 0 and cnt < M:
        num = M - cnt
        for breakbreakbreak in range(num):
            remember[-1], remember[-2] = remember[-2], remember[-1]
        a = moneymoney(remember)
        print('#%d %d' % (test_num, a))
    else:
        print('#%d %d' % (test_num, maximoney))
# def moneymoney(list):
#     money = 0
#     for i in range(len(list)-1, -1, -1):
#         money += list[i] * (10**(len(list)-1-i))
#     return money
# testcase = int(input())
# for test_num in range(1, testcase + 1):
#     N, M = list(map(int, input().split()))
#     b = list(map(int, str(N)))
#     b.sort(reverse=True)
#     maximoney = moneymoney(b)
#     print('#%d %d' %(test_num, maximoney))