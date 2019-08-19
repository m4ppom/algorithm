lines = int(input())
for i in range(1,lines+1):
    options = input().split()
    recharger_list = input().split()
    n = int(options[1])
    charge = 0
    stop = 0 
    k = int(options[0])
    road = [0] * (int(options[1])+k)
    point = 0
    for j in recharger_list:
        road[int(j)] = 1
    while point < n and stop ==0:
        for move in range(k,-1,-1):
            if point+move == n:
                point += move
                break
            elif move == 0 or point == n:
                stop = 1
                charge = 0
            elif road[point + move] != 0:
                point += move
                charge += 1
                break

    print('#{} {}'.format(i, charge))