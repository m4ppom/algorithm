test_case = int(input())
for numbers in range(1, test_case + 1):
    number = int(input())
    number_list = list(map(int, input().split()))
    maximum = 0
    minimum = 100
    for idx in range(len(number_list)):
        maximum = 0
        minimum = 100
        if idx % 2:  # if odd number
            for find_mini in range(idx, len(number_list)):
                if number_list[find_mini] < minimum:
                    temp = minimum
                    minimum = number_list[find_mini]
                    number_list[find_mini] = temp
            number_list[idx] = minimum

        else:
            for find_max in range(idx, len(number_list)):
                if number_list[find_max] > maximum:
                    temp = maximum
                    maximum = number_list[find_max]
                    number_list[find_max] = temp
            number_list[idx] = maximum

    print('#{}'.format(numbers), end=' ')
    for i in number_list[:10]:
        print('{}'.format(i), end=' ')
    print('')
