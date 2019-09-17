import sys
sys.stdin = open('inpu.txt', 'r')
sys.setrecursionlimit(10000)


def encryp2(i, j):
    global code_ratio, cnt
    if j > 0:
        if base[i][j] == 0:
            encryp(i, j-1)
            return
    else:
        return
    top = 3
    code_ratio[top] += 1
    for a in range(j-1, -1, -1):
        # print(a)
        if base[i][a] == '0':
            base[i][a] = 0
        if base[i][a+1] == base[i][a]:
            # print(top)
            code_ratio[top] += 1
        else:
            if top > 0:
                top -= 1
                code_ratio[top] += 1
            # else:
            #     top = 3
                # top -= 1
        if code_ratio[0] != 0:
            aa = sum(code_ratio) % 7
            bb = sum(code_ratio) // 7
            if aa == 0:
                for l in range(4):
                    if code_ratio[l] % bb:
                        break
                else:
                    for nn in range(4):
                        code_ratio[nn] //= bb
            # if code_ratio[0] != 0 and cnt % 56 == 0:
                # print(code_ratio)
                    cnt += sum(code_ratio)
                    calculate(code_ratio)
                    code_ratio = [0] * 4  # 초기화
                    # print('재귀', a)
                    encryp(i, a-1)
                    # print('aa', code_ratio)

    return


def encryp3(i, j):
    global code_ratio, cnt
    if j > 0:
        if base[i][j] == 0:
            # encryp(i, j-1)
            return
    else:
        return
    top = 3
    code_ratio[top] += 1
    for a in range(j-1, -1, -1):
        # print(a)
        if base[i][a] == '0':
            base[i][a] = 0
        if base[i][a+1] == base[i][a]:
            # print(top)
            code_ratio[top] += 1
        else:
            if top > 0:
                top -= 1
                code_ratio[top] += 1
            # else:
            #     top = 3
                # top -= 1
        if code_ratio[0] != 0:
            aa = sum(code_ratio) % 7
            bb = sum(code_ratio) // 7
            if aa == 0:
                for l in range(4):
                    if code_ratio[l] % bb:
                        break
                else:
                    for nn in range(4):
                        code_ratio[nn] //= bb
            # if code_ratio[0] != 0 and cnt % 56 == 0:
                # print(code_ratio)
                    cnt += sum(code_ratio)
                    calculate(code_ratio)
                    code_ratio = [0] * 4  # 초기화
                    # print('재귀', a)
                    # encryp(i, a-1)
                    # print('aa', code_ratio)

    return

def encryp(i, j):
    global code_ratio
    # list poping reverse
    top = 3
    while len(base[i]):
        if len(base[i])==0:
            break
        if base[i][-1] == 0:
            base[i].pop(-1)
            continue
        while num_top != -1:
            if len(base[i])==1:
                break
            if code_ratio[0] != 0:
                aa = sum(code_ratio) % 7
                bb = sum(code_ratio) // 7
                if aa == 0:
                    for l in range(4):
                        if code_ratio[l] % bb:
                            break
                    else:
                        for nn in range(4):
                            code_ratio[nn] //= bb
                        calculate(code_ratio)
                        code_ratio = [0] * 4
            if top == -1:
                top = 3
            a = base[i].pop(-1)
            code_ratio[top] += 1
            if base[i][-1] != a:
                top -= 1
                continue


    return


def calculate(lst):  # 코드비율 리스트에 넣어서 8자리만드는거
    global number_list, num_top
    # for i in range(sum(lst), 0, -1):
    #     for j in range(4):
    #         if lst[j] % i:
    #             break
    #     for j in range(4):
    #         lst[j] //= i
    # if num_top == -1:
    #     result.append(enc(number_list))
    #     # print('넘나 리스트한거', number_list)
    #     number_list = [0] * 8
    #     num_top = 7
    # print(base[i])
    # print(lst)
    # print(lst)
    if lst not in cryp:
        return
    key = cryp.index(lst)
    number_list[num_top] = key
    num_top -= 1
    if num_top == -1:
        # print(enc(number_list))
        result.append([enc(number_list),i,number_list])  # if lst[3] == next then pass this idx
        # print('넘나 리스트한거', number_list)
        number_list = [0] * 8
        num_top = 7
        return


def enc(lst):  # 안의 값이 코드가 맞는지 확인하는거
    odd = 0
    even = 0
    for i in range(len(lst)-1):
        if (i+1) % 2:
            odd += lst[i]
        else:
            even += lst[i]
    v_code = (odd*3 + even) % 10
    if (10 - v_code) % 10 == lst[7]:
        # print('sumsum', lst, sum(lst))
        return sum(lst)
    else:
        # print('이거당가')
        return 0


