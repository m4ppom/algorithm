import sys
sys.stdin = open('inpu.txt', 'r')


def calc(n):  # 2
    global N, summ
    if n > N:
        return
    if new[n] == 0:
        calc(n*2+1)
        calc(2 * n)
        # new[n] = summ
        # summ = 0
        # # new[n] = calc(2*n) + calc(n*2+1)
    else:
        summ += new[n]


T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    arr = []
    for _ in range(M):
        arr += input().split()
    arr = list(map(int, arr))
    arr.extend([N+1, 0])
    new = [0]*(N*2)
    for i in range(0, len(arr)-1, 2):
        for j in range(i+2, len(arr)-1, 2):
            new[arr[i]] = arr[i+1]
    summ = 0
    calc(L)
    # print(new)
    print('#{} {}'.format(tc, summ))

