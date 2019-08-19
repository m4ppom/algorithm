test_case = int(input())
for number in range(1, test_case +1):
    base = [[0 for _ in range(10)] for _ in range(10)]
    count = 0
    square_number = int(input())
    for sqn in range(square_number):
        area_info = list(map(int, input().split()))
        for x in range(area_info[0], area_info[2]+1):
            for y in range(area_info[1], area_info[3]+1):
                base[y][x] += 10**area_info[4]
    for i in range(10):
        for j in range(10):
            a = base[i][j] % 100
            b = base[i][j] // 100
            if a != 0 and b != 0 :
                count += 1
    print('#{} {}'.format(number, count))

# 3
# 2
# 2 2 4 4 1
# 3 3 6 6 2
# 3
# 1 2 3 3 1
# 3 6 6 8 1
# 2 3 5 6 2
# 3
# 1 4 8 5 1
# 1 8 3 9 1
# 3 2 5 8 2