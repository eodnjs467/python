#https://www.acmicpc.net/problem/17413
# 1. <> : 그대로 출력 split 해결법

S, tmp = input(), ""

ck = False          # < 열려있는지 확인

for i in S:
    if i == ' ':
        if not ck:                          # ck가 false면 즉, >뒤에 있다는거
            print(tmp[::-1], end=" ")       #tmp[::-1] 현재 보고있는 단어를 역순으로 해라
            tmp = ""
        else:
            print(" ", end="")
    elif i == '<':
        ck = True
        print(tmp[::-1] + "<", end="")
        tmp = ""
    elif i == '>':
        ck = False
        print(">", end="")
    else:
        if ck:
            print(i, end="")
        else:a
            tmp += i

print(tmp[::-1], end="")