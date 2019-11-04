import sys
sys.stdin = open('qbing.txt', 'r')

import collections
import copy
# stonin_cnt = int(input())
# 3by 3한개만들어놓고 줄별로 바꾸면될
# 숫자 바꾸면서 회전 ㄲ
# + clockwise  - reverse
#  U: 윗 면, D: 아랫 면, F: 앞 면, B: 뒷 면, L: 왼쪽 면, R: 오른쪽 면이다. 두 번째 문자는 돌린 방향이다
# 윗 면은 흰색, 아랫 면은 노란색, 앞 면은 빨간색, 뒷 면은 오렌지색, 왼쪽 면은 초록색, 오른쪽 면은 파란색이다.
def spinn(arrr, wise):  # ok
    temp = [[0,0,0],[0,0,0],[0,0,0]]
    if wise =="+":
        for ii in range(3):
            for jj in range(3):
                temp[jj][2 - ii] = arrr[ii][jj]
    else:
        for ii in range(3):
            for jj in range(3):
                temp[2 - jj][ii] = arrr[ii][jj]
                # 0 0 2 0
                # 0 1 1 0
                # 0 2 0 0
                # 1 0 2 1
                # 1 1 1 1
                # 1 2 0 1
    return

def circulating_L_R(LR, wwise):
    if wwise == "+":
        if LR == "L":
            reverss=[1,5,3]
            ddddddd=[0,1,5]
            temmp = [copy.deepcopy(cube[0][0][0]), copy.deepcopy(cube[0][1][0]), copy.deepcopy(cube[0][2][0])]
            for cucu in range(3):
                cube[ddddddd[cucu]][0][0], cube[ddddddd[cucu]][1][0], cube[ddddddd[cucu]][2][0] = cube[reverss[cucu]][0][0], cube[reverss[cucu]][1][0], cube[reverss[cucu]][2][0]
            cube[3][0][0], cube[3][1][0], cube[3][2][0] = temmp[0], temmp[1], temmp[2]
        elif LR == "R":
            reverss = [1, 5, 3]
            ddddddd = [0, 1, 5]
            temmp = [copy.deepcopy(cube[0][0][2]), copy.deepcopy(cube[0][1][2]), copy.deepcopy(cube[0][2][2])]
            for cucu in range(3):
                cube[ddddddd[cucu]][0][2], cube[ddddddd[cucu]][1][2], cube[ddddddd[cucu]][2][2] = cube[reverss[cucu]][0][2], cube[reverss[cucu]][1][2], cube[reverss[cucu]][2][2]
            cube[1][0][2], cube[1][1][2], cube[1][2][2] = temmp[0], temmp[1], temmp[2]
        elif LR == "F":
            reverss = [4, 5, 2]
            ddddddd = [0, 4, 5]
            temmp = [copy.deepcopy(cube[0][2][0]), copy.deepcopy(cube[0][2][1]), copy.deepcopy(cube[0][2][2])]
            for cucu in range(3):
                cube[ddddddd[cucu]][2][0], cube[ddddddd[cucu]][2][1], cube[ddddddd[cucu]][2][2] = cube[reverss[cucu]][2][0], cube[reverss[cucu]][2][1], cube[reverss[cucu]][2][2]
            cube[2][2][0], cube[2][2][1], cube[2][2][2] = temmp[0], temmp[1], temmp[2]

        elif LR == "B":  # 반대로 끼워봄
            reverss = [2, 5, 4]
            ddddddd = [0, 2, 5]
            temmp = [copy.deepcopy(cube[0][0][0]), copy.deepcopy(cube[0][0][1]), copy.deepcopy(cube[0][0][2])]
            for cucu in range(3):
                cube[ddddddd[cucu]][0][0], cube[ddddddd[cucu]][0][1], cube[ddddddd[cucu]][0][2] = cube[reverss[cucu]][0][0], cube[reverss[cucu]][0][1], cube[reverss[cucu]][0][2]
            cube[4][0][0], cube[4][0][1], cube[4][0][2] = temmp[0], temmp[1], temmp[2]
        # elif LR == "B":
        #     reverss = [4, 5, 2]
        #     ddddddd = [0, 4, 5]
        #
        #     temmp = [copy.deepcopy(cube[0][0][0]), copy.deepcopy(cube[0][0][1]), copy.deepcopy(cube[0][0][2])]
        #     for cucu in range(3):
        #         cube[ddddddd[cucu]][0][0], cube[ddddddd[cucu]][0][1], cube[ddddddd[cucu]][0][2] = cube[reverss[cucu]][0][0], cube[reverss[cucu]][0][1], cube[reverss[cucu]][0][2]
        #     cube[4][0][0], cube[4][0][1], cube[4][0][2] = temmp[0], temmp[1], temmp[2]


    else:
        if LR == "L":  # ok
            reverss=[3,5,1]
            ddddddd=[0,3,5]
            temmp = [copy.deepcopy(cube[0][0][0]), copy.deepcopy(cube[0][1][0]), copy.deepcopy(cube[0][2][0])]
            for cucu in range(3):
                cube[ddddddd[cucu]][0][0], cube[ddddddd[cucu]][1][0], cube[ddddddd[cucu]][2][0] = cube[reverss[cucu]][0][0], cube[reverss[cucu]][1][0], cube[reverss[cucu]][2][0]
            cube[1][0][0], cube[1][1][0], cube[1][2][0] = temmp[0], temmp[1], temmp[2]
        elif LR == "R":
            reverss = [3, 5, 1]
            ddddddd = [0, 3, 5]
            temmp = [copy.deepcopy(cube[0][0][2]), copy.deepcopy(cube[0][1][2]), copy.deepcopy(cube[0][2][2])]
            for cucu in range(3):
                cube[ddddddd[cucu]][0][2], cube[ddddddd[cucu]][1][2], cube[ddddddd[cucu]][2][2] = cube[reverss[cucu]][0][2], cube[reverss[cucu]][1][2], cube[reverss[cucu]][2][2]
            cube[1][0][2], cube[1][1][2], cube[1][2][2] = temmp[0], temmp[1], temmp[2]


        elif LR == "F":  # F -
            reverss = [2, 5, 4]
            ddddddd = [0, 2, 5]
            temmp = [copy.deepcopy(cube[0][2][0]), copy.deepcopy(cube[0][2][1]), copy.deepcopy(cube[0][2][2])]
            cube[0][2][0], cube[0][2][1], cube[0][2][2] = cube[2][0][0], cube[2][1][0], cube[2][2][0]
            cube[2][0][0], cube[2][1][0], cube[2][2][0] = cube[5][2][0], cube[5][2][1], cube[5][2][2]
            cube[5][2][0], cube[5][2][1], cube[5][2][2] = cube[4][2][2], cube[4][1][2], cube[4][0][2]
            cube[4][2][2], cube[4][1][2], cube[4][0][2] =

            # for cucu in range(3):
            #     cube[ddddddd[cucu]][2][0], cube[ddddddd[cucu]][2][1], cube[ddddddd[cucu]][2][2] = cube[reverss[cucu]][2][0], cube[reverss[cucu]][2][1], cube[reverss[cucu]][2][2]
            cube[4][2][0], cube[4][2][1], cube[4][2][2] = temmp[0], temmp[1], temmp[2]
        # elif LR == "B":  # 반대로 끼워봄        #     reverss = [2, 5, 4]
        #     ddddddd = [0, 2, 5]
        #     temmp = [copy.deepcopy(cube[0][2][0]), copy.deepcopy(cube[0][2][1]), copy.deepcopy(cube[0][2][2])]
        #     for cucu in range(3):
        #         cube[ddddddd[cucu]][2][0], cube[ddddddd[cucu]][2][1], cube[ddddddd[cucu]][2][2] = cube[reverss[cucu]][2][0], cube[reverss[cucu]][2][1], cube[reverss[cucu]][2][2]
        #     cube[4][0][0], cube[4][0][1], cube[4][0][2] = temmp[0], temmp[1], temmp[2]
        elif LR == "B":
            reverss = [4, 5, 2]
            ddddddd = [0, 4, 5]
            temmp = [copy.deepcopy(cube[0][0][0]), copy.deepcopy(cube[0][0][1]), copy.deepcopy(cube[0][0][2])]
            for cucu in range(3):
                cube[ddddddd[cucu]][0][0], cube[ddddddd[cucu]][0][1], cube[ddddddd[cucu]][0][2] = cube[reverss[cucu]][0][0], cube[reverss[cucu]][0][1], cube[reverss[cucu]][0][2]
            cube[2][0][0], cube[2][0][1], cube[2][0][2] = temmp[0], temmp[1], temmp[2]


