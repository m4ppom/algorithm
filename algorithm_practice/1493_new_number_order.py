import sys
sys.stdin = open('inpu.txt', 'r')


def inserting_number():
    return


testcase = int(input())
for test_num in range(1, testcase+1):
        num1, num2 = map(int, input().split())
        base = [[0 for _ in range(310)]for _ in range(310)]
        count = 1
        cord_info = []
        row = 10001
        # col = 1000000
        # if num1 == 1 and num2 == 1:
        #     print('#{} 5'.format(test_num))
        #     continue
        # else:
        for i in range(1, 300):
            a = i
            b = 1
            while a != 0:
                base[a][b] = count
                a -= 1
                b += 1
                if count == num1: #count == num2:
                    cord_info.append([a, b])
                if count == num2: #count == num2:
                    cord_info.append([a, b])
                if len(cord_info) == 2:
                    row = cord_info[0][0]+1 + cord_info[1][0]+1
                    col = cord_info[0][1]-1 + cord_info[1][1]-1
                count += 1

                # if row < 10000 and i > row:
                #     break
                    # if
                    # if base[row+1][col+1] != 0:
                    #     break
                # if a > row:
                #     break
            # print(base)
        print('#{} {}'.format(test_num, base[row][col]))

# cnt = 1
# summ = 1
# while summ < 10000:
#     summ += cnt
#     cnt += 1
# print(cnt)

