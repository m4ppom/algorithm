import sys
sys.stdin = open('inpu.txt', 'r')


def maxi(lili):
    numb = 0
    for aa in lili:
        if aa > numb:
            numb = aa
    return numb

testcase = int(input())


for test_num in range(1, testcase + 1):
    info = list(map(int, input().split()))
    # print(info)
    result = 0
    row_N = info[0]
    col_M = info[1]
    painting = info[2]
    base = [[0 for _ in range(col_M+1)]for _ in range(row_N+1)]
    strength_book = [0]
    area_num_list = []
    # print(base)
    for _ in range(painting):
        painting_info = list(map(int, input().split()))
        # print(painting_info)
        strength = painting_info[4]
        strength_book += [painting_info[4]]
        # print('책', strength_book)
        notpaint = 0
        for i in range(painting_info[0], painting_info[2]+1):
            if notpaint == 1:
                break
            else:
                for j in range(painting_info[1], painting_info[3]+1):

                    if base[i][j] > strength:

                        notpaint = 1
                        break
        if notpaint == 0:
            for i in range(painting_info[0], painting_info[2]+1):
                for j in range(painting_info[1], painting_info[3]+1):
                    base[i][j] = strength
    coloring = []
    # for color in set(strength_book):
    for color in set(strength_book):
        count = 0
        for i in range(row_N):
            for j in range(col_M):
                if base[i][j] == color:
                    count += 1
        coloring.append(count)
    # print(base)
    # print(coloring)
    result = maxi(coloring)
    print('#{} {}'.format(test_num, result))




