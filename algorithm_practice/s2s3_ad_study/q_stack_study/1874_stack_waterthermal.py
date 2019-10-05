import sys
sys.stdin = open('wathe.txt', 'r')

from collections import deque
N = int(input())
q = deque()
for i in range(1, N+1):
    q.append(int(input()))
cnt = 0
visited = [0]*(N+1)
brea = False
printing = deque()
while q and brea == False:
    no = q.popleft()
    if cnt < no:
        while cnt != no:
            cnt += 1
            if 0 < cnt < N+1:
                if visited[cnt] == 0:
                    printing.append('+')
            elif cnt == no:
                if visited[cnt] == 0:
                    printing.append('-')
                    visited[cnt] = 1
                else:
                    brea = True
                    break
            else:
                brea = True
                break
        if cnt == no:
            if visited[cnt] == 1:
                brea = True
            else:
                printing.append('-')
                visited[cnt] = 1
    elif cnt > no:
        while cnt != no:
            cnt -= 1
            if 0 < cnt < N + 1:
                if visited[cnt] == 0:
                    visited[cnt] = 1
                    if cnt == no:
                        printing.append('-')
                    else:
                        printing.append('-')
            else:
                brea = True
                break
    if brea == True:
        print('NO')
        break
if brea == False:
    for i in printing:
        print(i)