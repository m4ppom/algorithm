import sys
sys.stdin = open('cook.txt', 'r')

import collections
import itertools


def CnullG_calculator(lst1, lst2):
    global N, minimi
    sumA = 0
    sumB = 0
    for _ in lst1:
        for __ in lst1:
            if _ == __:
                continue
            else:
                sumA += base[_][__]
    for _ in lst2:
        for __ in lst2:
            if _ == __:
                continue
            else:
                sumB += base[_][__]
    cha = abs(sumA - sumB)
    if cha < minimi:
        minimi = cha
    return


def CnullG_finder():
    # glob
    global N, minimi
    if len(cosA) == N//2 and len(cosB) == N//2:
        CnullG_calculator(cosA, cosB)
    else:
        if len(cosA) != N//2:
            for i in range(N):
                if vztd[i] == 0:
                    vztd[i] = 1
                    cosA.append(i)
                    CnullG_finder()
                    cosA.pop()
                    vztd[i] = 0
                else:
                    continue
        else:
            for i in range(N):
                if vztd[i] == 0:
                    vztd[i] = 1
                    cosB.append(i)
                    CnullG_finder()
                    cosB.pop()
                    vztd[i] = 0
                else:
                    continue


testnum = int(input())
for testcase in range(1, testnum+1):
    N = int(input())
    base = [0]*N
    cosA = []
    cosB = []
    vztd = [0]*N
    minimi = 10000000
    for _ in range(N):
        base[_] = list(map(int, input().split()))
    # for i in range(N):
    #     vztd[i] = 1
    #     cosA.append(i)
    #     CnullG_finder()
    #     cosA.pop()
    #     vztd[i] = 0
    lst = [_ for _ in range(N)]

    a = list(itertools.combinations(lst, N//2))
    for i in range(len(a)):
        idx = 0
        inb = 0
        b = [0] * (N // 2)
        aa = [0] * (N // 2)
        for _ in range(N):
            if idx < N//2:
                if a[i][idx] == _:
                    aa[idx] = _
                    idx += 1
                else:
                    b[inb] = _
                    inb += 1
            else:
                b[inb] = _
                inb += 1
        CnullG_calculator(aa, b)
    print('#%d %d' %(testcase, minimi))