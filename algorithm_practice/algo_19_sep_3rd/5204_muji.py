import sys
sys.stdin = open('muji.txt', 'r')
sys.setrecursionlimit(100000)

def div(lst):
    global cnt
    if len(lst) <= 2:
        if len(lst) == 1 or len(lst) == 0:
            return lst
        elif lst[0] > lst[1]:
            lst[0], lst[1] = lst[1], lst[0]
            cnt += 1
            return lst
    a = lst[:len(lst)//2]
    b = lst[len(lst)//2:]
    # if a[-1] > b[-1]:
    #     cnt += 1
    a = div(a)
    b = div(b)
    return merging(a, b)


def merging(left, right):
    global cnt
    if left[-1] > right[-1]:
        cnt += 1
    result = left + right
    result.sort()
    return result


def merge_sort(list_m):
    if len(list_m) == 1:
        return list_m
    left = []
    right = []
    middle = len(list_m) // 2
    for x in range(middle):
        left.append(list_m[x])
    for x in range(middle, len(list_m)):
        right.append(list_m[x])
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        elif len(left) > 0:
            result.append(left.pop(0))
        elif len(right) > 0:
            result.append(left.pop(0))
    return result


testcase = int(input())
for test_num in range(1, testcase+1):
    cnt = 0
    num = int(input())
    base = list(map(int, input().split()))
    a = div(base)
    # merge_sort(base)
    print('#%d %d %d' % (test_num, a[len(a) // 2], cnt))





