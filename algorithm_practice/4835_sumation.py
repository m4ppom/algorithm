test_case = input()
for i in range(1,int(test_case)+1):
    sum_sum = 0
    sum_list = []
    sum_leng = input().split()
    number_list = input().split()
    for j in range(len(number_list)-int(sum_leng[1])+1):
        for k in range(int(sum_leng[1])):
            sum_sum += int(number_list[j+k])
        sum_list.append(sum_sum)
        sum_sum = 0
    result = max(sum_list) - min(sum_list)
    print("#%d %d" % (i, result))
