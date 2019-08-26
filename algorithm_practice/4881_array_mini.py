import sys
sys.stdin = open('inpu.txt', 'r')


def dfs(i, j):
    global N
    global summing
    global cnt
    global hapi
    global hapj
    summing += base[i][j]
    print(summing)
    # print('rere', summing)
    cnt += 1
    hapi += [i]
    hapj += [j]
    print('iii', hapi, 'jjjj', hapj)
    for a in range(N):
        for b in range(N):
            # if a in hapi or b in hapj:
            if cnt > N-1:
                continue
            else:
                dfs(a, b)



testcase = int(input())
for test_num in range(1, testcase + 1):
    result = 100
    hapi = []
    hapj = []
    N = int(input())
    base = [0] * N
    for i in range(N):
        base[i] = list(map(int, input().split()))
    for i in range(N):
        for j in range(N):
            cnt = 0
            summing = 0 
            hapi = []
            hapj = []
            dfs(i, j)
            if len(set(hapi)) < N or len(set(hapj)):
                continue
            if summing < result:
                print('summing', summing, 'result', result)
                result = summing
    print('#{} {}'.format(test_num, result))