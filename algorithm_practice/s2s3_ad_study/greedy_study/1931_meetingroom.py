import sys
sys.stdin = open('1931.txt', 'r')
sys.setrecursionlimit(10000000)
#
# def pathfinder(start):
#     global N, cnt, maximu
#     for ii in range(start, N):
#         if timelist[start][1] == timelist[ii][0] and visited[ii] == 0:
#             visited[ii] = 1
#             cnt += 1
#             pathfinder(ii)
#             cnt -= 1
#             visited[ii] = 0
#         elif timelist[start][1] == timelist[ii][0]+1 and visited[ii] == 0:
#             visited[ii] = 1
#             cnt += 1
#             pathfinder(ii)
#             cnt -= 1
#             visited[ii] = 0
#     if maximu < cnt:
#         maximu = cnt
#
#
# N = int(input())
# timelist = [0]*N
# for i in range(N):
#     timelist[i] = list(map(int, input().split()))
# timelist.sort()
# cnt = 0
# maximu = 0
# visited = [0]*N
# for j in range(N):
#     if N - j < maximu:
#         break
#     visited[j] = 1
#     pathfinder(j)
#     visited[j] = 0
# if N == 1:
#     maximu = 1
# print(maximu)
#
# def roomfinder(index):
#     global N, count, maxx
#     if index == N-1:
#         if maxx < count:
#             maxx = count
#         return
#     for idx in range(index+1, N):
#         if timelist[index][0] >= timelist[idx][1]:
#             count += 1
#             roomfinder(idx)
#             count -= 1
#         else:
#             continue
#     else:
#         if maxx < count:
#             maxx = count


N = int(input())
timelist = [0]*N
for i in range(N):
    timelist[i] = list(map(int, input().split()))
    timelist[i][0], timelist[i][1] = timelist[i][1], timelist[i][0]
timelist.sort()
count = 0
idx = 0
while idx != N-1:
    end_time = timelist[idx][0]
    for i in range(idx+1, N):
        if timelist[i][1] == end_time:
            count += 1
            idx = i
            break
        elif timelist[i][1] == end_time+1:
            count += 1
            idx = i
            break
        elif i == N-1:
            idx = N-1
print(count)