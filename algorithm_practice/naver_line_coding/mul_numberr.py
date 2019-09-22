'''
연속하는 자연수 두 개 이상을 곱해서 만들 수 있는 자연수를 크기 순으로 나열한 수열이 있습니다. 다음은 수열의 예시입니다.

2, 6, 12, 20, 24, 30, 42, 56, 60, 72 ...
예를 들어 2는 두 연속하는 자연수 1과 2를 곱해서 만들 수 있습니다. 마찬가지로 6 = 2 x 3 또는 6 = 1 x 2 x 3이며, 20 = 4 x 5, 60 = 3 x 4 x 5와 같이 연속하는 자연수를 두 개 이상 곱해서 만들 수 있습니다.

자연수 n이 매개변수로 주어질 때, 위 수열에서 n 번째 숫자를 return 하도록 solution 함수를 완성해주세요.

제한사항
n은 1 이상 1,000,000 이하인 자연수입니다.
정답이 1012 이하인 경우만 입력으로 주어집니다.
입출력 예
n	result
1	2
2	6
4	20
9	60
입출력 예 설명
문제에 주어진 수열에 따라 수열의 1,2,4,9 번째 값은 각각 2, 6, 20, 60입니다.
'''
import sys
sys.stdin = open('mul_num.txt', 'r')


def solution(n):
    answer = 0
    new =[]
    def facto(num):
        result = 1
        for i in range(1, n+1):
            result *= i
        return result
    for i in range(2, 16):
        for j in range(1, 14):
            if i <  j+2:
                break
            new.append(facto(i)//facto(j))
    ans = []
    new.sort()
    for i in range(len(new)):
        if new[i] not in ans:
            ans.append(new[i])
        else:
            pass
        if len(ans) > n+2:
            break
        print(ans)
        answer = ans[n-1]
        return answer

