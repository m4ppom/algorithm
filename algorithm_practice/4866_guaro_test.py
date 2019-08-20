import sys
sys.stdin = open("inpu.txt", "r")

testcase = int(input())
find_list = ['(',')','{','}','[',']']
stack = []
for test_no in range(1, testcase+1):
    sting_list = list(input())
    for i in sting_list:
        if i in find_list:
            stack += i
    summ = 0
    summm = 0
    for _ in range(len(stack)):
        a = stack.pop()
        if len(stack) != 0:
            b = stack[-1]

        if summ < 0 or summm < 0:
            result = 0
            break

        elif a == ')':
            summ += 1000
        elif a == '(':
            summ -= 1000
        elif a == '}':
            summm += 1
        elif a == '{':
            summm -= 1
        if len(stack):
            if a == ')' and b == '{':
                result = 0
                break
            elif a == '}' and b == '(':
                result = 0
                break
    if summm == 0 and summ == 0:
        result = 1
    else:
        result = 0

    print('#{} {}'.format(test_no, result))


# T = int(input())
# for tc in range(1, T+1):
#     s = input()
#
#     stack = []
#
#     # for i in s:
#     for i in range(len(s)):
#         if s[i] == '(' or s[i] == '{':
#             stack.append(s[i])
#         elif s[i] == ')' or s[i] == '}':
#             if len(stack) == 0:
#                 result = 0
#                 break
#             else:
#                 if s[i] == ')':
#                     t = stack[-1]
#                     stack.pop(-1)
#                     if t == '(':
#                         continue
#                     else:
#                         result = 0
#                         break
#                 elif s[i] == '}':
#                     t = stack[-1]
#                     stack.pop(-1)
#                     if t == '{':
#                         continue
#                     else:
#                         result = 0
#                         break
#     else:
#         if len(stack) == 0:
#             result = 1
#         else:
#             result = 0
#
#     print('#{} {}'.format(tc, result))