# def search_text(testing_text, searching_text):
#     test = []
#     search = []
#     for i in testing_text:
#         test.append(i)
#     for i in searching_text:
#         search.append(i)
#     if len(test) == len(search):
#         if test == search:
#             result = 1
#         else:
#             result = 0
#     else:
#         for i in range(len(test)-len(search)+1):
#             if test[i:i+len(search)] == search:
#                 result = 1
#                 break
#             else:
#                 result = 0
#     return result
# test_case = int(input())
# for numbers in range(1, test_case + 1):
#     searching_text = input()
#     testing_text = input()
#     result = search_text(testing_text, searching_text)
#     print('#{} {}'.format(numbers, result))

T = int(input())
for tc in range(1, T+1):
    fir = input()
    sed = input()
    # for_ind = fir[::-1]
    a = len(fir)
    b = 0
    c = 0
    while a-1 < len(sed) and b < len(fir):
        if sed[a-1-b] == fir[-1-b]:
            b += 1
        else:
            if sed[a-1-b] in fir:
                c = fir.index(sed[a-1-b])
                b = 0
                a = a + len(fir) - c - 1
            else:
                a += len(fir)
                b = 0
    if b == len(fir):
        print('#{} 1'.format(tc))
    else:
        print('#{} 0'.format(tc))