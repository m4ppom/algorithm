import sys
sys.stdin = open('sutja.txt', 'r')


def calculator():
    return


def sequence(temp):
    global randidx, N, maxx, minn
    if randidx == N-1:
        # print(maxx, minn)
        if maxx < temp:
            maxx = temp
        if minn > temp:
            minn = temp
        return
    for coco in range(4):
        if opcode[coco] == 0:
            continue
        else:
            if coco == 0:
                opcode[coco] -= 1
                temp += operand[randidx+1]
                randidx += 1
                sequence(temp)
                randidx -= 1
                temp -= operand[randidx+1]
                opcode[coco] += 1

            elif coco == 1:
                opcode[coco] -= 1
                temp -= operand[randidx + 1]
                randidx += 1
                sequence(temp)
                randidx -= 1
                temp += operand[randidx + 1]
                opcode[coco] += 1

            elif coco == 2:
                opcode[coco] -= 1
                beforebefore.append(temp)
                temp *= operand[randidx + 1]
                randidx += 1
                sequence(temp)
                randidx -= 1
                temp = beforebefore.pop()
                # temp //= operand[randidx + 1]
                opcode[coco] += 1

            elif coco == 3:
                opcode[coco] -= 1
                before.append(temp)
                # temp = ((-1) * temp) // operand[randidx + 1]
                if temp < 0:
                    temp = ((-1)*temp) // operand[randidx + 1]
                    temp = (-1)*temp
                else:
                    temp = temp // operand[randidx + 1]
                randidx += 1
                sequence(temp)
                randidx -= 1
                temp = before.pop()
                opcode[coco] += 1




testnum = int(input())
# 1 +,    2 -,     3 *,    4 /
for testcase in range(1, testnum+1):
    N = int(input())
    opcode = list(map(int, input().split()))
    operand = list(map(int, input().split()))
    randidx = 0
    before = []
    beforebefore = []
    maxx = -99999999
    minn = 9999999
    sequence(operand[randidx])
    # print(maxx, '         |||||           ', minn)
    # if testcase == 1:
    #     maxx += 1
    print('#%d %d' %(testcase, maxx - minn))