cryp = [[3, 2, 1, 1], [2, 2, 2, 1], [2, 1, 2, 2], [1, 4, 1, 1],
            [1, 1, 3, 2], [1, 2, 3, 1], [1, 1, 1, 4], [1, 3, 1, 2],
            [1, 2, 1, 3], [3, 1, 1, 2]]
testcase = int(input())
for test_num in range(1, testcase+1):
    N, M = map(int, input().split())
    base = [0]*N
    cnt = 0  # 코드뽑아온 전체 길이
    idx = 0
    for i in range(N):
        base[i] = list(map(str, input()))
    # 여기까지 받아오는 부분
    # 암호코드 56의 배수 연속적이라고 생각
    # 16진수 2진수로 변환
    for i in range(N):
        for j in range(M-1, -1, -1):
            if base[i][j] != '0':
                # print(base[i][j], end=' ')
                if base[i][j] == 'A':
                    base[i][j] = 10
                elif base[i][j] == 'B':
                    base[i][j] = 11
                elif base[i][j] == 'C':
                    base[i][j] = 12
                elif base[i][j] == 'D':
                    base[i][j] = 13
                elif base[i][j] == 'E':
                    base[i][j] = 14
                elif base[i][j] == 'F':
                    base[i][j] = 15
                # 16진수 2진수로 변환하려고 바꿔줌
                a = bin(int(base[i][j]))
                b = list(map(int, a[2:]))
                base[i].pop(j)
                if len(b) != 4:
                    for _ in range(4-len(b)):
                        b.insert(0, 0)
                for k in range(len(b)-1, -1, -1):
                    base[i].insert(j, b[k])
            else:
                b = [0, 0, 0, 0]
                base[i].pop(j)
                for k in range(len(b)-1, -1, -1):
                    base[i].insert(j, b[k])
    temp = 10
    result = [0]
    for i in range(N):
        number_list = [0] * 8
        num_top = 7
        code_ratio = [0] * 4  # 문제 제시에 비율 나와있으니 나중에 활용하려고
        encryp(i,-1)
        # while temp > 6:
        #     temp = len(base[i])-1
        #     for j in range(temp, -1, -1):  # 뒤에서 부터 앞으로
        #         if base[i][j] == 1:
        #             encryp(i, j)  # 1만나면 멈춰서 확인해줌
        #             temp = j
        #             print(temp)
        #             if sum(base[i][:temp]) == 0:
        #                 temp = 0
        #             break
        #         else:
        #             pass
        # if cnt != 0:
        #     if idx - cnt > 7:
        #         for j in range(idx - cnt, -1, -1):
        #             if base[i][j] == 1:
        #                 encryp(i, j)
        #                 idx = j
        #                 break
        #             else:
        #                 pass
    # print('다다ㅏ다다답모으므므므으므으므', result)
    print(result)
    a = []
    for i in range(1, len(result)):
        if result[i][2] not in a:
            a.append(result[i][2])
    print(a)
    summ = 0
    laalal = []
    for i in range(1, len(result)):
        if result[i][2] not in laalal:
            summ += result[i][0]
            laalal.append(result[i][2])
    summ = 0
    # while len(result) != 1:
    for i in range(1,len(result)):
        for j in range(i+1, len(result)):
            if result[i][2] == result[j][2] and result[i][1]+1 == result[j][1] and result[i][1] - result[j][1] < 10 :
                result[j][0] = 0
    for i in range(1,len(result)):
        summ += result[i][0]
    # if len(result) > 2:
    #     for i in range(1,len(result)):
    #         if result[i][2] not in laalal:
    #             summ += result[i][0]
    #             laalal.append(result[i][2])
    #     # while len(result) == 3:
    #     #     if result[1][2] == result[2][2]:
    #     #         result.pop(2)
    #     #     else:
    #     #         summ += result[1][0]
    #             # result.pop(1)
    #         # if result[i][0] != result[i+1][0] or result[i][2] != result[i+1][2]:
    #     summ += result[1][0]
    # elif len(result) ==2:
    #     summ = result[1][0]
    # else:
    #     summ = 0
    # print(result)
    print('#{} {}'.format(test_num, summ))
    # if not result[0]:
    #     print('0')
    #     # print('{}'.format(sum(set(result))))
    # else:
    # print(result)
    # print('{}'.format(sum(set(result))), end='')
    # print()
