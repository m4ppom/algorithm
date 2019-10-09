import sys
sys.stdin = open('colorpap.txt', 'r')


N = int(input())
base = [[i for i in list(map(int, input().split()))]for i in range(N)]
print(base)