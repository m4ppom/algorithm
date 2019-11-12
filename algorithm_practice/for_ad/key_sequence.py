import sys
sys.stdin = open('key.txt', 'r')


def deeeeeep_up(idx):
    # for i in range(M):
    #     if base[i][1] == idx:
    #         vztd[base[i][0]] = 1
    #         deeeeeep_up(base[i][0])
    q = []
    q.append(idx)
    while q:
        a = q.pop()
        for i in range(M):
            if base[i][1] == a:
                vztd[base[i][0]] = 1
                q.append(base[i][0])

def deeeeeep_down(idx):
    # for i in range(M):
    #     if base[i][0] == idx:
    #         vztd[base[i][1]] = 1
    #         deeeeeep_down(base[i][1])
    q = []
    q.append(idx)
    while q:
        a = q.pop()
        for i in range(M):
            if base[i][0] == a:
                vztd[base[i][1]] = 1
                q.append(base[i][1])


testnum = int(input())
for testcase in range(1, testnum+1):
    N = int(input())  # 명의 학생들은 키가다르다
    M = int(input())  # 비교횟수
    base = [0]*M
    cnt = 0
    for _ in range(M):
        base[_] = list(map(int, input().split()))
    for i in range(1, N+1):
        vztd = [0]*(N+1)
        vztd[i] = 1
        for __ in range(M):
            if base[__][0] == i:
                vztd[base[__][1]] = 1
                deeeeeep_up(base[__][1])
            elif base[__][1] == i:
                vztd[base[__][0]] = 1
                deeeeeep_up(base[__][0])
            if sum(vztd) == N:
                cnt += 1
                break

    print('#%d %d' %(testcase, cnt))