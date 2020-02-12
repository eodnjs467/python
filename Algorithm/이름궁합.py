#https://www.acmicpc.net/problem/17269

N, M = map(int, input().split())

A, B = input().split()

alp = [3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,2,2,2,1,2,1,1,1,2,2,1]

AB = ''
min_len = min(N, M)

for i in range(min_len):
    AB +=A[i] + B[i]

AB += A[min_len:]+B[min_len:]   #   min_len 이 7 이면 7부터 끝까지

lst = [alp[ord(i)-ord('A')] for i in AB]
#
# def f(lst):
#     ret = []
#     for i in range(lst-1):
#         ret.append((lst[i] + lst[i+1])%10)
#     return ret    밑에 대신 이런식의 함수로 해도 됨

for i in range(N+M-2):      #  A + B 에서 맨 마지막에 2 개 남겨야하니까 -2
    for j in range(N+M-1-i): #  i가 처음에 0이고, 수행할때마다 1개씩 줄어야하니까 -1
        lst[j] += lst[j+1]

print("{}%".format(lst[0] % 10*10 + lst[1] % 10))   # lst[0] = 2, lst[1] = 7  이 되는데
                                                    # 20+7 이 되어야하니까 lst[0]을% 10 하고
                                                    # 곱하기 10 해줘서 20 맞춘거 십의 자리로 ㅇㅇ
                                                    # % 붙어야하니까 {} 뒤에 % 해줌
                                                    # format(a) -> a값이 {}에 들어감