import sys
sys.stdin = open("inpu.txt","r")

testcase = int(input())
for num in range(1, testcase+1):
    stack = []
    stop = True
    string = list(input())
    while stop:
        for i in string:
            stack += i
            if len(stack) >= 2 and stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
        stop = False
    print('#{} {}'.format(num, len(stack)))

