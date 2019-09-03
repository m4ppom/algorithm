import sys
sys.stdin = open('inpu.txt', 'r')



# # def earning_money(k, sum):
# #     global cnt
# #     cnt += 1
# #     if k == N:
# #         if sum == 10:
# #             for i in range(1, 11):
# #                 if a[i] == True:
# #             #         print(i, end=' ')
# #             # print()
# #     else:
# #         k += 1
# #         # if sum + k <= 10 :
# #         #     a[k] = 1; backtrack(k, sum + k)  # 가지치기
# #         a[k] = 1; backtrack(k, sum + k)
# #         a[k] = 0; backtrack(k, sum)


# # def comb_i():
# #     for i in range(N - 1):
# #         for j in range(i + 1, N):
# #             print(a[i], a[j])


# # def comb_r(k, s):
# #     if k == R: 
# #         print(t[0], t[1])
# #     else:
# #         for i in range(s, N + (k - R) + 1):
# #             t[k] = a[i]
# #             comb_r(k + 1, i + 1)

# def solve(day, profit):
#     global ans
#     if day == n+1:
#         if ans < profit:
#             ans = profit
#         return
#     if day > n+1:
#         return
#     solve(day+t[day], profit+p[day])
#     solve(day+1, profit)


# testcase = int(input())
# for test_num in range(1, testcase + 1):
#     ans = 0
#     n = int(input())
#     t, p = [0]*(n+1), [0]*(n+1)
#     for i in range(1, n+1):
#         t[i], p[i] = map(int, input().split())

#     solve(1, 0)
#     print(ans)
    # N = int(input())
    # lst = [0 for _ in range(N)]
    # for i in range(N):
    #     lst[i] = list(map(int, input().split()))
    # cnt = 0
    # earring = []
    # while cnt != N:
    #     cnt += 1
    #     money = 0
    #     cnt2 = cnt
    #     while cnt2 != N:
    #         for i in range(cnt, N):
    #             if cnt + i > N-1:
    #                 cnt2 += 1 
    #                 break
    #             else:
    #                 money += lst[i][1]
def solve(day, profit):
    global ans
    global n
    if day == n+1:
        if ans < profit:
            ans = profit
        return
    if day > n+1:
        return
    solve(day+t[day], profit+p[day])
    solve(day+1, profit)


ans = 0
n = int(input())
t, p = [0]*(n+1), [0]*(n+1)
for i in range(1, n+1):
    t[i], p[i] = map(int, input().split())
solve(1, 0)
print(ans)

