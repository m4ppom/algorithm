import sys
sys.stdin = open('yut.txt', 'r')

'''
가장 처음에는 시작에 말 4개가 있다. 말은 게임판에 적힌 화살표의 방향대로만 이동할 수 있다. 
파란색 칸에서 말이 이동을 시작하는 경우에는 파란색 화살표의 방향으로 이동해야 하며 파란색 칸을 지나가는 경우에는 
빨간 화살표의 방향대로 이동해야 한다.
게임은 1부터 5까지 한 면에 하나씩 적혀있는 5면 주사위를 굴려서 나온 수만큼 이동하는 방식으로 진행한다. 
이동하려고 하는 칸에 말이 이미 있는 경우에는 그 칸으로 이동할 수 없다. 시작과 도착칸은 말이 이미 있어도 이동할 수 있다. 
말이 이동을 마칠때마다 칸에 적혀있는 수가 점수에 추가된다. 
말이 도착으로 이미 이동한 경우에는 더 이상 이동할 수 없고, 말이 이동하려고 하는 칸이 도착을 넘어가는 경우에는 도착에서 이동을 마친다.
주사위에서 나올 수 10개를 미리 알고있을때, 얻을 수 있는 점수의 최댓값을 구해보자.
'''
num_list = list(map(int, input().split()))
print(num_list)
game_pan1 = [2, 4, 6, 8, 10]
game_pan2 = [12, 14, 16, 18, 20]
game_pan3 = [22, 24, 26, 28, 30]
game_pan4 = [32, 34, 36, 38, 40]
game_pan5 = [13, 16, 19, 25]
game_pan6 = [22, 24, 25]
game_pan7 = [28, 27, 26, 25]
game_pan8 = [30, 35, 40]

case = [0]*5
case[1] = game_pan1+ game_pan5 + game_pan8
case[2] = game_pan1+ game_pan2 + game_pan6 + game_pan8
case[3] = game_pan1+ game_pan2 + game_pan3 + game_pan7+ game_pan8
case[4] = game_pan1+ game_pan2 + game_pan3 + game_pan4
leng = [0]*5
leng[1] = len(case[1])
leng[2] = len(case[2])
leng[3] = len(case[3])
leng[4] = len(case[4])

def pathfinder():
    global idx, maxx, lange, summation
    if idx >= lange:
        if maxx < summation:
            maxx = summation
            return
        else:
            return
    else:
        for iii in range(10):
            if visited[iii] == 0:
                visited[iii] = 1
                summation += case[i][num_list[iii]]
                idx += num_list[iii]
                pathfinder()
                idx -= num_list[iii]
                summation -= case[i][num_list[iii]]
                visited[iii] = 0
            else:
                continue


summ = sum(num_list)
maxx = 0
for i in range(1, 5):
    if leng[i] > summ:
        continue
    else:
        lange = leng[i]
        idx = -1
        summation = 0
        visited = [0]* 10
        for ii in range(10):
            visited[ii] = 1
            summation += case[i][num_list[ii]]
            idx += num_list[ii]
            pathfinder()
            idx -= num_list[ii]
            summation -= case[i][num_list[ii]]
            visited[ii] = 0
print(maxx)

