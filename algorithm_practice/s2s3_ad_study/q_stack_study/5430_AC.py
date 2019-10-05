import sys
sys.stdin = open('ac.txt', 'r')

from collections import deque
testcase = int(input())
for test_num in range(1, testcase+1):
    func = deque(map(str, input()))
    N = int(input())
    if N == 0:
        input()
        lst = []
    else:
        lst = list(map(int, input()[1:-1].split((','))))
        b = ''
    result = 1
    rev = 0
    for i in func:
        if i == 'R':
            if rev == 0:
                rev = 1
            else:
                rev = 0
        elif i == 'D':
            if lst == []:
                result = 0
                print('error')
                break
            elif rev == 1:
                lst.pop(-1)
            elif rev == 0:
                lst.pop(0)
    if result == 1:
        if lst == []:
            print('[]')
        else:
            if rev == 1:
                lst = lst[::-1]
            print('[', end='')
            for i in range(len(lst)):
                print(lst[i],end='')
                if i != len(lst)-1:
                    print(',',end='')
            print(']')