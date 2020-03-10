# https://www.acmicpc.net/problem/1018

n, m = map(int, input().split())
board = [list(map(str, list(input()))) for _ in range(n)]
BW = [[0 for _ in range(m)] for _ in range(n)]
WB = [[0 for _ in range(m)] for _ in range(n)]

#BW TEST
for i in range(n):
    for j in range(m):
        if(i+j)%2==0:
            if board[i][j] == 'B':      # BW 로 채웠을때 바꿔야하는 경우
                pass
            else:
                BW[i][j] += 1
        else:
            if board[i][j] == 'W':      # WB 로 패웠을때 바꿔야하는 경우
                pass
            else:
                BW[i][j] += 1
# WB TEST
for i in range(n):
    for j in range(m):
        if (i+j)%2==0:
            if board[i][j] == 'W':
                pass
            else:
                WB[i][j] +=1
        else:
            if board[i][j] == 'B':
                pass
            else:
                WB[i][j] +=1

min_num = 64
# BW 최소
for i in range(7, n):
    for j in range(7, m):
        sum_num = 0
        for p in range(8):
            for q in range(8):
                if BW[i-p][j-q]:
                    sum_num+=1
        if sum_num <= min_num:
            min_num = sum_num
        # ans = min(sum_num, min_num)

# WB 최소
for i in range(7, n):
    for j in range(7, m):
        sum_num = 0
        for p in range(8):
            for q in range(8):
                if WB[i-p][j-q]:
                    sum_num += 1
        # ans = min(sum_num, min_num)
        if sum_num <= min_num:
            min_num = sum_num
print(min_num)
type(min_num)