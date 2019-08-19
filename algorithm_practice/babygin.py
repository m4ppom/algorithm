# numbers = input()
# num_list = numbers.split()
# for number in num_list:
#     if num_list.index(number+1):
#         if num_list.index(number+2):
#             num_list.pop(number)
#             num_list.pop(number+1)
#             num_list.pop(number+2)
#             run += 1
#     elif num_list.index(number-1):
#         if num_list.index(number-2):
#             num_list.pop(number)
#             num_list.pop(number-1)
#             num_list.pop(number-2)
#             run += 1
#     elif num_list.count(number) == 3:
#         triplet += 1
#         num_list.pop(number,3)
#         print("jin")
# if run = 1 and triplet = 1:
#     print("boby-jin")
# elif run =2 or triplet =2:
#     print("baby-jin")
# else:
#     print("lose")

num =456789
c = [0]*12

for i in range(6):
    c[num %10] += 1
    num //= 10

i = 0
tri = run = 0
while i < 10:
    if c[i] >= 3 :
        c[i] -= 3
        tri +=1
        continue
    if c[i] >=1 and c[i+1] >=1 and c[i+2] >=1:
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1
        run += 1
        continue
    i += 1
if run + tri == 2:
    print("baby gin")
else:
    print("lose")














