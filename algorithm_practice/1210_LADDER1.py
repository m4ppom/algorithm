import  sys
sys.stdin = open("inpu.txt", "r")

testcase = 10
for test in range(1,testcase+1):
    dddddd = input()
    base = []
    for _ in range(100):
        base.append(list(map(int, input().split())))
    for j in range(100):
        y = 99
        i = j
        if base[y][i] == 2:
            # print(i)
            while y != 0:
                y -= 1
                # print(y, i)
                #if i + 1 > 99 or i - 1 < -2:
                if i == 99:
                    while i - 1 > -1 and base[y][i - 1] == 1:
                        i -= 1
                elif i + 1 > 99 or i - 1 < -2:
                    continue
                elif base[y][i+1] == 1:
                    while i+1 < 100 and base[y][i+1] == 1:
                        i += 1

                elif base[y][i - 1] == 1:
                    while i - 1 > -1 and base[y][i - 1] == 1:
                        i -= 1
            result = i
            # while
    print('#{} {}'.format(test, result))

