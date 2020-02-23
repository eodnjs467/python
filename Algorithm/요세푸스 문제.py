# https://www.acmicpc.net/problem/1158

N, K = map(int, input().split())
jose = [i for i in range(1, N+1)]
tmp, result = K-1, []

for i in range(N):
    if len(jose)>tmp:
        result.append(jose.pop(tmp))
        tmp += K-1
    elif len(jose)<=tmp:
        tmp%=len(jose)
        result.append(jose.pop(tmp))
        tmp += K-1

print("<", end='')
for i in result:
    if i==result[-1]:
        print(i, end='')
    else:
        print(i, end=', ')
print(">", end='')