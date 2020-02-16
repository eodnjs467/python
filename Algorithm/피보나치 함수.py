# https://www.acmicpc.net/problem/1003


def fibonacci(n):
    if len(cnt_0) <= n :
        for i in range(len(cnt_0), n+1):
            cnt_0.append(cnt_0[i-1] + cnt_0[i-2])
            cnt_1.append(cnt_1[i-1] + cnt_1[i-2])
    print(cnt_0[n], cnt_1[n])
    print(cnt_0[n], end=' ')
    print(cnt_1[n])s
    # print(cnt_0[n] + cnt_1[n], end=' ')
    # print('{} {}'.format(cnt_0[n], cnt_1[n]))

TC = int(input())
cnt_0, cnt_1 = [1, 0, 1], [0, 1, 1]

for i in range(TC):
    fibonacci(int(input()))
