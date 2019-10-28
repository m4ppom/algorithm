import sys
sys.stdin = open('einger_King.txt', 'r')


def sharkmovin():
    global R, C
    for iii in range(R):
        for jjj in range(C):
            if base[iii][jjj] != 0:
                if base[iii][jjj][1] == 1:  # up
                    namuji = base[iii][jjj][0] % (2*(R-1))
                    weechi = iii - namuji
                    if weechi < 0:
                        weechi = abs(weechi)
                        if weechi >= R:  # 선 넘고 또 선넘은 애들 디렉 안바뀜
                            weechi = (R - 1) - (weechi - (R - 1))
                            if weechi < 0:
                                weechi = abs(weechi)
                                if basecopy[weechi][jjj] != 0:
                                    if basecopy[weechi][jjj][2] > base[iii][jjj]:  # 갈곳이 더 크면 걍 스킵
                                        pass
                                    else:  # 아니면 넣어줘야함
                                        basecopy[weechi][jjj] = [base[iii][jjj][0], 2, base[iii][jjj][2]]
                                else:  # 아니면 넣어줘야함
                                    basecopy[weechi][jjj] = [base[iii][jjj][0], 2, base[iii][jjj][2]]
                            else:
                                if basecopy[weechi][jjj] != 0:
                                    if basecopy[weechi][jjj][2] > base[iii][jjj]:  # 갈곳이 더 크면 걍 스킵
                                        pass
                                    else:  # 아니면 넣어줘야함
                                        basecopy[weechi][jjj] = base[iii][jjj]
                                else:  # 아니면 넣어줘야함
                                    basecopy[weechi][jjj] = base[iii][jjj]

                        else:  # 선넘고 또 넘지 않은 애들  넘은 애들 .
                            if basecopy[weechi][jjj] != 0:
                                if basecopy[weechi][jjj][2] > base[iii][jjj][2]:
                                    pass
                                else:
                                    basecopy[weechi][jjj] = [base[iii][jjj][0], 2, base[iii][jjj][2]]
                            else:  ####
                                basecopy[weechi][jjj] = [base[iii][jjj][0], 2, base[iii][jjj][2]]
                    else:  # 선안넘은애들
                        if basecopy[weechi][jjj] != 0:
                            if basecopy[weechi][jjj][2] > base[iii][jjj][2]:
                                pass
                            else:
                                basecopy[weechi][jjj] = base[iii][jjj]
                        else:
                            basecopy[weechi][jjj] = base[iii][jjj]
                elif base[iii][jjj][1] == 2:  # down
                    namuji = base[iii][jjj][0] % (2 * (R - 1))
                    weechi = iii + namuji
                    if weechi >= R:  # 선넘은애들 방향반대
                        weechi = (R - 1) - (weechi - (R - 1))
                        if weechi < 0:  # 선넘고 또넘은애들 방향 다시 원래대로
                            weechi = abs(weechi)
                            if weechi >= R:  # 선넘고 또넘고 또넘은애들 방향반대
                                weechi = (R - 1) - (weechi - (R - 1))
                                if basecopy[weechi][jjj] != 0:
                                    if basecopy[weechi][jjj][2] > base[iii][jjj][2]:
                                        pass
                                    else:
                                        basecopy[weechi][jjj] = [base[iii][jjj][0], 1, base[iii][jjj][2]]
                                else:
                                    basecopy[weechi][jjj] = [base[iii][jjj][0], 1, base[iii][jjj][2]]
                            else:
                                if basecopy[weechi][jjj] != 0:
                                    if basecopy[weechi][jjj][2] > base[iii][jjj][2]:
                                        pass
                                    else:
                                        basecopy[weechi][jjj] = base[iii][jjj]
                                else:
                                    basecopy[weechi][jjj] = base[iii][jjj]
                        else:
                            if basecopy[weechi][jjj] != 0:
                                if basecopy[weechi][jjj][2] > base[iii][jjj][2]:
                                    pass
                                else:
                                    basecopy[weechi][jjj] = [base[iii][jjj][0], 1, base[iii][jjj][2]]
                            else:  ####
                                basecopy[weechi][jjj] = [base[iii][jjj][0], 1, base[iii][jjj][2]]
                    else:  # 선안넘은애들
                        if basecopy[weechi][jjj] != 0:
                            if basecopy[weechi][jjj][2] > base[iii][jjj][2]:
                                pass
                            else:
                                basecopy[weechi][jjj] = base[iii][jjj]
                        else:
                            basecopy[weechi][jjj] = base[iii][jjj]
                elif base[iii][jjj][1] == 3:  # right
                    namuji = base[iii][jjj][0] % (2 * (C - 1))
                    weechi = jjj + namuji
                    if weechi >= C:  # 선넘은애들 방향반대
                        weechi = (C - 1) - (weechi - (C - 1))
                        if weechi < 0:  # 선넘고 또넘은애들 방향 다시 원래대로
                            weechi = abs(weechi)
                            if weechi >= C:  # 선넘고 또넘고 또넘은애들 방향반대
                                weechi = (C - 1) - (weechi - (C - 1))
                                if basecopy[iii][weechi] != 0:
                                    if basecopy[iii][weechi][2] > base[iii][jjj][2]:
                                        pass
                                    else:
                                        basecopy[iii][weechi] = [base[iii][jjj][0], 4, base[iii][jjj][2]]
                                else:
                                    basecopy[iii][weechi] = [base[iii][jjj][0], 4, base[iii][jjj][2]]
                            else:
                                if basecopy[iii][weechi] != 0:
                                    if basecopy[iii][weechi][2] > base[iii][jjj][2]:
                                        pass
                                    else:
                                        basecopy[iii][weechi] = base[iii][jjj]
                                else:  ######
                                    basecopy[iii][weechi] = base[iii][jjj]
                        else:
                            if basecopy[iii][weechi] != 0:
                                if basecopy[iii][weechi][2] > base[iii][jjj][2]:
                                    pass
                                else:
                                    basecopy[iii][weechi] = [base[iii][jjj][0], 4, base[iii][jjj][2]]
                            else:  ####
                                basecopy[iii][weechi] = [base[iii][jjj][0], 4, base[iii][jjj][2]]
                    else:  # 선안넘은애들
                        if basecopy[iii][weechi] != 0:
                            if basecopy[iii][weechi][2] > base[iii][jjj][2]:
                                pass
                            else:
                                basecopy[iii][weechi] = base[iii][jjj]
                        else:
                            basecopy[iii][weechi] = base[iii][jjj]
                elif base[iii][jjj][1] == 4:  # left
                    namuji = base[iii][jjj][0] % (2*(C-1))
                    weechi = jjj - namuji
                    if weechi < 0:
                        weechi = abs(weechi)
                        if weechi >= C:  # 선 넘고 또 선넘은 애들 디렉 안바뀜
                            weechi = (C - 1) - (weechi - (C - 1))

                            if weechi < 0:
                                weechi = abs(weechi)
                                if basecopy[iii][weechi] != 0:
                                    if basecopy[iii][weechi][2] > base[iii][jjj]:  # 갈곳이 더 크면 걍 스킵
                                        pass
                                    else:  # 아니면 넣어줘야함
                                        basecopy[iii][weechi] = [base[iii][jjj][0], 3, base[iii][jjj][2]]
                                else:  # 아니면 넣어줘야함
                                    basecopy[iii][weechi] = [base[iii][jjj][0], 3, base[iii][jjj][2]]
                            else:
                                if basecopy[iii][weechi] != 0:
                                    if basecopy[iii][weechi][2] > base[iii][jjj]:  # 갈곳이 더 크면 걍 스킵
                                        pass
                                    else:  # 아니면 넣어줘야함
                                        basecopy[iii][weechi] = base[iii][jjj]
                                else:  # 아니면 넣어줘야함
                                    basecopy[iii][weechi] = base[iii][jjj]

                        else:  # 선넘고 또 넘지 않은 애들  넘은 애들 .
                            if basecopy[iii][weechi] != 0:
                                if basecopy[iii][weechi][2] > base[iii][jjj][2]:
                                    pass
                                else:
                                    basecopy[iii][weechi] = [base[iii][jjj][0], 3, base[iii][jjj][2]]

                            else:  ####
                                basecopy[iii][weechi] = [base[iii][jjj][0], 3, base[iii][jjj][2]]
                    else:  # 선안넘은애들
                        if basecopy[iii][weechi] != 0:
                            if basecopy[iii][weechi][2] > base[iii][jjj][2]:
                                pass
                            else:
                                basecopy[iii][weechi] = base[iii][jjj]
                        else:
                            basecopy[iii][weechi] = base[iii][jjj]


