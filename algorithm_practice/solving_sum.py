for _ in range(10):
    number = int(input())
    greatest = 0
    sero = [0]*100
    for cross in range(100):
        int_sum = []
        cross1 = cross2 = 0
        summing = 0
        need_sum = input().split()
        for mmm in need_sum:
            int_sum.append(int(mmm))
        cross1 += int_sum[cross]
        cross2 += int_sum[-cross]
        for i in len(int_sum):
            summing += int_sum[i]
            sero[i] += int_sum[i]

        if greatest < summing:
            greatest = summing
    for sssss in sero:
        if greatest < sssss:
            greatest = sssss
    if greatest < cross1:
        greatest = cross1
    elif greatest < cross2:
        greatest = cross2
    else:
        print('#{} {}'.format(number, greatest))