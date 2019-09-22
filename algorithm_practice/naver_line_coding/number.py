import sys
sys.stdin = open('number.txt', 'r')


def numbering(leng, numb, row, col):
    if numb == 0:
        for i in range(leng):
            if i == 0 or i == leng -1 :
                for j in range(1,leng+1):
                    plot[i][col + j] = '#'
            else:
                plot[i][col] = '#'
                plot[i][col+leng] = '#'
    elif numb == 1:
        for i in range(row):
                plot[i][col+leng] = '#'
    elif numb == 2:
        for i in range(row):
            if i == 0 or i == row -1 or i == row//2:
                for j in range(1,leng+1):
                    plot[i][col + j] = '#'
            elif i < row//2:
                plot[i][col+leng] = '#'
            else:
                plot[i][col] = '#'
    elif numb == 3:
        for i in range(row):
            if i == 0 or i == row -1 or i == row//2:
                for j in range((row+1)//2):
                    plot[i][col + j] = '#'
            else:
                plot[i][col+leng] = '#'
    elif numb == 4:
        for i in range(row):
            if i < row//2:
                plot[i][col] = '#'
                plot[i][col+leng] = '#'
            elif i == row//2:
                for j in range(1,leng+1):
                    plot[i][col + j] = '#'
            else:
                plot[i][col + (row // 2)] = '#'
    elif numb == 5:
        for i in range(row):
            if i == 0 or i == row //2 or i == row-1:
                for j in range(1,leng+1):
                    plot[i][col + j] = '#'
            elif i < row//2:
                plot[i][col] = '#'
            else:
                plot[i][col+leng] = '#'
    elif numb == 6:
        for i in range(row):
            if i == row // 2 or i == row - 1:
                for j in range(1,leng+1):
                    plot[i][col + j] = '#'
            elif i < row//2:
                plot[i][col] = '#'
            else:
                plot[i][col] = '#'
                plot[i][col+leng] = '#'
    elif numb == 7:
        for i in range(row):
            if i == 0:
                for j in range(1,leng+1):
                    plot[i][col + j] = '#'
            else:
                plot[i][col+leng] = '#'
    elif numb == 8:
        for i in range(row):
            if i == 0 or i == row//2 or i ==row -1:
                for j in range(1,leng+1):
                    plot[i][col + j] = '#'
            else:
                plot[i][col+leng] = '#'
                plot[i][col] = '#'
    elif numb == 9:
        for i in range(row):
            if i == 0 or i == row//2:
                for j in range(1,leng+1):
                    plot[i][col + j] = '#'
            elif i < row//2:
                plot[i][col+leng] = '#'
                plot[i][col] = '#'
            else:
                plot[i][col+leng] = '#'

number, metho = map(str,input().split())
number = int(number)
base = [0]*number
maxi = 0
length = 0
for i in range(number):
    base[i] = list(map(int, input().split()))
    base[i][1] = list(map(int,str(base[i][1])))
    print(base)
    if base[i][0] > maxi:
        maxi = base[i][0]
    length += base[i][0]*len(base[i][1])
    print(length)
print(base, maxi)
# 3이상홀수 +1 //2
plot = [['.']*length for _ in range(maxi*2 -1)]
if metho == 'TOP':


elif metho == 'MIDDLE':


elif metho == 'BOTTOM':
