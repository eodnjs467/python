#https://www.acmicpc.net/problem/2484

def money():
    lst = sorted(list(map(int, input().split())))
    if len(set(lst)) == 1:  # 모두 같은 경우
        return 50000 + lst[0] * 5000
    if len(set(lst)) == 2:
        if lst[1] == lst[2]:
            return 10000 + lst[1] * 1000            #3개 같은 경우
        else:
            return 2000 + lst[1]*500 + lst[2]*500   #2개 2쌍
    for i in range(3):
        if lst[i] == lst[i+1]:                      #2개 같은 경우
            return 1000 + lst[i] * 100
    if len(set(lst)) == 4:                          # 모두 다른경우
        return lst[-1] * 100

N = int(input())

print(max(money() for i in range(N)))