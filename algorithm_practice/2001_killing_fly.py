import sys
sys.stdin = open('input0902.txt', 'r')


testcase = int(input())
for test_num in range(1, testcase+1):
    N, killin_eM = map(int, input().split())
    base = [00] * N
    for a in range(N):
        base[a] = list(map(int, input().split()))
    most_eff = 0
    for i in range(N+1 - killin_eM):
        for j in range(N+1 - killin_eM):
            casualties = 0
            for k in range(i, i+killin_eM):
                for l in range(j, j + killin_eM):

.                    casualties += base[k][l]
            if casualties > most_eff:
                most_eff = casualties
    print('#{} {}'.format(test_num, most_eff))


