import sys
sys.stdin = open('input0828.txt', 'r')

opener = ['(']
closer = [')']
op1 = ['+', '-']
op2 = ['*', '/']


def cal(a, b, ap):
    a = int(a)
    b = int(b)
    result = 0
    if ap == '+':
        result = a + b
    elif ap == '-':
        result = abs(a - b)
    elif ap == '*':
        result = a * b
    elif ap == '/':
        result = a // b
    return result


op = ['+', '-', '*', '/']


def cacacacaca(lst):
    while len(lst) != 1:
        for i in range(len(lst)):
            if lst[i] in op:
                a = lst.pop(i - 2)
                b = lst.pop(i - 2)
                c = lst[i - 2]
                lst[i - 2] = cal(a, b, c)
                print(lst)
                cacacacaca(lst)
                return


testcase = 1
# for test_num in range(1, testcase+1):
#
#     leng = int(input())
#     func = list(map(str, input()))
#     op_stack = []
#     num_stack = []
#     high_rank_stack = []
#     stack = []
#     open_cnt = 0
#     while len(func) > 0:
#         if func[0] in opener or func[0] in op1 or func[0] in op2:
#             if func[0] in op2:
#                 high_rank_stack += [[func[0], open_cnt]]
#                 func.pop(0)
#             elif func[0] in opener:
#                 open_cnt += 1
#                 print(open_cnt)
#                 op_stack += func[0]
#                 # print(op_stack)
#                 func.pop(0)
#             else:
#                 op_stack += func[0]
#                 # print(op_stack)
#                 func.pop(0)
#         elif func[0] in closer:
#             open_cnt -= 1
#             func.pop(0)
#             while len(op_stack) != 0:
#                 a = op_stack.pop()
#                 if a in opener:
#                     # if len(op_stack) > 0:
#                     #     b = op_stack.pop()
#                     #     num_stack += b
#                     break
#                 else:
#                     num_stack += a
#                     # print(num_stack)
#         else:  # 숫자면
#             num_stack += func[0]
#             func.pop(0)
#             if high_rank_stack:
#                 print(num_stack)
#                 print(high_rank_stack)
#                 print(open_cnt, high_rank_stack[-1][1] )
#                 print(high_rank_stack)
#                 if high_rank_stack[-1][1] == open_cnt:
#                     num_stack += high_rank_stack[-1][0]
#                     high_rank_stack.pop()
#     # stack += num_stack.pop(0)
#     print(num_stack)
    # while len(num_stack) != 0:
    #     stack += num_stack.pop(0)
    #     if stack[-1] in op1 or stack[-1] in op2:
    #         if stack[-2] == '(':
    #             stack.pop(-2)
    #             continue
    #         if stack[-3] == '(':
    #             stack.pop(-3)
    #             continue
    #         if stack[-1]=='+':
    #             stack[-3] = int(stack[-3]) + int(stack[-2])
    #             stack.pop()
    #             stack.pop()
    #         elif stack[-1] == '-':
    #             stack[-3] = int(stack[-3]) - int(stack[-2])
    #             stack.pop()
    #             stack.pop()
    #         elif stack[-1] == '*':
    #             stack[-3] = int(stack[-3]) * int(stack[-2])
    #             stack.pop()
    #             stack.pop()
    #         elif stack[-1] == '/':
    #             stack[-3] = int(stack[-3]) / int(stack[-2])
    #             stack.pop()
    #             stack.pop()
    a = cacacacaca(num_stack)
    print(num_stack)
    # print('#{} {}'.format(test_num, stack[0]))


