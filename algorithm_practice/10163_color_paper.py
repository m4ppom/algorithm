testcase = int(input())
cord_info = [0]*testcase
for num in range(testcase):
    # print(testcase)
    cord_info[num] = list(map(int, input().split()))
    # print(cord_info)
cord_maxi_1 = 0
cord_maxi_2 = 0
# for i in range(len(cord_info)):
#     if cord_info[i][0] + cord_info[i][2] > cord_maxi_1:
#         cord_maxi_1 = cord_info[i][0] + cord_info[i][2]
#     if cord_info[i][1] + cord_info[i][3] > cord_maxi_2:
#         cord_maxi_2 = cord_info[i][1] + cord_info[i][3]
count = [0]*testcase
# base = [[0 for i in range(cord_maxi_1)] for _ in range(cord_maxi_2)]
base = [[0 for i in range(101)] for _ in range(101)]
for num in range(len(cord_info)):
    for i in range(cord_info[num][0], cord_info[num][0]+cord_info[num][2]):
        for j in range(cord_info[num][1], cord_info[num][1]+cord_info[num][3]):
            if base[i][j] == 0:
                base[i][j] = num+1
                count[num] += 1
            elif base[i][j] != 0:
                count[base[i][j]-1] -= 1
                base[i][j] = num + 1
                count[num] += 1
for i in range(testcase):
    print(count[i])
# print(len(base))
# print(len(base[0]))
# for num in range(1,testcase +1):
#     # print('num',num)
#     count = 0
#     for i in range(len(base)):
#         for j in range(len(base[0])):
#             if base[i][j] == num:
#                 count += 1
# for i in range(testcase):
#     print(count[i])
# print(base)















