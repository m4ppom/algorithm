import  sys
sys.stdin = open("inpu.txt", "r")

def counter(list, find):
    result = 0
    for i in range(len(list)):
        if find == list[i]:
            result +=
    return result

test_case = int(input())
for numbers in range(1, test_case + 1):
    find = list(map(str, input()))
    target = list(map(str, input()))
    result = 0
    for i in find:
        temp = counter(target, i)
        if result < temp:
            result = temp
    print('#{} {}'.format(numbers, result))
