# https://www.acmicpc.net/problem/16956
# i 는 x 값임  j 는 y값  코딩에선 x축과 y축이 반대라고 생각하면 편함
R, C = map(int, input().split())
M = [list(input()) for i in range(R)]

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
ck = False

for i in range(R):
    for j in range(C):
        if M[i][j] == 'W':
            for w in range(4):
                ii, jj = i + dx[w], j + dy[w]
                if ii<0 or ii==R or jj<0 or jj==C:
                    continue
                if M[ii][jj] == 'S':
                    print(0)
                    ck = True
if ck == True:
    print(0)
else:
    print(1)
    for i in range(R):
        for j in range(C):
            if M[i][j] not in 'SW':
                M[i][j] = 'D'
    for i in M:
        print(''.join(i))




# -------------------------------------------------------기존
R, C =map(int, input().split())
M = [list(input()) for i in range(R)]

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

for i in range(R):
    for j in range(C):
        if M[i][j] == 'W':
            for w in range(4):              # 상하좌우
                ii, jj = i+ dx[w], j + dy[w]
                if ii <0 or ii ==R or jj<0 or jj ==C:
                    continue
                if M[ii][jj] == 'S':        #  상하좌우에 양이 있다면
                    ck = True

if ck:
    print(0)
else:
    print(1)
    for i in range(R):
        for j in range(C):
            if M[i][j] not in 'SW':
                M[i][j] = 'D'
    for i in M:
        print(''.join(i))
