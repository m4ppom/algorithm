test_case = int(input())
for case in range(1,test_case+1):
    numbers = int(input())
    number_list = input().split()
    new_list = []
    for app in number_list:
        new_list.append(int(app))
    new_list = sorted(new_list)
    sub_num = new_list[len(new_list)-1] - new_list[0]

    print('#{} {}'.format(case, sub_num))