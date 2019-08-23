# sik = input().split()
# stack = []
# result = []
# fourchic= ['+', '-', '*', '/']
# guaro = ['(', ')']
# for i in sik:
#     if i in fourchic:
#         stack.append(i)
#     elif i == guaro[1]:
#         while len(stack) != 0:
#             result.append(stack.pop())
#     elif i == guaro[0]:
#         stack.append(i)
#         stack.pop()
#     else:
#         result.append(i)
#
# while len(stack) != 0:
#     result.append(stack.pop())
# print(result)

# def backtrack(a, k, input):
#     global MAXCANDIDATES
#     c = [0] * MAXCANDIDATES
#
#     if k == input:
#         for i in range(1, k+1):
#             print(a[i], end=' ')
#         print()
#     else:
#         k += 1
#         ncandidates = construct_candidates(a, k, input, c)
#         for i in range(ncandidates):
#             a[k] = c[i]
#             backtrack(a, k, input)
#
# def construct_candidates(a, k ,input, c):
#     in_perm = [False] * NMAX
#
#     for i in range(1, k):
#         in_perm[a[i]] = True
#
#     ncandidates = 0
#     for i in range(1, input+1):
#         if in_perm[i] == False:
#             c[ncandidates] = i
#             ncandidates += 1
#     return ncandidates
#
# MAXCANDIDATES = 100
# NMAX = 100
# a = [0] * NMAX
# backtrack(a, 0, 3)
#
#
#
#
# [1,2,3,4,5,6,7,8,9,10]


count = 1
def check(i, j):
    maps[i][j] = count
    if i - 1 >= 0 and maps[i - 1][j] == '1':
        check(i - 1, j)
    if i + 1 <= n - 1 and maps[i + 1][j] == '1':
        check(i + 1, j)
    if j - 1 >= 0 and maps[i][j - 1] == '1':
        check(i, j - 1)
    if j + 1 <= n - 1 and maps[i][j + 1] == '1':
        check(i, j + 1)


n = int(input())
maps = [list(input()) for i in range(n)]
for i in range(n):
    for j in range(n):
        if maps[i][j] == '1':
            check(i, j)
            count += 1
count - 1
s = [0 for i in range(count - 1)]
for i in range(1, count):
    for j in range(len(maps)):
        for k in range(len(maps[j])):
            if maps[j][k] == i:
                s[i - 1] += 1
print('\n'.join(map(str, sorted(s))))