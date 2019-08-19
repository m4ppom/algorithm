# arr = [
#    [9,20,2,18,11],
#    [19,1,25,3,21],
#    [8,24,10,17,7],
#    [15,4,16,5,6],
#    [12,13,22,23,14],
#       ]
# # arr2 = [
# #    [1, 2, 3, 4, 5],
# #    [2, 3, 4, 5, 6],
# #    [3, 4, 5, 6, 7],
# #    [4, 5, 6, 7, 8],
# #    [5, 6, 7, 8, 9],
# #       ]
# dx = [1,0,-1,0]
# dy = [0, 1, 0, -1]
# k = 0
# count= 0
# number = 4
# for i in range(5):
#     for j in range(5):
#         for _ in range(5):
#             if i + dx[k] > -1 and j + dy[k] > -1 and i + dx[k] < 5 and j + dy[k] < 5:
#                 temp = arr[i + dx[k]][j + dy[k]]
#                 if  arr[i][j] > arr[i + dx[k]][j + dy[k]]:
#                     temp = arr[i + dx[k]][j + dy[k]]
#                     a = i + dx[k]
#                     b = j + dy[k]
#                 else:
#                     pass
#         while count< 2:
#             for num in range(number):
#                 if i + dx[k] > -1 and j + dy[k] > -1 and i + dx[k] < 5 and j + dy[k] < 5:
#                     temp = arr[i + dx[k]][j + dy[k]]
#                     if  arr[i][j] > arr[i + dx[k]][j + dy[k]]:
#                         temp = arr[i + dx[k]][j + dy[k]]
#                         a = i + dx[k]
#                         b = j + dy[k]
#                     else:
#                         pass
#                 else:  # 방향 바꾸기.
#                     if k == 3:
#                         k = 0
#                         count += 1
#                     else:
#                         k += 1
#                         count += 1
#             number -= 1
#
#         arr[a][b] = arr[i][j]
#         arr[i][j] = temp
# print(arr)

544332211
arr1 = [
   [9,20,2,18,11],
   [19,1,25,3,21],
   [8,24,10,17,7],
   [15,4,16,5,6],
   [12,13,22,23,14],
      ]
arr2 = [
   [1,20,2,18,11],
   [19,9,25,3,21],
   [8,24,10,17,7],
   [15,4,16,5,6],
   [12,13,22,23,14],
      ]
dx = [1,0,-1,0]
dy = [0, 1, 0, -1]
count = 0 
while count < 25:
    for i in range(5):
        for j in range(5):
