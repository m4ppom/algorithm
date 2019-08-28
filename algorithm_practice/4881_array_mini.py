import sys
sys.stdin = open('input0828.txt', 'r')

#
# def dfs1(i, j):
#     global N
#     global summing
#     global cnt
#     global hapi
#     global hapj
#     summing += base[i][j]
#     print(summing)
#     # print('rere', summing)
#     cnt += 1
#     hapi += [i]
#     hapj += [j]
#     print('iii', hapi, 'jjjj', hapj)
#     for a in range(N):
#         for b in range(N):
#             # if a in hapi or b in hapj:
#             if cnt > N-1:
#                 break
#             else:
#                 dfs(a, b)
#
#
#
# def ezwall(x):
#     global N
#     if x > N-1:
#         return False
#     return 1
#
# def dfs(i, j, temp):
#     global summing
#     global cnt
#     global N
#     global nonoj
#     global nonoi
#     # dx = [1,1,-1,-1,0,0,1,-1]
#     # dy = [1,-1,1,-1,1,-1,0,0]
#     visited[j] = 1
#     visited2[i] = 1
#     cnt += 1
#     print('base',i,j)
#     temp = summing
#     summing += base[i][j]
#     mmm = nonoi.index(i)
#     # nonoi.pop(mmm)
#     nnn = nonoj.index(j)
#     # nonoj.pop(nnn)
#     if cnt == N-1:
#         return
#     for a in range(len(nonoi)):
#         for b in range(len(nonoj)):
#             print(nonoi,'iiiii', nonoj,'jjjjj')
#             if visited[a] == 0 and visited2[b] == 0:
#             # print('ez', i+dy[a], j+dx[a])
#             # print(visited)
#                 dfs(a, b, temp)
#
#
# testcase = int(input())
# for test_num in range(1, testcase + 1):
#     result = 100
#     hapi = []
#     hapj = []
#     N = int(input())
#     base = [0] * N
#     for i in range(N):
#         base[i] = list(map(int, input().split()))
#     for i in range(N):
#         temp = 0
#         for j in range(N):
#
#             cnt = 0
#             summing = 0
#             # hapi = []
#             # hapj = []
#             nonoi = [0 for _ in range(N)]
#             nonoj = [0 for _ in range(N)]
#             for i in range(N):
#                 nonoi[i] = i
#                 nonoj[i] = i
#             # visited = [[0 for _ in range(N)]for _ in range(N)]
#             visited = [0 for _ in range(N)]
#             visited2 = [0 for _ in range(N)]
#             # print(visited)
#             dfs(i, j, temp)
#             # if len(set(hapi)) < N or len(set(hapj)):
#             #     continue
#             if summing < result and cnt == N:
#                 print('summing', summing, 'result', result)
#                 result = summing
#     print('#{} {}'.format(test_num, result))


def MyCalc(row):
    global sub_result
    global result
    if result < sub_result:
        return
    if row == N:
        if sub_result < result:
            result = sub_result
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            sub_result += arr[row][i]
            MyCalc(row + 1)
            visited[i] = False
            sub_result -= arr[row][i]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    sub_result, result = 0, 100
    MyCalc(0)
    print('#{} {}'.format(tc, result))