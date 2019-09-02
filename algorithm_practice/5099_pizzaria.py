import sys
sys.stdin = open('input0902.txt', 'r')

testcase = int(input())
for test_num in range(1, testcase+1):
    info = list(map(int, input().split()))
    pizza = list(map(int, input().split()))
    fire = [0] * info[0]
    while len(pizza) != 0 and sum(fire) != 0:
        for i in range(info[1]):
            fire[i] = pizza[i]



