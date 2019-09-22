import sys
sys.stdin = open('combi.txt', 'r')


import copy
def swap(k, i):
    temp = array[k]
    array[k] = array[i]
    array[i] = temp
    return


def perm(n, k):
    if k == n:
        a = copy.deepcopy(array)
        new.append(a)
        return
    else:
        for i in range(k, n):
            swap(k, i)
            perm(n, k+1)
            swap(k, i)
array = list(map(int, input().split()))
N = int(input())
new = []
perm(len(array), 0)
new.sort()
for i in range(len(array)):
    print('%d'%(new[N-1][i]),end='')
print()

