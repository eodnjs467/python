# https://www.acmicpc.net/problem/9012

TC = int(input())

for _ in range(TC):
    data = list(input())
    cnt = 0
    for i in data:
        if cnt<0:
            break
        elif i=='(':
            cnt+=1
        elif i==')':
            cnt-=1
    if cnt == 0:
        print('YES')
    else:
        print('NO')