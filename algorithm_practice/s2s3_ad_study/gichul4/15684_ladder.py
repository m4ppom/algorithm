import sys
sys.stdin = open('ladder.txt', 'r')
# 세로선이 사실상 가로수 가로선이 사실상 세로 높

import copy, collections,itertools


def pathfinder(iii, jjj):  # 길을 찾는
    global Hgarosun, num, next
    goal = iii  # 마지막에 같은 위치 가는지 보려고
    go = iii  # 실제로 움직이는애
    wechi = 1  # 내려가는 층? 수
    while True:
        for nn in range(wechi, Hgarosun+2):
            if nn == Hgarosun+1:  # 끝에 도착하면 확인
                if go == goal:
                    next = True
                    return
                else:
                    next = False
                    return
            if go ==  0:   # 맨첫줄은 한쪽만 보면되니까
                if base[go+1][nn] == 1:
                    go = go + 2
                    wechi = nn+1
            elif go ==  num-2:  # 젤옆줄도 한쪽만 보면되니까
                if base[go-1][nn] == 1:
                    go = go - 2
                    wechi = nn+1
            else:  # 양쪽확인
                if base[go+1][nn] == 1:
                    go = go + 2
                    wechi = nn+1
                elif base[go-1][nn] == 1:
                    go = go - 2
                    wechi = nn+1



def canMakeBridge(ii, jj):  # 다리 만드는친구
    global num  # 그 갈 수 있는 대상을 후보군에 넣어줌.
    if ii == 1:
        if base[ii+2][jj] == 1:
            return
        else:
            hubo.append((ii, jj))
    elif ii == num-1:
        if base[ii - 3][jj] == 1:
            return
        else:
            hubo.append((ii, jj))
    else:
        if base[ii][jj] == 0:
            if base[ii-2][jj] == 0 and base[ii+2][jj] == 0:
                hubo.append((ii, jj))


Nserosun, Mgaesu, Hgarosun = map(int, input().split())
base = [[0]*(Hgarosun+2)for _ in range(Nserosun*2+1)]
# print(base)
if Mgaesu == 0:  # 처음에 바로가는애들 커트
    print(0)
else:
    num = 0
    for gilmandulgui in range(Nserosun):  # 위아래로 가는게아니라 옆으로 돌려서 하는거
        base[num] = [1]*(Hgarosun+1)      # 길을 1로 만들어줌.
        num += 2
    # print(base)
    for _ in range(Mgaesu):
        a, b = map(int, input().split())
        base[(b-1)*2+1][a] = 1
    # print(base)
    hubo = []
    for vv in range(Nserosun):
        w = (vv * 2) + 1
        for uu in range(1, Hgarosun+1):
            if base[w][uu] == 0:
                canMakeBridge(w, uu)
    # print(hubo)
    end = 0
    for vvv in range(Nserosun): # 처음 한번 돌려봄 0일 때 끝날 수 있으니까.
        ww = (vvv * 2)
        next = True
        pathfinder(ww, 0)
        if next == False:
            break
        if vvv == Nserosun-1 and next == True:
            print(0)
            end = 1
            break
    if end != 1:
        visited = [0]*len(hubo)
        solution = -1
        for t in range(1, 4):
            if solution != -1:
                break
            a = list(itertools.combinations(hubo, t))
            while a:
                bbb = a.pop()
                for cc in range(len(bbb)):
                    x,y = bbb[cc]
                    base[x][y] = 1

                for vvv in range(Nserosun):
                    ww = (vvv * 2)
                    next = True
                    pathfinder(ww, 0)
                    if next == False:
                        break
                else:
                    solution = t
                    break
                    # print(solution)

                for cc in range(len(bbb)):
                    x,y = bbb[cc]
                    base[x][y] = 0
        if solution != -1:  # 다돌기전에끝나면 이거 출력
            print(solution)
        else:
            print(-1) # 여기까지 안끝났으면 없거나 넘기니까 -1
