import sys

money = int(sys.stdin.readline())
money_lst = [50000, 10000, 1000, 500, 100, 50, 10, 1]
tmp = []

for idx, i in enumerate(money_lst):
    tmp.append((str(i)+"원 짜리 : ", idx, money//i))
    money -= (money//i)*i
sys.stdout.write(money)
for i in range(len(tmp)):
    if tmp[i][2] !=0:
        print(tmp[i][0], end='')
        print(tmp[i][2], "개")