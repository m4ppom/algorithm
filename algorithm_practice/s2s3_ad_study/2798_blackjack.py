import sys
sys.stdin = open('blackjack.txt', 'r')


def finding_max(idx):
    global card_sum, M, result, card_number_N, temp
    if card_sum > M:
        return
    if card_sum == M:
        result = M
        return
    if temp < card_sum:
        temp = card_sum
    for i in range(idx, card_number_N):
        card_sum += card_list[i]
        finding_max(i +1)
        card_sum -= card_list[i]


card_number_N, M = map(int, input().split())
card_list = list(map(int, input().split()))
card_list.sort(reverse = True)
maximum_sum = 0
card_sum = 0
result = 0
temp = 0
for i in range(card_number_N):
    finding_max(i)
    if result == M:
        break
    else:
        result = temp
print(result)
