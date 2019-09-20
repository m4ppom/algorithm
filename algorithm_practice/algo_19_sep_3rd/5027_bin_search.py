import sys
sys.stdin = open('bin_search.txt', 'r')
sys.setrecursionlimit(100000)


def finder(list, dir2):
    global number, cnt
    if len(list) == 1:
        if list[0] == number:
            cnt += 1
            return
        return
    if len(list) == 2:
        if list[0] == number:
            cnt += 1
        elif list[1] == number and dir2 == -1:
            return
        elif list[0] == number or list[1] == number:
            cnt += 1
        return
    mid = (len(list)-1)//2
    if list[mid] == number:
        cnt += 1
        return
    elif list[mid] < number:
        dir = -1
        if dir != dir2:
            finder(list[mid+1:], dir)
        else:
            return
    elif list[mid] > number:
        dir = 1
        if dir != dir2:
            # cnt += 1
            finder(list[:mid], dir)
        else:
            return
    else:
        number += 1
        return


testcase = int(input())
for test_num in range(1, testcase+1):
    dir = 0
    N, M = map(int, input().split())
    N_list = list(map(int, input().split()))
    N_list.sort()
    M_list = list(map(int, input().split()))
    cnt = 0
    for i in range(len(M_list)):
        number = M_list[i]
        finder(N_list, dir)
    print('#%d %d' % (test_num, cnt))