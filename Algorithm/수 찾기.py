#https://www.acmicpc.net/problem/1920

N, A = int(input()), {i: 1 for i in map(int, input().split())}
M = input()

for i in list(map(int, input().split())):       # 어떻게 해서 A 딕셔너리의 key 값과 비교가 되는걸까 ...
    print(A.get(i, 0))
    # print(1 if i in A else 0)             #윗 줄(7)과 같은 표현