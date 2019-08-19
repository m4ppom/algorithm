# 04131241
# A = input()
def Counting_sort(A, B, k):
    for i in range(len(B)):
        C[A[i]] += 1

    for i in range(1, len(C)):
        C[i] += C[i - 1]

    for i in range(len(B) - 1, 0, -1):
        B[C[A[i]] - 1] = A[i]
        C[A[i]] -= 1
    return B

# def Counting_sort(A, B, k):
    A = [0, 4, 1, 3, 1, 2, 4, 1]
    B = [0] * len(A)
    C = [0] * len(set(A))
Counting_sort(A, B, C)