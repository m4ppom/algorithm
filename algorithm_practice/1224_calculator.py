import sys
sys.stdin = open('input0828.txt', 'r')

opener = ['(']
closer = [')']
op1 = ['+','-']
op2 = ['*','/']
testcase = 10
for test_num in range(1, testcase+1):

    leng = int(input())
    func = list(map(str, input()))
    op_stack = []
    num_stack = []
    stack = []
    while len(func) > 0:
        if func[0] in opener or func[0] in op1 or func[0] in op2:
            op_stack += func[0]
            # print(op_stack)
            func.pop(0)
        elif func[0] in closer:
            func.pop(0)
            while len(op_stack) != 0:
                a = op_stack.pop()
                if a in opener:
                    if len(op_stack) > 0:
                        b = op_stack.pop()
                        num_stack += b

                    break
                else:
                    num_stack += a
                    # print(num_stack)
        else:
            num_stack += func[0]
            func.pop(0)
    stack += num_stack.pop(0)
    print(num_stack)
    while len(num_stack) != 0:
        stack += num_stack.pop(0)
        if stack[-1] in op1 or stack[-1] in op2:
            if stack[-2] == '(':
                stack.pop(-2)
                continue
            if stack[-3] == '(':
                stack.pop(-3)
                continue
            if stack[-1]=='+':
                stack[-3] = int(stack[-3]) + int(stack[-2])
                stack.pop()
                stack.pop()
            elif stack[-1] == '-':
                stack[-3] = int(stack[-3]) - int(stack[-2])
                stack.pop()
                stack.pop()
            elif stack[-1] == '*':
                stack[-3] = int(stack[-3]) * int(stack[-2])
                stack.pop()
                stack.pop()
            elif stack[-1] == '/':
                stack[-3] = int(stack[-3]) / int(stack[-2])
                stack.pop()
                stack.pop()
    print('#{} {}'.format(test_num, stack[0]))


