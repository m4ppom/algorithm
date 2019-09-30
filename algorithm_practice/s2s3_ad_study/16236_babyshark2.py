import sys
sys.stdin = open('baby_shark.txt', 'r')
import copy
import collections


def sharksize():
    global shark_size, cnt
    if cnt == shark_size:
        shark_size += 1
        cnt = 0
    else:
        cnt += 1
        if cnt == shark_size:
            shark_size += 1
            cnt = 0


def bfs(finding_i, finding_j):
    global shark_size, time, N
    # q = collections.deque()
    q = []
    # fishing = collections.deque()
    fishing = []
    visited = [[0]*N for _ in range(N)]
    visited[finding_i][finding_j] = 1
    q.append([visited[finding_i][finding_j], finding_i, finding_j])
    base[finding_i][finding_j] = 0
    while q:
        # tt = q.popleft()
        tt = q.pop(0)
        a, b = tt[1], tt[2]
        for delta in range(4):
            aa = a + dy[delta]
            bb = b + dx[delta]
            if -1 < aa < N and -1 < bb < N:
                if visited[aa][bb] == 0:
                    if base[aa][bb] == 0 or base[aa][bb] == shark_size:
                        visited[aa][bb] = visited[a][b]+1
                        q.append([visited[aa][bb], aa, bb])
                    elif base[aa][bb] < shark_size:
                        visited[aa][bb] = visited[a][b]+1
                        fishing.append([visited[aa][bb], aa, bb])
                        # break
        # if fishing:
        #     break
    if fishing:
        fishing.sort()
        # ttt = fishing.popleft()
        ttt = fishing.pop(0)
        fi, sh = ttt[1], ttt[2]

        sharksize()
        time += visited[fi][sh]-1
        base[fi][sh] = 9
        bfs(fi, sh)
    else:
        return


dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]
# testcase = int(input())
# for test_num in range(1, testcase+1):
shark_size = 2
time = 0
cnt = 0
N = int(input())
base = [0]*N
for i in range(N):
    base[i] = list(map(int, input().split()))
for find_i in range(N):
    for find_j in range(N):
        if base[find_i][find_j] == 9:
            bfs(find_i, find_j)
            break
print(time)
    # print('#%d %d' %(test_num, time))
