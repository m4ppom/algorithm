import sys
sys.stdin =open('input0902.txt', 'r')

testcase = int(input())
for test_num in range(1, testcase +1):
    line = [0] * 5001
    N = int(input())
    for _ in range(N):
        info = list(map(int, input().split()))
        for i in range(info[0], info[1]+1):
            line[i] += 1
    p = int(input())
    p_list = [0] * p
    for i in range(p):
        p_list[i] = int(input())
    print('#{} '.format(test_num), end='')
    for i in p_list:
        print('{} '.format(line[i]), end='')
    print()