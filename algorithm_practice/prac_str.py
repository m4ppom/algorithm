# strings = input()
# new = []
# for i in range(len(strings)):
#     new += strings[i]
# print(new)
# newnew = new[0]
# for i in range(1, len(new)):
#     newnew += new[i]
#
# def atoi(str):
#     value = 0
#     for i in range(len(str)):
#         if ord(str[i]) >= ord('0') and ord(str[i]) <= ord('9'):
#             digit = ord(str[i]) -ord('0')
#         else:
#             break
#         value = (value* 10) + digit
#     return value
#
# print(type(strings[0]))
# print(newnew)
testing_text = 'wepifpsdfpaspnkvnpjvx;kcjvpokp[dk[adkmxzkc'
searching_text = 'vnp'

def search_text(testing_text, searching_text):
    idx = 0
    test = []
    search = []
    for i in testing_text:
        test.append(i)
    for i in searching_text:
        search.append(i)
    # test = testing_text.split()
    # search = searching_text.split()
    for i in range(len(test)-len(search)):
        if test[i:i+len(search)] == search:
            idx = i
            break
    return idx

search_text(testing_text, searching_text)
    # for i in range(len(searching_text)):
    #     for j in range(len(testing_text)):
    #         if searching_text[i] == testing_text[j]:
    #             continue
    #         else:
    #             break
