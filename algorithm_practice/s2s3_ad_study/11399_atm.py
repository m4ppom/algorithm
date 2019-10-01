import sys
sys.stdin = open('atm.txt', 'r')
import copy
import collections


N = int(input())
time_list = list(map(int, input().split()))
time_list.sort()
summ = 0
for i in range(len(time_list)):
    summ  +=  sum(time_list[:i+1])
print(summ)