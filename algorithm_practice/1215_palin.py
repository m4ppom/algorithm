import  sys
sys.stdin = open("inpu.txt", "r")

def palin(list):
    i = 0
    fin = len(list) - 1
    stop = 0
    # print(list)
    while fin != i and fin - i != 1:
        # print(list)
        i += 1
        fin -= 1
        if list[i] != list[fin]:
            stop = 1
            break
    # print(list)
    if stop == 1:
        return 0
    else:
        return 1

for num in range(1, 11):
    test_case = int(input())
    matrix = [[i for i in input()] for _ in range(8)]
    maxi = test_case
    count = 0
    for i in range(8):
        # print(maxi)
        for j in range(0, 8-maxi+1):
            for k in range(j, 8):
                # if j - k != maxi-1:
                #     break
                if len(matrix[i][j:k+1]) == maxi:
                    if matrix[i][j] == matrix[i][k]:
                        # print(matrix[i][j:k+1])
                        count += palin(matrix[i][j:k+1])

    for j in range(8):
        for i in range(0, 8-maxi+1):
            test = []
            for k in range(i, 8):
                test.append(matrix[k][j])
                if matrix[i][j] == matrix[k][j]:
                    if len(test) == maxi:
                    #     continue
                    # else:
                        count += palin(test)

    print('#{} {}'.format(num, count))
