first_number2 = int(input())
# second_number = int(first_number/2)+int(first_number**0.5)+ int(first_number**0.25)
for second_number in range(int(first_number2/2), first_number2):
    list_list = []
    first_number = first_number2
    list_list.append(first_number)
    list_list.append(second_number)
    while first_number > 0:
        temp = first_number - second_number
        first_number = second_number
        if temp < 0:
            break
        second_number = temp
        list_list.append(temp)
    count = len(list_list)
    nu = []
    for i in list_list:
        nu.append(str(i))
    result = ' '.join(nu)
    print(count)
    print(result)
