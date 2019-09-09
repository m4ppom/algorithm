import sys
sys.stdin = open('inpu.txt', 'r')


def tr(a, b):
    if a not in result:
        result.append(a)
    if b not in result:
        result.append(b)
    if b not in info:
        return
    else:
        idx = info.index(b)
    if info:
        c = info.pop(idx)
        d = info.pop(idx)
        tr(c, d)
        tr(c, d)
        # return


node_num = int(input())
info = list(map(int, input().split()))
result = []
# info.index(99)
while info:
    a = info.pop(0)
    b = info.pop(0)
    tr(a, b)
print(result)
print(info)


def preorder(t):
    if t:
        visit(t)
        preorder(t.left)
        preorder(t.right)


visit = [0] * node_num

'''
13 ← 정점의 개수
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''


import sys
sys.stdin = open("input.txt", "r")


def preorder_traverse(T):
    if T:
        print("%d" % T, end=' ')
        preorder_traverse(tree[T][0])
        preorder_traverse(tree[T][1])


n = int(input())
tree = [[0] * 2 for _ in range(n + 1)]

templ = list(map(int, input().split()))

for i in range(len(templ) // 2):
    parent, child = templ[i * 2], templ[i * 2 + 1]
    if not tree[parent][0] :
        tree[parent][0] = child
    else:
        tree[parent][1] = child

preorder_traverse(1)
print()

