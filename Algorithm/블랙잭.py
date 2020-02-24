# https://www.acmicpc.net/problem/2798

N, M = list(map(int, input().split()))

A = list(map(int, input().split()))
result = 0
for i in range(len(A)):
    for j in range(i+1, len(A)):
        for k in range(j+1, len(A)):
            sum = A[i] + A[j] + A[k]
            if sum <= M:
                result = max(result, sum)
print(result)