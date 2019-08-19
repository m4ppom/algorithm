import  sys
sys.stdin = open("inpu.txt", "r")

test_case = int(input())
for numbers in range(1, test_case + 1):
    N, M = map(int, input().split())
    matrix = [[i for i in input().split()] for _ in range(M)]
    if not N % 2:  # 짝수면
        for i in range(M):
            for j in range(int(N/2)):
                if matrix[i][int(N/2)+j] == matrix[i][int(N/2)-j]:
                    if N-j==0:
                        result = matrix[i]
    elif N % 2:  # 홀수면
        for i in range(M):
            for j in range(1,int(N/2)+1):
                if matrix[i][int(N/2)+j] == matrix[i][int(N/2)-j]:
                    if N-j==0:
                        result = matrix[i]
    if not M % 2:  # 짝수면
        for i in range(N):
            for j in range(M/2):
                if matrix[M/2+j][i] == matrix[M/2-j][i]:
                    if M-j==0:
                        result=[]
                        for k in range(M):
                            result += matrix[k][i]

    elif M % 2:  # 홀수면
        for i in range(N):
            for j in range(1,int(M/2)+1):
                if matrix[int(M/2)+j][i] == matrix[int(M/2)-j][i]:
                    if M-j==0:
                        result = []
                        for k in range(M):
                            result += matrix[k][i]

    print('#{} {}'.format(numbers, result))
