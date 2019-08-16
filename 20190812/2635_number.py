first_number2 = int(input())
result2 = []
first_number = first_number2
# second_number = int(first_number/2)+int(first_number**0.5)+ int(first_number**0.25)
for second_number in range(int(first_number2/2)+int(first_number2**0.5),int(first_number2/2)+int(2*first_number2**0.5)):
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
    result2.append(count)
    nu = []
    for i in list_list:
        nu.append(str(i))
    result = ' '.join(nu)
    # print(count)
    # print(result)
n = result2.index(max(result2))
second_number = (int(first_number2/2)+int(first_number2**0.5) + n
list_list = []
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
result.append(count)
nu = []
for i in list_list:
    nu.append(str(i))
result = ' '.join(nu)
print(count)
print(result)

# number = int(input())
# max_list = []
# maximum = 0
# for i in range(int(number/2), int(number/4*3)):
#     result = [number, i]
#     j = 0
#     while(True):
#         a = result[j] - result[j+1]
#         if a <= -1:
#             break
#         result.append(a)
#         if maximum < len(result):
#             maximum = len(result)
#             max_list = result[:]
#         j += 1
# print(maximum)
# for k in max_list:
#     print(k, end=' ')
# print()

# first_number2 = int(input())
# result2 = []
# # second_number = int(first_number/2)+int(first_number**0.5)+ int(first_number**0.25)
# for second_number in range(int(first_number2 / 2) + int(first_number2 ** 0.5), int(first_number2 / 4 * 3)):
#     list_list = []
#     list_list.append(first_number2)
#     list_list.append(second_number)
#     first_number = first_number2
#     while first_number > 0:
#         temp = first_number - second_number
#         first_number = second_number
#         if temp < 0:
#             break
#         second_number = temp
#         list_list.append(temp)
#     count = len(list_list)
#
#     result2.append(count)
#     nu = []
#     for i in list_list:
#         nu.append(str(i))
#     result = ' '.join(nu)
# n = result2.index(max(result2))
# second_number = int(first_number2 / 2) + int(first_number2 ** 0.5) + n
# list_list = []
# list_list.append(first_number2)
# list_list.append(second_number)
# while first_number > 0:
#     temp = first_number - second_number
#     first_number = second_number
#     if temp < 0:
#         break
#     second_number = temp
#     list_list.append(temp)
# count = len(list_list)
#
# nu = []
# for i in list_list:
#     nu.append(str(i))
# result = ' '.join(nu)
# print(count)
# print(result)
