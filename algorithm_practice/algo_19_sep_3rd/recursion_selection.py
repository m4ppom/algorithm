import copy


def recursion(list):
    global cnt, temp, search
    if search == len(base)-1:
        list[temp[1]] = list[cnt]
        list[cnt] = temp[0]
        search = 0
        cnt += 1
        return
    if visit[cnt] == 0:
        visit[cnt] = 1
        temp = [list[cnt], cnt]
    search += 1
    if visit[search] == 0 and list[search] < temp[0]:
        temp = [list[search], search]
        search += 1
        recursion(list)


def recsele(A, s, e):
    if s == e:
        return
    mini = s
    for j in range(s+1, e):
        if A[j] < A[mini]
            mini = j
    A[s], A[mini] = A[mini], A[s]
    recsele(A, s+1, e)

cnt = 0
search = 0
temp = 100
base = [3, 1, 5, 8, 7, 2, 9, 4, 9, 10]
coopy = copy.deepcopy(base)
visit = [0]*len(base)
while sum(visit) != len(base):
    recursion(base)
print(base)