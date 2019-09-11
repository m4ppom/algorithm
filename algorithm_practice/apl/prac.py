import random

# a = random.choice()
# lst =[]
# while len(lst) != 1000000:
#     a = random.choice()
#     lst.append(a)
# b = sorted(lst)
# print(b)

# def bit(i):
#     output = ''
#     for j in range(7, -1, -1):
#         if i & (1 << j):
#             output += '1'
#         else:
#             output += '0'
#     print(output)
#
#
# for i in range(-7, 6):
#     print('%3d ='%i, end='')
#     bit(i)


# def viy(i):
#     if i & (1 << j):
#

# a='0000000111100000011000000111100110000110000111100111100111111001100111'
# # lst=list(map(int, input()))
# temp = []
# lst=list(map(int, a))
# while len(lst) != 0:
#     summ = 0
#     for _ in range(7):
#         temp.append(lst.pop(0))
#     for j in range(0, 7, 1):
#         if temp[j] == 1: #  & (1 >> j):
#             summ += 2**(7-j)
#     temp = []
#     print(summ)

# n = 0x00111111
# if n & 0xff:
#     print('little endian')
# else:
#     print('big end')
#
#
def vivit(i):
    output = ''
    for j in range(7, -1, -1):
        if i & (1 << j):
            output += '1'
        else:
            output += '0'
    print(output, end='')
#
# a = 0x10
# x = 0x01020304
# print('%d = ' % a, end='')
# vivit(a)
# print()
# print('0%X =' % x, end='')
# for i in range(0, 4):
#     vivit((x >> i*8) & 0xff)


a= 0x86
key = 0xAA
print('a ==>', end='')
vivit(a)
print()
print('a^key ==>', end='')
a ^= key
vivit(a)
print()
print('a^key ==>', end='')
a ^= key
vivit(a)
print('a' + 'b')
# a = [0, F, 9, 7, A, 3]
# for i in a:
#     if type(i) != int:
#         i = '0x' + i
#         i = int(i)
#         print(bin(i))
#         print()
#     else:
#         print(bin(i))
#         print()


# num = ord(ch) - ord('A')+10
hexa_dict = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F': 15}
def making_binary(num):
    if num in hexa_dict:
        num = hexa_dict[num]
    lst = [0]*4
    # while num // 2 != 0:
    for i in range(3,-1,-1):
        lst[i] = num % 2
        num //= 2
    lll.extend(lst)
    # print(lst)
        # break


def printind_decimal(lst):
    a = []
    while len(lst):
        a.append(lst.pop(0))
        # print(a)
        if len(a) == 7:
            summ = 0
            for i in range(6, -1, -1):
                summ += a[i] * 2 ** (7 - i-1)
            print(summ)
            sum_lst.append(summ)
            a = []
    if a:
        summ = 0
        for b in range(len(a)-1, -1, -1):
            summ += a[b] * 2 ** (len(a)-b-1)
        print(summ)
        sum_lst.append(summ)


a = [0, 'F', 9, 7, 'A', 3]
lll = []
sum_lst = []
for i in a:
    making_binary(i)
printind_decimal(lll)
# print(lll)
print(sum_lst)
for i in range(len(sum_lst)):
    print('%d' % sum_lst[i], end ='')
    if i != len(sum_lst)-1:
        print(', ', end='')
print()


def in_pattern(lst):
    a = 0
    new = []
    while a != 1:
        a = lst.pop(-1)
    for i in range(6):
        new.append(lst[-(6-i)])
    new.append(a)
    if new in pattern:
        print(new)
    else:
        new.pop(-1)
        new.append()
pattern = [[0,0,1,1,0,1],[0,1,0,0,1,1],[1,1,1,0,1,1],[1,1,0,0,0,1],[1,0,0,0,1,1],[1,1,0,1,1,1],[0,0,1,0,1,1],[1,1,1,1,0,1],[0,1,1,0,0,1],[1,0,1,1,1,1]]
a = [0, 'D', 'E', 'C']
for i in a:
    making_binary(i)
print(lll)
in_pattern(lll)