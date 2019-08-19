import sys

sys.stdin = open("input.txt", "r")
for i in range(1, 11):
    test_case = input()
    test_case_list = input().split()
    count = 0

    for j in range(1, len(test_case_list) - 2):
        temp = []
        floor = int(test_case_list[j])
        temp.append(floor - int(test_case_list[j - 1]))
        temp.append(floor - int(test_case_list[j - 2]))
        temp.append(floor - int(test_case_list[j + 1]))
        temp.append(floor - int(test_case_list[j + 2]))
        if min(temp) < 0:
            pass
        else:
            count += min(temp)
    print("#%d %d" % (i, count))
