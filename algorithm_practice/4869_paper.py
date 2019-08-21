import  sys
sys.stdin = open("inpu.txt", "r")

testcase = int(input())

for num in range(testcase):
    mux = 0
    count= 0
    garo = int(input())
    sq = garo//20
    sq_2 = garo % 20
    if sq_2:
        mux += 1
    count += sq +1
    (sq + 1)




    print('#{} {}'.format(num, ))