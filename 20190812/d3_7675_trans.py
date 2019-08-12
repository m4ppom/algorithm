test_case = input()
sum_list = []
sum_sum = 0
for i in test_case:
    number_list = input().split()
    if len(number_list) > 3:
        for j in range(1, len(number_list)-2):
            for k in range(-1, 2, 1):
                sum_sum += int(number_list[j+k])
            sum_list.append(sum_sum)
        result = max(sum_list) - min(sum_list)
    elif len(number_list) == 2:
        for num in number_list:
            sum_list.append(int(num))
        result = max(sum_list)-min(sum_list)
    # else:
    #     result =
    print("#%d %d" % (i, result))
