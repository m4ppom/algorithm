import sys
sys.stdin = open('input0902.txt', 'r')


def linear_increase(num1_index, num):
    global N
    global result
    if num1_index + num >= N:
        return result
    left = num_list[num1_index] * num_list[num1_index+num]
    if len(str(left)) == 1:
        pass
    else:
        for i in range(len(str(left))-1):
            if str(left)[i] <= str(left)[i+1]:
                pass
            else:
                # linear_increase(num1_index, num+1)
                return
    if result < left:
        result = left
        return
    # linear_increase(num1_index+num, num+1)
    # linear_increase(num1_index+1, num)
    # linear_increase(num1_index + 1, num2_index + 1)


testcase = int(input())
for test_num in range(1, testcase+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    num = 1
    result = -1
    if N == 1:
        result = -1
    else:
        for i in range(N):
            for j in range(1, N-i):
                linear_increase(i, j)
    # linear_increase(0, num)
    print('#{} {}'.format(test_num, result))
# 10**n
