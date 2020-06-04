# "ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"
import  sys
sys.stdin = open("inpu.txt", "r")

test_case = int(input())
num_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for numbers in range(1, test_case + 1):
    trans_list= []
    tc = input().split()
    test_case = int(tc[1])
    foreign = input().split()
    for i in foreign:
        for j in range(len(num_list)):
            if i == num_list[j]:
                trans_list += str(j)
    for i in range(len(trans_list)):
        for j in range(i, len(trans_list)):
            if trans_list[i] > trans_list[j]:
                temp = trans_list[i]
                trans_list[i] = trans_list[j]
                trans_list[j] = temp
    result = []
    for i in trans_list:
        result += num_list[int(i)]
    print('#{}'.format(numbers))
    for i in range(int(len(result)/3)):
        for j in range(3):
            print('{}'.format(result[3*i + j]), end='')
        print(' ',end='')
    print('')
