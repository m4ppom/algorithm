import sys
sys.stdin = open('pool.txt', 'r')


def costfinder():
    global total_cost, maxi_cost
    if total_cost > maxi_cost or total_cost >= cost[3]:
        return


def dfs(wichi):
    global maxi_cost, total_cost
    if total_cost >= cost[3]:
        return
    if wichi >= 12:
        if maxi_cost > total_cost:
            maxi_cost = total_cost
        return
    if month[wichi] == 0:
        dfs(wichi+1)
    for i in range(3):
        if i == 0:
            total_cost += cost[0] * month[wichi]
            dfs(wichi+1)
            total_cost -= cost[0] * month[wichi]
        elif i == 1:
            total_cost += cost[1]
            dfs(wichi + 1)
            total_cost -= cost[1]
        elif i == 2:
            total_cost += cost[2]
            dfs(wichi + 3)
            total_cost -= cost[2]


testcase = int(input())
for test_num in range(1, testcase+1):
    cost = list(map(int, input().split()))
    month = list(map(int, input().split()))
    maxi_cost = 100000
    total_cost = 0
    dfs(0)
    if maxi_cost > cost[3]:
        maxi_cost = cost[3]
    print('#%d %d' %(test_num, maxi_cost))