'''                    
                    if weechi < 0:  # 선 넘어가면
                        weechi = abs(weechi)  # 양수로 바꿔주고 이동
                        if weechi >= R-1:
                            weechi = (R - 1) - (weechi - (R - 1))
                            if basecopy[weechi][jjj] != 0:
                                if basecopy[weechi][jjj][2] > base[iii][jjj][2]:  # 겹치면
                                    pass
                                else:
                                    basecopy[weechi][jjj] = [base[iii][jjj][0], 1, base[iii][jjj][2]]
                            else:  # 안겹치면 그대로 넣어줌
                                basecopy[weechi][jjj] = [base[iii][jjj][0], 2, base[iii][jjj][2]]
                        else:
                            if basecopy[weechi][jjj] != 0:
                                if basecopy[weechi][jjj][2] > base[iii][jjj][2]:
                                    pass
                                else:
                                    basecopy[weechi][jjj] = [base[iii][jjj][0], 1, base[iii][jjj][2]]
                            else:
                                basecopy[weechi][jjj] = [base[iii][jjj][0], 1, base[iii][jjj][2]]

                    else:  # -안넘어가면 방향 안바뀌니까.
                        if basecopy[weechi][jjj] != 0:
                            if basecopy[weechi][jjj][2] > base[iii][jjj][2]:
                                pass
                            else:
                                basecopy[weechi][jjj] = [base[iii][jjj][0], 1, base[iii][jjj][2]]
                        else:
                            basecopy[weechi][jjj] = [base[iii][jjj][0], 1, base[iii][jjj][2]]


                elif base[iii][jjj][1] == 2:  # down
                    namuji = base[iii][jjj][0] % (2*(R-1))
                    weechi = iii + namuji
                    if weechi > R-1:  # 크기넘어가면
                        weechi = (R - 1) - (weechi - (R - 1))  # 짤라주고
                        if weechi < 0:  # 0보다 작으면 또 짤라줌
                            weechi = abs(weechi)
                            weechi = (R - 1) - (weechi - (R - 1))
                            if basecopy[weechi][jjj] != 0:
                                if basecopy[weechi][jjj][2] > base[iii][jjj][2]:
                                    pass
                                else:
                                    basecopy[weechi][jjj] = [base[iii][jjj][0], 2, base[iii][jjj][2]]
                            else:
                                basecopy[weechi][jjj] = [base[iii][jjj][0], 1, base[iii][jjj][2]]
                        else:
                            if basecopy[weechi][jjj] != 0:
                                if basecopy[weechi][jjj][2] > base[iii][jjj][2]:
                                    pass
                                else:
                                    basecopy[weechi][jjj] = [base[iii][jjj][0], 2, base[iii][jjj][2]]
                            else:
                                basecopy[weechi][jjj] = [base[iii][jjj][0], 1, base[iii][jjj][2]]
                    else:
                        if basecopy[weechi][jjj] != 0:
                            if basecopy[weechi][jjj][2] > base[iii][jjj][2]:
                                pass
                            else:
                                basecopy[weechi][jjj] = [base[iii][jjj][0], 2, base[iii][jjj][2]]
                        else:
                            basecopy[weechi][jjj] = [base[iii][jjj][0], 2, base[iii][jjj][2]]


                elif base[iii][jjj][1] == 3:  # right
                    namuji = base[iii][jjj][0] % (2*(C-1))
                    weechi = iii + namuji
                    if weechi > C-1:
                        weechi = (C - 1) - (weechi - (C - 1))
                        if weechi < 0:
                            weechi = abs(weechi)
                            weechi = (C - 1) - (weechi - (C - 1))
                            if basecopy[iii][weechi] != 0:
                                if basecopy[iii][weechi][2] > base[iii][jjj][2]:
                                    pass
                                else:
                                    basecopy[iii][weechi] = [base[iii][jjj][0], 3, base[iii][jjj][2]]
                            else:
                                basecopy[iii][weechi] = [base[iii][jjj][0], 4, base[iii][jjj][2]]
                        else:
                            if basecopy[iii][weechi] != 0:
                                if basecopy[iii][weechi][2] > base[iii][jjj][2]:
                                    pass
                                else:
                                    basecopy[iii][weechi] = [base[iii][jjj][0], 3, base[iii][jjj][2]]
                            else:
                                basecopy[iii][weechi] = [base[iii][jjj][0], 4, base[iii][jjj][2]]
                    else:
                        if basecopy[iii][weechi] != 0:
                            if basecopy[iii][weechi][2] > base[iii][jjj][2]:
                                pass
                            else:
                                basecopy[iii][weechi] = [base[iii][jjj][0], 3, base[iii][jjj][2]]
                        else:
                            basecopy[iii][weechi] = [base[iii][jjj][0], 3, base[iii][jjj][2]]


                elif base[iii][jjj][1] == 4:  # left
                    namuji = base[iii][jjj][0] % (2*(C-1))
                    weechi = jjj - namuji
                    if weechi < 0:
                        weechi = abs(weechi)
                        if weechi >= C-1:
                            weechi = (C - 1) - (weechi - (C - 1))
                            basecopy[iii][weechi] = [base[iii][jjj][0], 4, base[iii][jjj][2]]
                            if basecopy[iii][weechi] != 0:
                                if basecopy[iii][weechi][2] > base[iii][jjj][2]:
                                    pass
                                else:
                                    basecopy[iii][weechi] = [base[iii][jjj][0], 4, base[iii][jjj][2]]
                            else:
                                basecopy[iii][weechi] = [base[iii][jjj][0], 3, base[iii][jjj][2]]
                        else:
                            if basecopy[iii][weechi] != 0:
                                if basecopy[iii][weechi][2] > base[iii][jjj][2]:
                                    pass
                                else:
                                    basecopy[iii][weechi] = [base[iii][jjj][0], 4, base[iii][jjj][2]]
                            else:
                                basecopy[iii][weechi] = [base[iii][jjj][0], 3, base[iii][jjj][2]]
                    else:
                        if basecopy[iii][weechi] != 0:
                            if basecopy[iii][weechi][2] > base[iii][jjj][2]:
                                pass
                            else:
                                basecopy[iii][weechi] = base[iii][jjj]
                        else:
                            basecopy[iii][weechi] = base[iii][jjj]
'''


R, C, M = map(int, input().split())
base = [[0]*C for _ in range(R)]
# direction = up:1 down:2 right:3   left:4
summ = 0
for i in range(M):
    r, c, s, d, z = map(int, input().split())
    base[r-1][c-1] = [s, d, z]
gotgot = 0
man = 0
while man != M:
    got = 0
    # print(man)
    # for man in range(C):
    for ii in range(R):
        if base[ii][man] != 0:
            summ += base[ii][man][2]
            base[ii][man] = 0
            got = 1
            break
    # if got == 1:
    #     break
    # else:
    #     got = 1
    basecopy = [[0] * C for _ in range(R)]
    sharkmovin()
    base = basecopy
    if got == 1:
        gotgot += 1
        if gotgot == M:
            break
    man += 1
    if man == C:
        break
print(summ)
