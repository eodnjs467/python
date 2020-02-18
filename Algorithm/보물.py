# https://www.acmicpc.net/problem/1026

TC = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A, reverse=True)
B = sorted(B)
sum = 0

for i in range(TC):
    sum += A[i] * B[i]
print(sum)
