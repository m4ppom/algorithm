import sys
sys.stdin = open('thinq.txt', 'r')

N, M = map(int, input().split())
lst = [num for num in range(N+1)]
lst.pop(0)
wanna = list(map(int, input().split()))
idx = 0
func_pop = 0
func_shift_left = 0
func_shift_right = 0
for i in range(M):
    find = lst.index(wanna[i])
    if find > idx:
        left  = len(lst)-find + idx
        right = find - idx
    elif find < idx:
        left = idx - find
        right = len(lst)-idx+find

    if find == idx:
        lst.pop(idx)
    elif left > right:
        lst.pop(find)
        idx = find
        if find > len(lst)-1:
            idx =0
        func_shift_left+= right
    elif right > left:
        lst.pop(find)
        idx = find
        if idx > len(lst)-1:
            idx = 0
        func_shift_right += left
    else:
        lst.pop(find)
        idx = find
        if idx > len(lst)-1:
            idx = 0
        func_shift_left += right
print(func_shift_right + func_shift_left)


