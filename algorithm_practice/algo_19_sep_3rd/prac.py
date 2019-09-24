import sys
sys.setrecursionlimit(100000)
import itertools

#
# def swap(k, i):
#     temp = array[k]
#     array[k] = array[i]
#     array[i] = temp
#     return
#
#
# def perm(n, k):
#     if k == n:
#         print(array)
#         return
#     else:
#         for i in range(k, n):
#             swap(k, i)
#             perm(n, k+1)
#             # print(array)
#             swap(k, i)
#             # print(array)
#         # print(array)
#
#
# array = [1, 2, 3]
# array2 = [6, 6, 7, 7, 6, 7]
# array3 = [1, 0, 1, 1, 2, 3]
# perm(3, 0)
#
# arr = [3, 6, 7, 1, 5, 4]
# n = len(arr)
#
# for i in range(0, (1 << n)):
#     for j in range(0, n):
#         if i & (1 << j):
#             print('{}'.format(arr[j]), end=' ')
#     print()
#
#
# arr_list = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
# temp_list = [0]*len(arr_list)
#
#
# def combination(n, r):
#     global temp_list
#     if r == 0:
#         if sum(temp_list) == 0:
#             a = sorted(temp_list)
#             if a not in new:
#                 new.append(a)
#             for i in range(len(temp_list)):
#                 if temp_list[i] != 0:
#                     print(temp_list[i], end=' ')
#             print()
#     elif n < r:
#         return
#     else:
#         temp_list[r-1] = arr_list[n-1]
#         combination(n-1, r-1)
#         combination(n-1, r)
#
#
# new = []
# for i in range(1, len(temp_list)+1):
#     combination(len(arr_list), i)
# print(len(new), new)
#
#
# def comb(n, r):
#     global res
#     if r == 0:
#         res += 1
#         return
#     elif r == n:  # 이거넣으면 아래 추가해주는 부분 추가해줘야하고 리턴 아니면 한개 안들어감
#         res += 1
#         return
#     elif n < r:
#         res += 1
#         return
#     else:
#         comb(n-1, r-1)
#         comb(n-1, r)
#
# res = 0
# comb(5, 2)
# print(res)
# aa = list(itertools.combinations(arr_list, 3))
# print(aa)
#
#
# def quicksort(lst, l, r):
#     if l < r:
#         s = partition(lst, l, r)
#         quicksort(lst, l, s-1)
#         quicksort(lst, s+1, r)
#
#
# def partition(lst, l, r):
#     p = lst[l]
#     i = l
#     j = r
#     while i <= j:
#         while i<r and lst[i] <= p:
#             i += 1
#             # if i == r:
#             #     break
#         while i > l and lst[j] >= p:
#             j -= 1
#             # if j == 0:
#             #     break
#         if i < j:
#             print(lst)
#             lst[i], lst[j] = lst[j], lst[i]
#             print(lst)
#     print(lst)
#     lst[l], lst[j] = lst[j], lst[l]
#     print(lst)
#     return j
#
#
# def lomuto(lst, p, r):
#     x = lst[r]
#     i = p -1
#     for j in range(p, r):
#         if lst[j] <= x:
#             i += 1
#             lst[i], lst[j] = lst[j], lst[i]
#
#     lst[i+1], lst[r] = lst[r], lst[i+1]
#     return lomuto(lst, p+1, r)
#
#
# lst =[11, 45, 23, 81, 28, 34]
# lst2 = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
# lst = [11, 45, 22, 81, 23, 34, 99, 22, 17, 8]
#
#
# quicksort(lst, 0, len(lst)-1)
# print('sss', lst)
#
#
# def finder(idx, summ):
#     if summ > 10 or idx > len(a):
#         return
#     elif summ == 10:
#         print(mm)
#         return
#     else:
#         summ += a[idx]
#         mm.append(a[idx])
#         finder(idx + 1, summ)
#         mm.pop(-1)
#         summ -= a[idx]
#
#     # finder(idx + 1, summ)
# mm = []
# a = [1, 2, 3, 4, 5 , 6, 7, 8, 9, 10]
# finder(0, 0)
#
# def backtrack(a, k, input):
#     c[MAXCANDIDATES]
#     ncands
#     if k == input:
#         process_solution(a, k)
#     else:
#         k += 1
#         make_candidates(a, k, input, c, ncands)
#         for i in range(ncands):
#             a[k] += c[i]
#             backtrack(a, k , input)
#
# def make_candidates(a, k, n, c, ncands):
#     c[0] = True
#     c[1] = False
#     ncands = 2
#
# def process_solution(a, k):
#     for i in range(1, k+1):
#         if a[i] == True:
#             print(i)




def preorder_traverse(T):
    if T:
        print("%d" % T, end=' ')
        preorder_traverse(tree[T][0])
        preorder_traverse(tree[T][1])


def inorder_traverse(T):
    if T:
        inorder_traverse(tree[T][0])
        print("%d" % T, end=' ')
        inorder_traverse(tree[T][1])


def postorder_traverse(T):
    if T:
        postorder_traverse(tree[T][0])
        postorder_traverse(tree[T][1])
        print("%d" % T, end=' ')


n = 12
# n = int(input())
tree = [[0] * 2 for _ in range(n + 1)]

# templ = list(map(int, input().split()))
templ = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]

for i in range(len(templ) // 2):
    parent, child = templ[i * 2], templ[i * 2 + 1]
    if not tree[parent][0]:
        tree[parent][0] = child
    else:
        tree[parent][1] = child

# preorder_traverse(1)
# print(tree)
# print()
# inorder_traverse(1)
# print()
postorder_traverse(1)
print()

def finder(start):
    global N, summ, mini
    if start == N:
        if mini > summ:
            mini = summ
        return
    visited[start] = 1
    for i in range(N+1):
        if base[start][i] != 0 and visited[i] == 0:
            visited[i] = 1
            summ += base[start][i]
            finder(i)
            summ -= base[start][i]
            visited[i] = 0


testcase = int(input())
for test_num in range(1, testcase + 1):
    N, M = map(int, input().split())
    base=[[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        base[a][b] = c
    mini = 9900000
    for i in range(N+1):
        visited = [0]*(N+1)
        summ = 0
        visited[i] = 1
        finder(i)
    print('#%d %d' % (test_num, mini))

