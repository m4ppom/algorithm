import sys
sys.stdin = open('movie666.txt', 'r')
import collections

num = int(input())
devil = collections.deque()
cnt = 0
# devil.append(666)
# devil.append(1666)
# devil.append(2666)
# devil.append(3666)
# devil.append(4666)
# devil.append(5666)
find_num = 665
while True:
    if cnt == num:
        print(devil[num-1])
        break
    find_num += 1
    mmm = find_num
    while mmm:
        if mmm % 1000 == 666:
            devil.append(find_num)
            cnt+=1
            break
        else:
            mmm //= 10
