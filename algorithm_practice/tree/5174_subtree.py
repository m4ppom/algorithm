import sys
sys.stdin = open('inpu.txt', 'r')


def counter(a):
    global count
    if node_info2[a]:
        for i in range(len(node_info2[a])):
            count += 1
            counter(node_info2[a][i])



testcase = int(input())
for test_num in range(1, testcase+1):
    result = 0
    E, N = map(int, input().split())
    info = list(map(int, input().split()))
    node_info = [0] * (E + 2)
    node_info2 = [[] for _ in range(E + 2)]
    nonodede = [0]*E
    cnt = [0]*(E + 2)
    for i in range(E):
        nonodede[i] = [info[2*i], info[2*i+1]]
        node_info[info[2 * i]] += 1
        # node_info[info[2 * i+1]] += 1
    for i in range(E):
        node_info2[nonodede[i][0]].append(nonodede[i][1])
    # print(nonodede)
    # print(node_info)
    # print(node_info2)
    count = 0
    counter(N)
    # print(count)
    # for i in range(1,E+2):
    #     if nonodede[i] == 0:











    print('#{} {}'.format(test_num, count+1))