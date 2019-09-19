import sys
sys.stdin = open('baby_jin.txt', 'r')


def 베이비진찾는애(list, i):
    임시 = sorted(list[:i+1])
    진 = [0]*10
    for a in range(i):
        런 = 0
        for b in range(a+1, i+1):
            if 임시[a]+1 == 임시[b]:
                런 += 1
                if 임시[b]+1 in 임시[b+1:i+1]:
                    런 += 1
                    return i
            런 = 0
            진[임시[a]] += 1
            # if 임시[a] == 임시[b]:
            #     진[임시[a]] += 1
                # if 임시[b:i+1] == 임시[a]:
                #     진[임시[a]] += 1
                #     return i
        if 런 == 2:
            return i
    # print(진, 런)
    for l in range(10):
        if 진[l] == 3:
            return i
    else:
        return 0


testcase = int(input())
for test_num in range(1, testcase+1):
    temp = list(map(int, input().split()))
    player1 = [0]*6
    player2 = [0]*6
    # print(temp)
    for i in range(6):
        player1[i] = temp[2*i]
        player2[i] = temp[2*i+1]

    for i in range(2, 6):
        pl1 = 베이비진찾는애(player1, i)
        if pl1 != 0:
            break
    print(pl1,'pl1pl11111')

    for i in range(2, 6):
        pl2 = 베이비진찾는애(player2, i)
        if pl2 != 0:
            break
    print(pl2, 'pl1pl2222')


    if pl1 == pl2:
        result = 0
    elif pl1 < pl2:
        if pl1 == 0:
            result = 2
        else:
            result = 1
    elif pl1 > pl2:
        if pl2 == 0:
            result = 1
        else:
            result = 2
    else:
        print('에러')
    print('#%d %d'%(test_num, result))