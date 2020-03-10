# https://www.acmicpc.net/problem/15829

L = int(input())
word = input()
sum = 0
for i in range(L):
    sum += (ord(word[i])-96)*(31**i)
print(sum % 1234567891)