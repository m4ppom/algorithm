import itertools
import sys
sys.stdin = open('eleccart.txt', 'r')

testcase = int(input())
for test_num in range(1, testcase+1):
    N = int(input())
    base = [0]*N
    for i in range(N):
        base[i] = list(map(int, input().split()))
    a = list(itertools.permutations(range(0, N), N))
    mini = 99999
    for i in range(len(a)):
        summ = 0
        cnt = 0
        # stst = 0
        # if stst == 0:
        #     for mm in range(N-1):
        #         if abs(a[i][mm]-a[i][mm+1]) == 1:
        #             # print(a)
        #             stst = 1
        #             break
        # if stst == 1:
        #     continue

        for j in range(N):
            if j == a[i][j]:  # or a[i][j-1] == j:
                break
            else:
                summ += base[j][a[i][j]]
                cnt += 1
        if mini > summ and cnt == N:
            if a[i][-1] == 0:
            # lst = a[i].insert(0, 0)
                print(a)
                mini = summ
        cnt = 0
    print('#%d %d' % (test_num, mini))

