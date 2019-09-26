import sys
sys.stdin = open('honey.txt', 'r')
import copy
import collections
import itertools


def finder(index, start, N, M):
    global vivivisit, afufufu, size
    maxq = 0
    if index == M:
        mul = 0
        summ = 0
        # print(afufufu)
        for i in range(len(afufufu)):
            summ += afufufu[i]
            mul += afufufu[i]**2
        if summ <= size:
            if maxq < mul:
                maxq = mul
                # print(maxq,'mamam')
        return maxq
    for i in range(start, N + 1):
        if vivivisit[i]:
            continue
        vivivisit[i] = 1
        afufufu[index] = i
        finder(index + 1, i + 1, N, M)
        vivivisit[i] = 0


def combination(arr, r):
    arr = sorted(arr)
    mamam = []
    def generate(chosen):
        if len(chosen) == r:
            # print(chosen, 'ad')
            mmm = copy.deepcopy(chosen)
            mamam.append(mmm)
            return
        start = arr.index(chosen[-1]) + 1 if chosen else 0
        for nxt in range(start, len(arr)):
            chosen.append(arr[nxt])
            generate(chosen)
            chosen.pop()
    generate([])
    # print(mamam)
    return mamam


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


def comb_i():
    for i in range(N - 1):
        for j in range(i + 1, N):
            print(a[i], a[j])
            mmm = copy.deepcopy(chosen)
    return mmm


def comb_r(k, s):
    if k == R:
        print(t[0], t[1])
        mmm = copy.deepcopy(chosen)
    else:
        for i in range(s, N + (k - R) + 1):
            t[k] = a[i]
            comb_r(k + 1, i + 1)
    return mmm

def finder2(q1, num):
    global qua
    maxq = 0
    # for i in range(1, num+1):
    # afufufu = perm(q1, num)
    afufufu = []
    for i in range(1, len(q1) + 1):
        els = [list(x) for x in itertools.combinations(q1, num)]
        afufufu.extend(els)
    # afufufu = [list()for x in itertools.combinations(q1, num)]
    # print(afufufu)
    # print('adadad', afufufu)
    # print(afufufu)
    for kkk in range(len(afufufu)):
        mul = 0
        summ = 0
        for b in range(len(afufufu[kkk])):
            summ += afufufu[kkk][b]
            mul += afufufu[kkk][b] ** 2
        if summ <= qua:
            if maxq < mul:
                maxq = mul
                # print(maxq, 'mamam')
    return maxq




def honeyhoney(q1, q2, qua):
    global maxhoney
    global vivivisit, afufufu
    maxa = 0
    maxb = 0
    for i in range(1, len(q1)+1):
        a = finder2(q1, i)
        if maxa < a:
            maxa = a
    for i in range(1, len(q2)+1):
        b = finder2(q2, i)
        if maxb < b:
            maxb = b
    return maxa + maxb


testcase = int(input())
for test_num in range(1, testcase+1):
    size, number, qua = map(int, input().split())
    hive = [list(map(int, input().split()))for _ in range(size)]
    maxhoney = 0
    for iii in range(size):
        for jjj in range(size - number+1):
            # honeyhoney(i, j)
            q1 = collections.deque()
            q2 = collections.deque()
            for aaa in range(number):
                # print(i, a)
                q1.append(hive[iii][jjj+aaa])
                hive[iii][jjj + aaa] = 0
            for ix in range(size):
                for jx in range(size - number+1):
                    if hive[ix][jx] == 0:
                        continue
                    else:
                        for a in range(number):
                            q2.append(hive[ix][jx + a])
                            hive[ix][jx + a] = 0
                        hu = honeyhoney(q1, q2, qua)
                        if maxhoney < hu:
                            maxhoney = hu
                            # print('honey', maxhoney)
                        for a in range(number):
                            hive[ix][jx + a] = q2.popleft()
            for a in range(number):
                hive[iii][jjj + a] = q1.popleft()
    print('#%d %d' %(test_num, maxhoney))




