import sys
import itertools
sys.stdin = open('sunban.txt', 'r')


# testcase = int(input())
# for test_num in range(1, testcase+1):
#     N, M = map(int, input().split())
#     num_list = list(map(int, input().split()))
#     gap = 1000000
#     for i in range(len(num_list)+1):
#         a = list(itertools.combinations(num_list, i))
#         # print(a)
#         for j in range(len(a)):
#             if sum(a[j]) >= M:
#                 if gap > sum(a[j]) - M >= 0:
#                     gap = sum(a[j]) - M
#     print('#%d %d' %(test_num, gap))


def swap(k, i):
    temp = array[k]
    array[k] = array[i]
    array[i] = temp
    return


def perm(n, k):
    global gap
    if k == n:
        print(array)
        if gap > sum(array) - M >= 0:
            gap = sum(array) - M
        # print(array)
        return
    else:
        for i in range(k, n):
            swap(k, i)
            perm(n, k+1)
            # print(array)
            swap(k, i)
            # print(array)
        # print(array)

testcase = int(input())
for test_num in range(1, testcase+1):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    gap = 1000000
    for i in range(len(num_list)):
        # perm(len(num_list), i)
        array = num_list[:i+1]
        perm(i, 0)
        if gap == 0:
            break
        # a = list(itertools.combinations(num_list, i))
        # print(a)
        # for j in range(len(a)):
        #     if sum(a[j]) >= M:
        #         if gap > sum(a[j]) - M >= 0:
        #             gap = sum(a[j]) - M
    print('#%d %d' %(test_num, gap))

array = [1, 2, 3]
array2 = [6, 6, 7, 7, 6, 7]
array3 = [1, 0, 1, 1, 2, 3]
perm(3, 0)

