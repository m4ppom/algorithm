arr = [
    [9, 20, 2, 18, 11],
    [19, 1, 25, 3, 21],
    [8, 24, 10, 17, 7],
    [15, 4, 16, 5, 6],
    [12, 13, 22, 23, 14],
]
# arr2 = [
#    [1, 2, 3, 4, 5],
#    [2, 3, 4, 5, 6],
#    [3, 4, 5, 6, 7],
#    [4, 5, 6, 7, 8],
#    [5, 6, 7, 8, 9],
#       ]
dx = [0, 1, 0, 1]
dy = [1, 0, -1, 0]
k = 0
count = 0
number = 4
for i in range(5):
    for j in range(5):
        temp = arr[i][j]
        for _ in range(4):
            if i + dx[k] > -1 and j + dy[k] > -1 and i + dx[k] < 5 and j + dy[k] < 5:
                if temp > int(arr[i + dx[k]][j + dy[k]]):
                    print(arr[i][j])
                    print(arr[i + dx[k]][j + dy[k]])
                    temp = arr[i + dx[k]][j + dy[k]]
                    a = i + dx[k]
                    b = j + dy[k]
                    i += dx[k]
                    j += dy[k]
                else:
                    i += dx[k]
                    j += dy[k]

        while count < 2:
            for num in range(number):
                if i + dx[k] > -1 and j + dy[k] > -1 and i + dx[k] < 5 and j + dy[k] < 5:
                    if arr[i][j] > arr[i + dx[k]][j + dy[k]]:
                        temp = arr[i + dx[k]][j + dy[k]]
                        a = i + dx[k]
                        b = j + dy[k]
                        i += dx[k]
                        j += dy[k]
                    else:
                        i += dx[k]
                        j += dy[k]
                else:  # 방향 바꾸기.
                    if k == 3:
                        k = 0
                        count += 1
                    else:
                        k += 1
                        count += 1
            number -= 1

        arr[a][b] = arr[i][j]
        arr[i][j] = temp
print(arr)
