import sys
sys.stdin = open('input0902.txt', 'r')

testcase = int(input())
for test_num in range(1, testcase+1):
    card_list = [[0 for _ in range(14)]for _ in range(4)]
    got = input()
    print(card_list, got)

    # print(type(got), len(got))
    for i in range(len(got)//3):
        result = 0
        # print(card_list)
        shape = got[3*i]
        number = got[3*i+1]
        number += got[3*i+2]
        # print(number)
        if shape == 'S':
            card_list[0][int(number)] += 1
            if card_list[0][int(number)] >= 2:
                result = 'ERROR'
                break
        elif shape == 'D':
            card_list[1][int(number)] += 1
            if card_list[1][int(number)] >= 2:
                result = 'ERROR'
                break
        elif shape == 'H':
            card_list[2][int(number)] += 1
            if card_list[2][int(number)] >= 2:
                result = 'ERROR'
                break
        elif shape == 'C':
            card_list[3][int(number)] += 1
            if card_list[3][int(number)] >= 2:
                result = 'ERROR'
                break
    if result == 'ERROR':
        print('#{} {}'.format(test_num, result))
    else:
        print('#{} '.format(test_num), end='')
        for i in range(4):
            a = 13 - sum(card_list[i])
            print('{} '.format(a), end='')
        print()

    # print('#{} {}'.format(test_num, result))