import sys
sys.stdin = open('inpu.txt', 'r')

#
# def right(node):
#     print(base[node - 1][1], end='')
#
#     return
#
# def inord(start):
#     print(base[start-1][1], end='')
#     for i in range(node_num):
#         if
#         if base[i][2] == str(start):
#             inord(i)
#             print(base[i][1], end='')
#     return
#
#
# def find(start):
#     global st_point
#     if base[start-1][2] == '0':
#         st_point = start
#         return
#     find(int(base[start-1][2]))
#
#
# testcase = 1
# for test_num in range(1, testcase+1):
#     print('#{} '.format(test_num), end='')
#     node_num = int(input())
#     base = [0]*node_num
#     st_point = 0
#     for i in range(node_num):
#         base[i] = list(map(str, input().split()))
#         if len(base[i]) == 3:
#             base[i].append('0')
#         elif len(base[i]) == 2:
#             base[i].append('0')
#             base[i].append('0')
#     print(base)
#     find(1)
#     print(st_point)
#     inord(st_point)
#     print()
#


def inord_traverse(T):
    if T:
        inord_traverse(tree[T][0])
        print('%s' % alpha[T], end='')
        inord_traverse(tree[T][1])


testcase = 10
for test_num in range(1, testcase+1):
    node_num = int(input())
    alpha = [0] * (node_num+1)
    tree = [[0] * 2 for _ in range(node_num + 1)]
    for aaa in range(node_num):
        temp = list(input().split())
        if len(temp)==3:
            temp.append('0')
        elif len(temp)==2:
            temp.append('0')
            temp.append('0')
        alpha[aaa + 1] = temp[1]
        for i in range(2, 4):  # 2, 3
            if temp[2]:
                parent, child = int(temp[0]), int(temp[2])
                tree[int(temp[0])][0] = int(temp[2])
            if temp[3]:
                parent, child = int(temp[0]), int(temp[3])
                tree[int(temp[0])][1] = int(temp[3])
    print('#{}'.format(test_num), end=' ')
    inord_traverse(1)
    print()
