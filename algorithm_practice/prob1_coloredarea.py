import  sys
sys.stdin = open("inpu.txt", "r")

testcase = int(input())

# tot=[]
for num in range(1, testcase + 1):
    area_info = list(map(int, input().split()))
    cord = [0] * area_info[1]
    space = []
    for area in range(area_info[1]):
        cord[area] = list(map(int, input().split()))

    # print('areainfo', area_info)
    #     print('cord', cord)
        for x in range(cord[area][0]-1, cord[area][2]):  # xy 좌표만큼 돌림 좌표를 영역이라 생각하고
            for y in range(cord[area][1]-1, cord[area][3]):  # set으로 중복제거 수 확인.
                a = str(x)+','+str(y)
                # print(a)
                space += [a]
                # tot +=[a]
                # print(space)
    print(space)
    result = len(set(space))
    print('#{} {}'.format(num, result))
# print(len(set(tot)))