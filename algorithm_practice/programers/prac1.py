# 정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수,
# solution을 완성해주세요. 단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요.
# 예를들어 arr이 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고,
# [10]면 [-1]을 리턴 합니다.


def solution(arr):
    a = min(arr)
    b = arr.index(a)
    arr.pop(b)
    # answer = []
    answer = arr
    if answer == []:
        answer = [ -1 ]
    return answer

# 수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
# 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때,
# 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.
import collections

def solution(participant, completion):

    return list((collections.Counter(participant)-collections.Counter(completion)).keys())[0]

    # answer = ''
    # visited = [0]*len(participant)
    # a = len(completion)
    # for i in range(a):
    #     for j in range(len(participant)-1, -1, -1):
    #         if completion[i] == participant[j] and visited[j] == 0:
    #             visited[j] = 1
    #             # participant.pop(j)
    #             # answer = aaa
    #             break
    #         else:
    #             pass
    # aa = visited.index(0)
    # answer = participant[aa]
    # for i in participant:
    #     if i in completion:
    #         completion.pop(completion.index(i))
    #     else:
    #         answer = i
    #         break
    #
    # return answer

