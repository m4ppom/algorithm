for tri in range(1, 11):
    test_case = int(input())
    numbers = []
    number_list = input().split()
    for i in number_list:
        numbers.append(int(i))
    for _ in range(test_case):
        idxmax = numbers.index(max(numbers))
        idxmin = numbers.index(min(numbers))
        numbers[idxmax] -= 1
        numbers[idxmin] += 1
    result = max(numbers)-min(numbers)
    print('#{} {}'.format(tri, result))

    # n, m = map(int, input().split())