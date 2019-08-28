import sys
sys.stdin = open('input0828.txt', 'r')

#
# def calculate(num1, num2, ope):
#     global result
#     if ope == '+':
#         result = num1 + num2
#     elif ope == '-':
#         result = num1 - num2
#     elif ope == '*':
#         result = num1 * num2
#     elif ope == '/':
#         result = num1 // num2
#     else:
#         result = 'error'
#         return result
#     if type(result) != int:
#         result = 'error'
#     return result
#
#
#
#
# testcase = int(input())
# for tc_num in range(1, testcase + 1):
#     post_fix = input().split()
#     post_fix.pop()
#     op = ['+', '-', '*', '/']
#     oper = [0]*256
#     op_top = 0
#     numb = [0]*256
#     numb_top = 0
#     if len(post_fix) == 0:
#         result = 'error'
#     while len(post_fix) != 1:
#         for i in range(len(post_fix)):
#             if post_fix[i] in op:
#                 if i == 1 or i == 0:
#                     result = 'error'
#                     break
#                 else:
#                     post_fix[i - 2] = calculate(int(post_fix[i - 2]), int(post_fix[i - 1]), post_fix[i])
#                     post_fix.pop(i)
#                     post_fix.pop(i-1)
#                     break
#             else:
#                 continue
#         if result == 'error':
#             break
#     print('#{} {}'.format(tc_num, result))

T = int(input())
for tc in range(1, T+1):
    L = list(map(str, input().split()))
    O = ['+', '-', '*', '/', '.']
    stack = []
    res = 0
    j = 0
    f = 1
    e = 0
    while f:
        for i in L:
            if i not in O:
                stack.append(i)
                j += 1
            elif i == '.':
                if len(stack)==1:
                    res = stack.pop()
                    f = 0
                    break
                else:
                    e = 1
                    f = 0
                    break
            else:
                if i == '*':
                    if len(stack) > 1:
                        tmp1 = int(stack.pop(j-1))
                        tmp2 = int(stack.pop(j-2))
                        res = tmp1 * tmp2
                        stack.append(res)
                        j -= 1
                    else:
                        e = 1
                        f = 0
                        break
                if i == '+':
                    if len(stack) > 1:
                        tmp1 = int(stack.pop(j-1))
                        tmp2 = int(stack.pop(j-2))
                        res = tmp1 + tmp2
                        stack.append(res)
                        j -= 1
                    else:
                        e = 1
                        f = 0
                        break
                if i == '-':
                    if len(stack) > 1:
                        tmp1 = int(stack.pop(j-1))
                        tmp2 = int(stack.pop(j-2))
                        res = tmp2 - tmp1
                        stack.append(res)
                        j -= 1
                    else:
                        e = 1
                        f = 0
                        break
                if i == '/':
                    if len(stack) > 1:
                        tmp1 = int(stack.pop(j-1))
                        tmp2 = int(stack.pop(j-2))
                        res = tmp2 // tmp1
                        stack.append(res)
                        j -= 1
                    else:
                        e = 1
                        f = 0
                        break
    if e:
        print('#%d' % (tc), 'error')
    else:
        print('#%d %d' % (tc, res))


