# a =[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1],[1,5,10,10,5,1],[1,6,15,20,15,6,1],[1,7,21,35,35,21,7,1],[1,8,28,56,70,56,28,8,1],[1,9,36,84,126,126,84,36,9,1],[1,10,45,120,210,252,210,120,45,10,1],[1,11,54,156,294,378,294,156,54,11,1],[1,12,64,201,414,588,414,201,64,12,1]]
# testcase = int(input())
# for test_num in range(1, testcase+1):
#     N = int(input())
#     print('#{}'.format(test_num))
#     for i in range(N):
#         for j in range(len(a[i])):
#             print(a[i][j],end=' ')
#         print()

import copy
n=0
a=0
for _ in range(int(input())):
    list1 = []
    list2=[]
    n+=1
    print('#{}'.format(n))
    for i in range(int(input())):
        if i == 0:
            list1.append(1)
            print(' '.join(map(str, list1)))
        elif i == 1:
            list1.append(1)
            print(' '.join(map(str, list1)))
        elif i >1:
            list2.append(1)
            for j in range(1,i):
                a = list1[j-1]+list1[j]
                list2.append(a)
            list2.append(1)
            print(' '.join(map(str, list2)))
            list1=copy.deepcopy(list2)
            list2=[]