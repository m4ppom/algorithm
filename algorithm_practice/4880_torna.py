import sys
sys.stdin = open('input0828.txt', )


# def rsp(no1, no2):
#     if no1==1 and no2==2:
#         return 2
#     elif no1 == 2 and no2 == 3:
#         return 3
#     elif no1 == 1 and no2 == 3:
#         return 1
#     elif no1 == no2:
#         return no1
#
#
# def dividing(list):
#
#     new_list = [[]for _ in range(2)]  # *
#     # print('ss',len(list))
#     for i in range(0,len(list)//2):
#         new_list[0]+=[list[i]]
#     for i in range((len(list)//2), len(list)):
#         new_list[1]+=[list[i]]
#     # print(new_list)
#     return new_list
#
# testcase = int(input())
#
# for tc_num in range(testcase):
#     result = 0
#     people = int(input())
#     people_list = [0]*people
#     card_info = list(map(int, input().split()))
#     for i in range(len(card_info)):
#         people_list[i] = card_info[i]
#     print(people_list)
#     people_list = dividing(people_list)
#     print(people_list)
#     print(len(people_list[0]))
#     if len(people_list[0]) > 2:
#         new_list = dividing(people_list[0])
#         print(new_list)
#
#

    # print('#{} {}'.format(tc_num, result))

def play_game(a, b):
    if a[1] == 1:
        if b[1] == 1:
            return a
        elif b[1] == 2:
            return b
        elif b[1] == 3:
            return a
    elif a[1] == 2:
        if b[1] == 1:
            return a
        elif b[1] == 2:
            return a
        elif b[1] == 3:
            return b
    elif a[1] == 3:
        if b[1] == 1:
            return b
        elif b[1] == 2:
            return a
        elif b[1] == 3:
            return a


def devision(group, lst):
    if len(group) == 1:
        lst.append(*group)
        winners.append(*group)
        if len(lst) == 2:
            b = lst.pop(-1)
            a = lst.pop(-1)
            winners.pop()
            winners.pop()
            winner = play_game(a, b)
            winners.append(winner)

    else:
        cnt = len(group)
        pivot = (1 + cnt) // 2
        tmp = []
        for i in [group[:pivot], group[pivot:]]:
            devision(i, tmp)

testcase = int(input())
for tc_num in range(1, testcase+1):
    people = int(input())
    group = []
    card = list(map(int, input().split()))
    for i in range(people):
        group.append((i+1, card[i]))
    winners = []
    while True:
        devision(group, [])
        group = winners.copy()
        winners.clear()
        if len(group) == 1:
            break
    print("#{} {}".format(tc_num, *group[0]))