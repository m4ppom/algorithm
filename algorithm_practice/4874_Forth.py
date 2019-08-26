import sys
sys.stdin = open('inpu.txt', 'r')


def calculate(num1, num2, ope):
    global result
    if ope == '+':
        result = num1 + num2
    elif ope == '-':
        result = num1 - num2
    elif ope == '*':
        result = num1 * num2
    elif ope == '/':
        result = num1 // num2
    else:
        result = 'error'
        return result
    if type(result) != int:
        result = 'error'
    return result




testcase = int(input())
for tc_num in range(1, testcase + 1):
    post_fix = input().split()
    post_fix.pop()
    op = ['+', '-', '*', '/']
    oper = [0]*256
    op_top = 0
    numb = [0]*256
    numb_top = 0
    if len(post_fix) == 0:
        result = 'error'
    while len(post_fix) != 1:
        for i in range(len(post_fix)):
            if post_fix[i] in op:
                if i == 1 or i == 0:
                    result = 'error'
                    break
                else:
                    post_fix[i - 2] = calculate(int(post_fix[i - 2]), int(post_fix[i - 1]), post_fix[i])
                    post_fix.pop(i)
                    post_fix.pop(i-1)
                    break
            else:
                continue
        if result == 'error':
            break
    print('#{} {}'.format(tc_num, result))
