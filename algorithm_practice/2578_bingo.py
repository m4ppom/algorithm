import  sys
sys.stdin = open("inpu.txt", "r")


def change_bingo(no, bingo):
    for i in range(5):
        for j in range(5):
            if no == bingo[i][j]:
                bingo[i][j] = 0
                break
def find_bingo(bingo):
    print('aaa')
    for i in range(5):
        j = 0
        if bingo[i][j] == 0:
            for mm in range(1,5):
                if bingo[i][mm] == 0:
                    pass
                else:
                    break
            return 1
        if bingo[0][0] == 0:
            for mm in range(1, 5):
                if bingo[mm][mm] == 0:
                    pass
                else:
                    break
            return  1
        if bingo[j][i] == 0:
            for mm in range(1,5):
                if bingo[mm][i] ==0:
                    pass
                else:
                    break
            return 1
        if bingo[0][4] == 0:
            for mm in range(5):
                if bingo[mm][4-mm] == 0:
                    pass
                else:
                    break
            return 1


bingo = [0]*5
ans = [0]*5
for i in range(5):
    bingo[i] = list(map(int, input().split()))
for i in range(5):
    ans[i] = list(map(int, input().split()))
print(bingo)
bg = 0
sount = 0
count = 0
while sount != 3:
    for i in range(len(ans)):
        for j in range(len(ans[i])):
            change_bingo(ans[i][j],bingo)
    print(bingo)
    sount += find_bingo(bingo)
    count += 1
    print(count)
print(count)