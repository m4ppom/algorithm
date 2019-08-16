test_case = int(input())
for numbers in range(1, test_case + 1):
    nasa_number = int(input())
    # nasa_list = [0] * nasa_number
    nasa_info = input().split()
    count = 0
    nasa_modum = [[0 for _ in range(2)] for _ in range(nasa_number)]
    while len(nasa_info) != 0:
        for i in range(2):
            nasa_modum[count][i] = nasa_info[i]
        nasa_info.pop(0)
        nasa_info.pop(0)
        count += 1
    while len(nasa_modum) != 1:
        for i in range(0, len(nasa_modum) - 1):
            for j in range(i + 1, len(nasa_modum)):
                if nasa_modum[i][-1] == nasa_modum[j][0]:
                    nasa_modum[i] += nasa_modum[j]
                    nasa_modum.pop(j)
                    break
                elif nasa_modum[i][0] == nasa_modum[j][-1]:
                    nasa_modum[j] += nasa_modum[i]
                    nasa_modum.pop(i)
                    break
                else:
                    pass
        if len(nasa_modum) > 1:
            if nasa_modum[0][-1] == nasa_modum[1][0]:
                nasa_modum[0] += nasa_modum[1]
                nasa_modum.pop(1)

            elif nasa_modum[0][0] == nasa_modum[1][-1]:
                nasa_modum[1] += nasa_modum[0]
                nasa_modum.pop(0)

    print('#{}'.format(numbers), end=' ')
    for i in range(len(nasa_modum[0])):
        print('{}'.format(nasa_modum[0][i]), end=' ')
    print('')