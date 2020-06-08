def solution(progresses, speeds):
    answer = []
    cnt = 0
    len_pro = len(progresses)
    while sum(answer) != len_pro:
        for speed in range(len(speeds)):
            progresses[speed] += speeds[speed]
            if progresses[speed] >= 100:
                progresses[speed] = 0
                speeds[speed] = 0
        for speed in speeds:
            if speed == 0:
                cnt += 1
            else:
                break
        if cnt:
            answer.append(cnt)
        for _ in range(cnt):
            progresses.pop(0)
            speeds.pop(0)
        cnt = 0
    return answer
print(solution([93, 30, 55], [1, 30, 5]))