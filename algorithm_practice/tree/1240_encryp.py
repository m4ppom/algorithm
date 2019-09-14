import sys
sys.stdin = open('inpu.txt', 'r')


def enc(lst):
    odd = 0
    even = 0
    for i in range(len(lst)):
        if (i+1) % 2:
            odd += lst[i]
        else:
            even += lst[i]
    v_code = (odd*3 + even) % 10
    if v_code == 0:
        return v_code
    else:
        v_code = 10 - v_code
        return v_code
# lst.append(vcode)

testcase = int(input())
cryp = [[0,0,0,1,1,0,1], [0,0,1,1,0,0,1], [0,0,1,0,0,1,1], [0,1,1,1,1,0,1],
        [0,1,0,0,0,1,1], [0,1,1,0,0,0,1], [0,1,0,1,1,1,1], [0,1,1,1,0,1,1],
        [0,1,1,0,1,1,1], [0,0,0,1,0,1,1]]
for test_num in range(1, testcase+1):
    N, M = map(int, input().split())
    base = [0]*N
    # death_note = []
    for i in range(N):
        base[i] = list(map(int, input()))
        # if sum(base[i]) == 0:
        #     death_note.append(i)
    # print(death_note)
    # for i in range(len(death_note)-1, -1, -1):
    #     base.pop(death_note[i])
    # print(base)
    num_list = [0]*7
    cryp_list = [0]*8
    summ = 0
    for i in range(len(base)):
        top = 7
        while len(base[i]) > 6 :
            if base[i][-1] == 1:
                for j in range(7):
                    num_list[6 - j] = base[i].pop(-1)
                key = cryp.index(num_list)
                cryp_list[top] = key
                top -= 1
            else:
                base[i].pop(-1)
        # if enc(cryp_list[0:7]) == cryp_list[7] and sum(cryp_list) != 0:
        if (10-((3*(cryp_list[0]+cryp_list[2]+cryp_list[4]+cryp_list[6])+cryp_list[1]+cryp_list[3]+cryp_list[5])%10)%10) == cryp_list[7] and sum(cryp_list) != 0:
            summ = sum(cryp_list)
            break
    print('#{} {}'.format(test_num, summ))

# a = [7,5,7,5,5,0,2,7]
# if enc(a[0:7]) == a[7]:
#     print(a[7])