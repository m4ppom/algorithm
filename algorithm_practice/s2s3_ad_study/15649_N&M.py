import sys
sys.stdin = open('N&M1.txt','r')
# import copy
# import itertools
# #
#
# def perm(n, k, M):
#     if k == n:
#         for i in range(len(array)):
#             a = copy.deepcopy(array)
#             new.append(a)
#         return
#     else:
#         for i in range(k, n):
#             array[k], array[i] = array[i], array[k]
#             perm(n, k+1, M)
#             array[k], array[i] = array[i], array[k]
#
#
# N, M = map(int,input().split())
# array = []
# for i in range(1, N+1):
#     array.append(i)
# new = []
# # perm(len(array), 0, M)
# new.sort()
# ans = []
# a = list(itertools.permutations(N, M))
# print(a)
# for cc in range(len(new)):
#     if new[cc][:M] not in ans:
#         ans.append(new[cc][:M])
# for j in range(len(ans)):
#     for i in range(len(ans[0])):
#         print(ans[j][i], end=' ')
#     print()

def fider(index, N, M):
    if index == M:
        if sorted(a)==a:
            for i in range(M):
                print(a[i], end=' ')
            print()
        return
    for i in range(1, N + 1):
        # if visited[i]:
        #     continue
        # if i > index:
        #     return
        # visited[i] = 1
        a[index] = i
        fider(index + 1, N, M)
        # visited[i] = 0
N, M = map(int, input().split())
visited = [0] * (N + 1)
a = [0] * M
fider(0, N, M)