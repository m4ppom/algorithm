import  sys
sys.stdin = open("input2.txt", "r")

result = 0
testcase = int(input())


def check_sum(x,y,leng):
    hap = 0
    result = 0
    for i in range(x, x+leng):
        if hap > result:
            result = hap
        if i == x or i == x+leng-1:
            for j in range(y, y+leng):
                hap += base[i][j]
                # print('i',i,'j',j,'hap',hap , 'base',base[i][j],'res',result)
                if hap > result:
                    result = hap
        else:
            hap = hap + base[i][y] + base[i][y+leng-1]
            # print('i', i, 'j', y, 'hap', hap,'res',result)
    if hap > result:
        result = hap
    return result


for num in range(1, testcase + 1):
    area_info = list(map(int, input().split()))
    # print(area_info)
    base = [0] * area_info[0]
    for i in range(area_info[0]):
        base[i] = list(map(int, input().split()))
    # print(base)
    # for x in range(0, area_info[1] - area_info[2] + 1):
    rere = 0
    for x in range(0, area_info[0]-area_info[2]+1):
        for y in range(0, area_info[1] - area_info[2] + 1):

        # for y in range(0, area_info[0]-area_info[2]+1):
            result = check_sum(x, y, area_info[2])
            if result > rere:
                rere = result

    print('#{} {}'.format(num, rere))