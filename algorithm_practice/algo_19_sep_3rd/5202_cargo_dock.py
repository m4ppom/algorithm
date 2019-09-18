import sys
sys.stdin = open('cargo.txt', 'r')


def pathfinder(idx, end):
    global num, aa
    num += 1
    # print('gogo', num)
    global cnt, maxx
    if idx >= len(base)-1:
        if maxx < cnt:
            maxx = cnt
        return
    # if maxx != 0:
    #     if abs(base[idx][0] - base[idx][1]) > aa//maxx:
    #         return
    if end == 0:
        ended.append(base[idx][1])
        end = ended[-1]
    if end <= base[idx+1][0]:
        ended.append(base[idx+1][1])
        end = ended[-1]
        cnt += 1
        pathfinder(idx + 1, end)
        cnt -= 1
        ended.pop(-1)
        end = ended[-1]
    else:
        pathfinder(idx+1, end)
    pathfinder(idx + 1, end)


def func():
    global se
    if len(se) == 0:
        return
    else:
        s = se.pop(0)
        if res[-1][1] <= s[0] and s not in res:
            res.append(s)
        func()


# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     se = [list(map(int, input().split())) for _ in range(N)]
#     for i in range(N-1):
#         mi = i
#         for j in range(i+1, N):
#             if se[mi][1] > se[j][1]:
#                 mi = j
#         se[i], se[mi] = se[mi], se[i]
#     res = [se[0]]
#     func()
#     print('#%d %d' % (tc, len(res)))
#
testcase = int(input())
for test_num in range(1, testcase+1):
    N = int(input())
    cnt = 0
    num =0
    result = 0
    base = [0]*N
    maxx = 0
    ended = []
    for i in range(N):
        base[i] = list(map(int, input().split()))
    base = sorted(base)
    # print(base)
    aa = abs(base[0][0] - base[0][1])
    pathfinder(0, 0)

    print('#%d %d'%(test_num, maxx+1))
