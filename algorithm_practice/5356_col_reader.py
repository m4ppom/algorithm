import sys
sys.stdin = open('input0902.txt', 'r')


def reader(base):
    global result
    # cnt = 0
    for i in range(15):
        for j in range(5):
            if len(base[j]) <= i:
                continue
            else:
                result += base[j][i]
        # return


testcase = int(input())
for test_num in range(1, testcase + 1):
    base = [0]*5
    for i in range(5):
        base[i] = list(map(str, input()))
    # print(base)
    result = []
    # print(len(base[1]))
    reader(base)
    # print(len(base[1]))
    print('#{} '.format(test_num), end='')
    for i in range(len(result)):
        print('{}'.format(result[i]),end='')
    print()

