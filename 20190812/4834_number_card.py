test_case = int(input())
for i in range(1, test_case+1):
    length = int(input())
    number = int(input())
    number_list = []
    sol = 0
    for _ in range(length):
        sol = number % 10
        number //= 10
        number_list.append(sol)

    dictionary = {}
    for j in range(length-1):
        count = 1
        for k in range(j+1, length):
            if number_list[j] == number_list[k]:
                number_list[k] = -1
                count += 1
        dictionary.update({number_list[j]: count})
    count, number = max(zip(dictionary.values(), dictionary.keys()))
    print('#{} {} {}'.format(i, number, count))


# 3
# 10 3
# 1 2 3 4 5 6 7 8 9 10
# 10 5
# 6262 6004 1801 7660 7919 1280 525 9798 5134 1821
# 20 19
# 3266 9419 3087 9001 9321 1341 7379 6236 5795 8910 2990 2152 2249 4059 1394 6871 4911 3648 1969 2176