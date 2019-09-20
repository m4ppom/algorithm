import sys
sys.stdin = open('Immigration.txt', 'r')

testcase = int(input())
for test_num in range(1, testcase+1):
    N, M = map(int, input().split())
    test_Man = [[0]*3 for _ in range(N)]
    for i in range(N):
        test_Man[i][0] = int(input())
    test_Man.sort()
    temp =0
    point = 0
    mul = 1
    lim_time = 0
    cnt = 0
    while M != 0:
        if test_Man[0][1] == 0:
            for i in range(len(test_Man)):
                if test_Man[0][0] == test_Man[i][0]:
                    cnt += 1
                break
            for i in range(cnt):
                test_Man[i][2] += 1
                test_Man[i][1] += test_Man[i][0]
                M -= 1
                if M == 0:
                    break
            lim_time += test_Man[0][0]
        else:
            for i in range(len(test_Man)):
                if test_Man[0][1] >= test_Man[i][1] and test_Man[0][1] >= test_Man[i][0]:
                    test_Man[i][1] += test_Man[i][0]
                    test_Man[i][2] += 1
                    M -= 1
                    if M == 0:
                        break
    # print(test_Man)
    maxx = 0
    for i in range(len(test_Man)):
        if maxx < test_Man[i][1]:
            maxx = test_Man[i][1]
    print('#%d %d' % (test_num, maxx))

    # while M != 0:
    #     for i in range(1, len(test_Man)):
    #         if test_Man[0][0] != 0 and test_Man[0][1] >= test_Man[i][1]:
    #             point = i
    #             break
    #         elif test_Man[0][0] != 0 and test_Man[0][1] >= test_Man[i][0]:
    #             point = i
    #             break
    #         elif test_Man[0][0] * mul < test_Man[i][0]:
    #             point = i
    #             break
    #     for i in range(0, point+1):
    #         test_Man[i][1] += test_Man[i][0]
    #         M -= 1
    #     mul += 1


    # while M != 0:
    #     mul = 1
    #     for i in range(len(test_Man)):
    #         for j in range(0, len(test_Man)):
    #             if test_Man[j][0] // test_Man[i][1] > mul:
    #                 temp = j
    #                 for aa in range(temp):
    #                     test_Man[aa][1] += test_Man[aa][0]
    #                     M -= 1
    #                     if M == 0:
    #                         break
    #                 break
    #             else:
    #                 for mm in range(len(test_Man)):
    #                     test_Man[mm][1] += 1
    #                     M -= 1
    #                     if M == 0:
    #                         break
    #             if M == 0:
    #                 break
    #         if M == 0:
    #             break
    #     mul += 1
    #     if M != 0 and test_Man[-1][1] != 0:
    #         for i in range(len(test_Man)):
    #             test_Man[i][1] += 1
    #             M -= 1
    #             if M == 0:
    #                 break