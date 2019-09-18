import sys
sys.stdin = open('contain.txt', 'r')


testcase = int(input())
for test_num in range(1, testcase+1):
    contain_number, bus_number = map(int, input().split())
    mass = list(map(int, input().split()))
    force = list(map(int, input().split()))
    mass = sorted(mass)
    mass = mass[::-1]
    force = sorted(force)
    force = force[::-1]
    point = False
    result = 0
    if len(force) <= len(mass):
        for i in range(len(force)):
            gap = 1000
            for j in range(len(mass)):
                if -1 < force[i] - mass[j] <= gap:
                    point = (mass[j], j)
                    gap = force[i] - mass[j]
            if point:
                # print(mass)
                result += point[0]
                mass.pop(point[1])
                point = False
        print('#%d %d'%(test_num, result))
    else:
        for i in range(len(mass)):
            gap = 1000
            for j in range(len(force)):
                if -1 < force[j] - mass[i] <= gap:
                    point = (mass[i], j)
                    gap = force[j] - mass[i]
            if point:
                # print(mass)
                result += point[0]
                force.pop(point[1])
                point = False
        print('#%d %d'%(test_num, result))
