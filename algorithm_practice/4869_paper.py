import sys
sys.stdin = open("inpu.txt", "r")

testcase = int(input())


def function(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    return function(n-1) + (function(n-2)*2)


for num in range(1,testcase+1):
    garo = int(input())
    # print(garo)
    sq = garo//10
    result = function(sq)

    print('#{} {}'.format(num, result))