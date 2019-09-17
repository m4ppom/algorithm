import sys
sys.setrecursionlimit(100000)
import itertools


def swap(k, i):
    temp = array[k]
    array[k] = array[i]
    array[i] = temp
    return


def perm(n, k):
    if k == n:
        print(array)
        return
    else:
        for i in range(k, n):
            swap(k, i)
            perm(n, k+1)
            # print(array)
            swap(k, i)
            # print(array)
        # print(array)


array = [1, 2, 3]
array2 = [6, 6, 7, 7, 6, 7]
array3 = [1, 0, 1, 1, 2, 3]
perm(3, 0)

arr = [3, 6, 7, 1, 5, 4]
n = len(arr)

for i in range(0, (1 << n)):
    for j in range(0, n):
        if i & (1 << j):
            print('{}'.format(arr[j]), end=' ')
    print()


arr_list = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
temp_list = [0]*len(arr_list)


def combination(n, r):
    global temp_list
    if r == 0:
        if sum(temp_list) == 0:
            a = sorted(temp_list)
            if a not in new:
                new.append(a)
            for i in range(len(temp_list)):
                if temp_list[i] != 0:
                    print(temp_list[i], end=' ')
            print()
    elif n < r:
        return
    else:
        temp_list[r-1] = arr_list[n-1]
        combination(n-1, r-1)
        combination(n-1, r)


new = []
for i in range(1, len(temp_list)+1):
    combination(len(arr_list), i)
print(len(new), new)


def comb(n, r):
    global res
    if r == 0:
        res += 1
        return
    elif r == n:  # 이거넣으면 아래 추가해주는 부분 추가해줘야하고 리턴 아니면 한개 안들어감
        res += 1
        return
    elif n < r:
        res += 1
        return
    else:
        comb(n-1, r-1)
        comb(n-1, r)

res = 0
comb(5, 2)
print(res)
aa = list(itertools.combinations(arr_list, 3))
print(aa)