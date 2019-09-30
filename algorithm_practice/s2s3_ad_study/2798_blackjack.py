import sys
sys.stdin = open('blackjack.txt', 'r')


def finding_max(idx):
    global card_sum, M, result, card_number_N, temp, cnt
    if card_sum > M or cnt > 3:
        return
    if card_sum == M and cnt == 3:
        result = M
        return
    if temp < card_sum and cnt == 3:
        temp = card_sum
        return
    for i in range(idx, card_number_N):
        card_sum += card_list[i]
        cnt += 1
        finding_max(i +1)
        cnt -= 1
        card_sum -= card_list[i]


card_number_N, M = map(int, input().split())
card_list = list(map(int, input().split()))
card_list.sort(reverse = True)
maximum_sum = 0
card_sum = 0
result = 0
temp = 0
cnt = 0
for i in range(card_number_N):
    finding_max(i)
    if result == M:
        break
    else:
        result = temp
print(result)
