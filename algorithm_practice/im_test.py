import sys
sys.stdin = open('input.txt', 'r')

testcase = int(input())

for test_num in range(1, testcase):
    N = int(input())
    base = [0] * N
    for i in range(N):
        base[i] = list(map(int, input().split()))
    result = 1
    corr = [0]*4
    summ = 0
    for i in range(N):
        for j in range(N):
            summ += base[i][j]
    want = summ // 4
    if want != summ/4:
        result = 0

    else:
        cut_i = 1
        cut_j = 1
        while sum(corr) != 4:
            corr = [0] * 4
            squ_sum = 0
            for i in range(0, cut_i):
                for j in range(0, cut_j):
                    squ_sum += base[i][j]
            if squ_sum == want:
                corr[0] = 1
            else:
                cut_j += 1
                if cut_j == N:
                    cut_j = 1
                    cut_i += 1
                    if cut_i == N:
                        result = 0
                        break
                    continue
                continue

            for i in range(cut_i, N):
                for j in range(0, cut_j):
                    squ_sum += base[i][j]
            if squ_sum == want:
                corr[1] = 1
            else:
                cut_j += 1
                if cut_j == N:
                    cut_j = 1
                    cut_i += 1
                    if cut_i == N:
                        result = 0
                        break
                    continue
                continue

            for i in range(0, cut_i):
                for j in range(cut_j, N):
                    squ_sum += base[i][j]
            if squ_sum == want:
                corr[2] = 1
            else:
                cut_j += 1
                if cut_j == N:
                    cut_j = 1
                    cut_i += 1
                    if cut_i == N:
                        result = 0
                        break
                    continue
                continue

            for i in range(cut_i, N):
                for j in range(cut_j, N):
                    squ_sum += base[i][j]
            if squ_sum == want:
                corr[3] = 1
            else:
                cut_j += 1
                if cut_j == N:
                    cut_j = 1
                    cut_i += 1
                    if cut_i == N:
                        result = 0
                        break
                    continue
                continue

    print('#{} {}'.format(test_num, result))