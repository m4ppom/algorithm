import sys
sys.stdin = open('elec_bus2.txt', 'r')
sys.setrecursionlimit(10000)


def bus_muvin(start, energy):
    global mini, cnt
    if cnt >= mini:
        return
    for i in range(1, energy+1):  # 뒤에서 부터 돌리면 줄일 수 있움
        if start + i > len(base)-1:
            if mini > cnt:
                mini = cnt
            return
        cnt += 1
        bus_muvin(start +i, base[start + i])
        cnt -= 1


testcase = int(input())
for test_num in range(1, testcase + 1):
    base = list(map(int, input().split()))
    start = 1
    cnt = 0
    mini = 99999
    energy = base[start]
    bus_muvin(start, energy)
    print('#%d %d' % (test_num, mini))