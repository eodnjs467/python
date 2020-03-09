# https://www.acmicpc.net/problem/1978

N = int(input())

num = list(map(int, input().split()))
cnt = 0
for i in num:
    tmp =0
    for j in range(1, i+1):
        if i%j ==0:
            tmp+=1
    if tmp==2:
        cnt+=1
print(cnt)