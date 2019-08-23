import  sys
sys.stdin = open("inpu.txt", "r")

testcase = int(input())

# tot=[]
for num in range(1, testcase + 1):
    aaaa = [[0 for _ in range(100)] for _ in range(100)]
    area_info = list(map(int, input().split()))
    cord = [0] * (2*area_info[1])
    space = []
    cnt = 0
    for area in range(area_info[1]):
        a = list(map(int, input().split()))
        # print(a)
        cord[cnt] = a[0:2]
        cord[cnt + 1] = a[2:]
        cnt += 2
    # print(cord)


    while len(cord) != 0:
        a = cord.pop()
        # print(a)
        b = cord.pop()
        # print(b)
        # print(type(a[0]))
        for i in range(b[0], a[0]+1):
            for j in range(b[1], a[1]+1):
                aaaa[i][j] = 1
                # print('jjj',i,j)
    count = 0
    for i in range(100):
        for j in range(100):
            if aaaa[i][j] != 0:
                count += 1
    print(count)
    #
    # # print('areainfo', area_info)
    # #     print('cord', cord)
    #     for x in range(cord[area][0]-1, cord[area][2]):  # xy 좌표만큼 돌림, 좌표를 영역이라 생각하고
    #         for y in range(cord[area][1]-1, cord[area][3]):  # set으로 중복제거 수 확인.
    #             a = str(x)+str(y)
    #             # print(a)
    #             space += [a]
