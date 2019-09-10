import sys
sys.stdin = open('inpu.txt', 'r')


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
        result = a//b
    return result


def post_traverse(T):
    global lst, tem, tem2
    if T:
        post_traverse(tree[T][1])
        post_traverse(tree[T][2])
        lst.append(alpha[T])
        # if len(lst) == 3:
        #     alpha[T] = cal(lst[0], lst[1], lst[2])
        #     tem = T
        #     lst = []
        # elif len(lst) == 2 and tem != 0:
        #     alpha[T] = cal(alpha[tem], lst[0], lst[1])
        #     tem2 = T
        #     print(alpha[T], end='')
        # elif len(lst) == 1 and tem != 0 and tem2 != 0:
        #     alpha[T] = cal(alpha[tem2], alpha[tem], lst[0])
        aaa.append(alpha[T])
        # print(aaa)
        # print('%s' % alpha[T], end='')


op = ['+', '-', '*', '/']


def cacacacaca(lst):
    while len(lst) != 1:
        for i in range(len(lst)):
            if lst[i] in op:
                a = lst.pop(i-2)
                b = lst.pop(i-2)
                c = lst[i-2]
                lst[i-2] = cal(a, b, c)
                cacacacaca(lst)
                return


testcase = 10
for test_num in range(1, testcase+1):
    node_num = int(input())
    alpha = [0] * (node_num+1)
    tree = [[0] * 3 for _ in range(node_num + 1)]
    for aaa in range(node_num):
        temp = list(input().split())
        # if len(temp) == 3:
        #     temp.append('0')
        if len(temp) == 2:
            temp.append('0')
            temp.append('0')
        alpha[aaa + 1] = temp[1]
        for i in range(2, 3):  # 2, 3
            if temp[2]:
                parent, child1, child2 = int(temp[0]), int(temp[2]), int(temp[3])
                tree[int(temp[0])][0] = int(temp[0])
                tree[int(temp[0])][1] = int(temp[2])
                tree[int(temp[0])][2] = int(temp[3])
            else:
                continue
    aaa = []
    lst = []
    tem = 0
    tem2 = 0
    print('#{}'.format(test_num), end=' ')
    post_traverse(1)
    cacacacaca(aaa)
    print(aaa[0])