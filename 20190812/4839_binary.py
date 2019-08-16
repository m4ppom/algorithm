test_case = int(input())
for number in range(1, test_case +1):
    info = list(map(int, input().split()))
    count_a = count_b = 0
    left_a = left_b = 1
    right_a = right_b = info[0]
    stop = 1
    center_a = center_b = int((left_a+right_a)/2)
    while stop:
        if info[1] == center_a:
            pass
        else:
            if info[1] > center_a:
                left_a = center_a
                center_a = int((left_a + right_a)/2)
                count_a += 1
            else:
                right_a = center_a
                center_a = int((left_a + right_a) / 2)
                count_a += 1

        if info[2] == center_b:
            pass
        else:
            if info[2] > center_b:
                left_b = center_b
                center_b = int((left_b + right_b)/2)
                count_b += 1
            else:
                right_b = center_b
                center_b = int((left_b + right_b) / 2)
                count_b += 1

        if center_a == info[1] and center_b == info[2]:
            stop = 0

    if count_b == count_a:
        result = 0
    elif count_b < count_a:
        result = 'B'
    else:
        result = 'A'
    print('#{} {}'.format(number, result))