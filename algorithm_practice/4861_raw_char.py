import  sys
sys.stdin = open("inpu.txt", "r")

test_case = int(input())
for numbers in range(1, test_case + 1):
    N, MM = map(int, input().split())
    M = MM-1
    result = 0
    matrix = [[i for i in input()] for _ in range(N)]
    for idx1 in range(N):
        for idx2 in range(N-M):
            # print(matrix)
            # print(idx1, idx2, M)
            mov = -1
            y = 0
            if matrix[idx1][idx2] == matrix[idx1][idx2+M]:
                finder1 = M
                i = 1
                while finder1 != i:
                    finder1 -= 1
                    # print('finder1',finder1 , 'i',i)
                    if matrix[idx1][idx2 +i] != matrix[idx1][idx2 + finder1]:
                        break
                    elif finder1 - i == 1 or finder1 == i:
                        if matrix[idx1][idx2 + i] == matrix[idx1][idx2 + finder1]:
                            result = matrix[idx1][idx2:idx2+M+1]
                            break
                    i += 1
                if result:
                    break
            elif idx1 + M < N:
                mov += 1
                # print('idx', idx1, 'M', M, 'N', N, 'mov', mov)
                while mov < N-1:
                    mov += 1
                    # print('idx', idx1, 'M', M, 'N', N, 'mov', mov)
                    # print(matrix)
                    # print('[',idx1,']','[',mov,']','이랑','[',idx1+M,']','[',mov,']')
                    # print(matrix[idx1][mov],'dasdas')
                    # print(matrix[idx1+M][mov])
                    if matrix[idx1][mov] == matrix[idx1+M][mov]:
                        finder2 = M
                        # print(idx1, mov, finder2)
                        j = 1
                        while finder2 != j:
                            finder2 -= 1
                            # print('finder2',finder2, 'j',j,'mov',mov, 'finder2', finder2)
                            if matrix[idx1+j][mov] != matrix[idx1+finder2][mov]:
                                break
                            elif finder2 - j == 1 or finder2 == j:
                                if matrix[idx1+j][mov] == matrix[idx1+finder2][mov]:
                                    result = []
                                    for k in range(M+1):
                                        result += matrix[idx1+k][mov]
                                    break
                            j += 1
                            if result:
                                break

                    if result:
                        break
            if result:
                break

        if result:
            break



    print('#{}'.format(numbers), end=' ')
    for i in result:
        print('{}'.format(i), end='')
    print('')
