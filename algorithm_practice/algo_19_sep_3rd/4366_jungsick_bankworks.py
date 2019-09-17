import sys

sys.stdin = open('jungsick.txt', 'r')

import copy
def fixbin(binary):
    for i in range(len(binary)):
        a = copy.deepcopy(binary)
        if binary[i] == 0:
            a[i] = 1
            bin_list.append(a)
        else:
            a[i] = 0
            bin_list.append(a)


def fixtri(triary):
    for i in range(len(triary)):
        a = copy.deepcopy(triary)
        b = copy.deepcopy(triary)
        if triary[i] == 0:
            a[i] = 1
            tri_list.append(a)
            b[i] = 2
            tri_list.append(b)
        elif a[i] == 1:
            a[i] = 0
            tri_list.append(a)
            b[i] = 2
            tri_list.append(b)
        else:
            a[i] = 0
            tri_list.append(a)
            b[i] = 1
            tri_list.append(b)


testcase = int(input())
for test_num in range(1, testcase+1):
    binary = list(map(int,input()))
    triary = list(map(int,input()))
    bin_list = []
    tri_list = []
    fixbin(binary)
    fixtri(triary)
    binbin = []
    tritri = []
    # print(bin_list, tri_list)
    for i in range(len(bin_list)):
        summ = 0
        for j in range(len(bin_list[0])):
            summ += bin_list[i][j]*(2**(len(bin_list[0])-j-1))
        binbin.append(summ)
    for i in range(len(tri_list)):
        summ = 0
        for j in range(len(tri_list[0])):
            summ += tri_list[i][j]*(3**(len(tri_list[0])-j-1))
        tritri.append(summ)
    for i in range(len(binbin)):
        for j in range(len(tritri)):
            if binbin[i] == tritri[j]:
                print('#{} {}'.format(test_num, binbin[i]))
