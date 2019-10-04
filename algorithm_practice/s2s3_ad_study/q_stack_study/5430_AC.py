import sys
sys.stdin = open('ac.txt', 'r')


def R(aaaaa):
    aaaaa = aaaaa[::-1]
    return aaaaa


def D(numnum):
    global result
    if numnum == []:
        result = 'error'
        return
    numnum.pop(0)
    return

testcase = int(input())
for test_num in range(1, testcase+1):
    func = list(map(str, input()))
    N = int(input())
    lst = list(map(str, input()))
    numnum = []
    b = ''
    result = 1
    while lst:
        a = lst.pop(0)
        if a == '[' or a == ']':
            continue
        elif a == ',':
            b = int(b)
            numnum.append(b)
            b = ''
        else:
            b += a
    if b != '':
        b = int(b)
        numnum.append(b)
        b = ''
    for i in func:
        if i == 'R':
            numnum = R(numnum)
        elif i == 'D':
            D(numnum)
    if result == 'error':
        print(result)
    else:
        print(numnum)