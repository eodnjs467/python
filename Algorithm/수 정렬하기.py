#https://www.acmicpc.net/problem/2750
#왜 파이썬3으로는 시간초과 나오고, pypy3는 맞다고 나옴 ?

num = []

for i in range(int(input())):
    num.append(int(input()))

for i in sorted(num):
    print(i)