import sys
# sys.stdin = open('N&M1.txt')


def finder(idx, start, N, M):
    if idx == M:
        for i in range(len(a)):
            print('%d' %a[i], end=' ')
        print()
        return
    for i in range(start, N + 1):
        if visited[i]:
            continue
        visited[i] = 1  
        a[idx] = i
        finder(idx + 1, i + 1, N, M)
        visited[i] = 0


N, M = map(int, input().split())
visited = [0] * (N + 1)
a = [0] * M
finder(0, 1, N, M)