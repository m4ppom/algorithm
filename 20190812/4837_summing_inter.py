# test_case = int(input())
# for number in range(1, test_case +1):
#     count = 0
#     # sum_list = 0
#     # num_list = [1,2,3,4,5,6,7,8,9,10,11,12]
#     info = list(map(int, input().split()))
#     #
#     # for i in range(12):
#     #     if num_list[i] > info[1]:
#     #         num_list.pop(i)
#     # for j in range(len(num_list)):
#     #     if num_list[j] < info[1]:
#     #         sum_list += num_list[j]
#     #         count += 1
#     #         if info[0] != count or info[1] != sum_list:
#     #             break
#     #         else:
#     #
#     # else:
#     #     sum_list += num_list[]
#     #     count += 1
#     #
#     # if info[0] != count or info[1] != sum_list:
#     #     continue
#     # else:
#     #     print('#{} {}'.format(number, count))
#
#
#
#     num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#     n = len(num_list)
#     li = []
#     for i in range(1<<n):
#         for j in range(n+1):
#             if i & (1<<j):
#                 if i == info[1] and info[0] == len(i):
#                     count += 1
#     print('#{} {}'.format(number, count))
#


num_list = [1,2,3,4,5,6,7,8,9,10,11,12]
n = len(num_list)
part_num_list = [0]*(2**12-1)
for i in range(1,1<<n):
    part_part = []
    for j in range(n+1):
        if i & (1 << j):
            part_part.append(num_list[j])
    part_num_list[i-1] = part_part
# part_num_list라는 리스트에 num_list의 모든 부분집합을 넣음
test_case = int(input())
for i in range(test_case):
    b, c = map(int,input().split())
    count = 0
    for j in part_num_list:
        if len(j) == b and sum(j) == c:
            count += 1
    print('#%d %d' %(i+1, count))


