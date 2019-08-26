import sys
sys.stdin = open('inpu.txt', 'r')


def ezwall(x):
    global N
    if x < 0 or x > N-1:
        return False
    return 1

def dfs(i, j):
    global result
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    for a in range(4):
        if ezwall(i+dy[a]) == True and ezwall(j+dx[a]) == True:
            # print('ez', i+dy[a], j+dx[a])
            if base[i+dy[a]][j+dx[a]] == 0:
                base[i][j] = 1
                dfs(i+dy[a], j+dx[a])
            elif base[i+dy[a]][j+dx[a]] == 3:
                result = 1


testcase = int(input())
for test_no in range(1, testcase+1):
    result = 0
    N = int(input())
    base = [0] * N
    for i in range(N):
        base[i] = list(map(int, input()))
    for i in range(N):
        for j in range(N):
            if base[i][j] == 2:
                # print('ij', i, j)
                dfs(i, j)
    # print(base)
    print('#{} {}'.format(test_no, result))
