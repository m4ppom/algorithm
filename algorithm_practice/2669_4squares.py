num_list = []
for i in range(4):
    square = input().split()
    # ''.join(square[1] + square[2])
    # a =  int(''.join(square[1]))
    # b =  int(''.join(square[2]))
    # c = int(''.join(square[3]))
    # d = int(''.join(square[4]))
    a = int(square[0])
    b = int(square[1])
    c = int(square[2])
    d = int(square[3])
    for j in range(a, c, 1):
        for k in range(b, d , 1):
            num_list.append([j,k])
print(num_list)
# 1 2 4 4
# 2 3 5 7
# 3 1 6 5
# 7 3 8 6