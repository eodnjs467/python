# https://www.acmicpc.net/problem/10816

# 주어진 카드 -> 딕셔너리
# i in 상근이카드
#  if i in 주어진카드:
#      주어진카드.values()
#      없으면 get(i), '0'

from collections import Counter

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
tmp = Counter(a)

for i in b:
    print(tmp[i], end=' ')