def row_circu(weare, plmi):
    if weare == 'U':
        if plmi == '+':
            temmmmp = copy.deepcopy(cube[3][0])
            cube[3][0] = cube[2][0]
            cube[2][0] = cube[1][0]
            cube[1][0] = cube[4][0]
            cube[4][0] = temmmmp
            return
        else:
            temmmmp = copy.deepcopy(cube[3][0])
            cube[3][0] = cube[4][0]
            cube[4][0] = cube[1][0]
            cube[1][0] = cube[2][0]
            cube[2][0] = temmmmp
            return
    else:  # down
        if plmi == '+':
            temmmmp = copy.deepcopy(cube[3][2])
            cube[3][2] = cube[2][2]
            cube[2][2] = cube[1][2]
            cube[1][2] = cube[4][2]
            cube[4][2] = temmmmp
            return
        else:
            temmmmp = copy.deepcopy(cube[3][2])
            cube[3][2] = cube[4][2]
            cube[4][2] = cube[1][2]
            cube[1][2] = cube[2][2]
            cube[2][2] = temmmmp
            return

def we_are(UD, pm):
    if UD == "U":
        if pm == '+':
            spinn(cube[0], '+')
        else:
            spinn(cube[0], '-')


    return


def cubing(facing, direction):
    if facing == "U":
        if direction == "+":
            spinn(cube[0], '+')
            row_circu("U", "+")
        else:
            spinn(cube[0], '-')
            row_circu("U", "-")
    elif facing == 'D':
        if direction == "+":
            spinn(cube[5], '+')
            row_circu("D", "+")
        else:
            spinn(cube[5], '-')
            row_circu("D", "-")
    elif facing == 'L':
        if direction == '+':
            circulating_L_R('L', '+')
            spinn(cube[4], '+')
        else:
            circulating_L_R('L', '-')
            spinn(cube[4], '-')
    elif facing == 'R':
        if direction == '+':
            circulating_L_R('R', '+')
            spinn(cube[2], '+')
        else:
            circulating_L_R('R', '-')
            spinn(cube[2], '-')
    elif facing == 'F':
        if direction == '+':
            circulating_L_R('F', '+')
            spinn(cube[3], '+')
        else:
            circulating_L_R('F', '-')
            spinn(cube[3], '-')

    elif facing == 'B':
        if direction == '+':
            circulating_L_R('B', '+')
            spinn(cube[1], '+')
        else:
            circulating_L_R('B', '-')
            spinn(cube[1], '-')



def convert():
    print(cube)
    for endendend in range(3):
        for endend in range(3):
            if cube[0][endendend][endend] == 0:
                print('w', end='')
            elif cube[0][endendend][endend] == 1:
                print('o', end='')
            elif cube[0][endendend][endend] == 2:
                print('b', end='')
            elif cube[0][endendend][endend] == 3:
                print('r', end='')
            elif cube[0][endendend][endend] == 4:
                print('g', end='')
            elif cube[0][endendend][endend] == 5:
                print('y', end='')
        else:
            print('')


def stcu():
    cube[1] = [[1,1,1],[1,1,1],[1,1,1]]
    cube[2] = [[2,2,2], [2,2,2], [2,2,2]]
    cube[3] = [[3,3,3],[3,3,3],[3,3,3]]
    cube[4] = [[4,4,4],[4,4,4],[4,4,4]]
    cube[5] = [[5,5,5],[5,5,5],[5,5,5]]
    cube[0] = [[0,0,0],[0,0,0],[0,0,0]]
    return

# L- F+ B +

# w= 0, o=1, b=2, r=3, g= 4, y=5
testcase = int(input())
for testnum in range(testcase):
    num = int(input())
    info = list(map(str , input()))
    cube = [0]*6
    stcu()
    idx = 0
    leng= len(info)
    while idx != leng-1:
        a = info[idx]
        idx += 1
        b = info[idx]
        cubing(a, b)
        idx += 1
        if idx == leng:
            break
        idx += 1
    convert()



