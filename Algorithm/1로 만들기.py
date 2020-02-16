
N, cnt = int(input()), 0

for i in range(N):
    if N != 1:
        if N % 3 == 0:
            N //= 3
            cnt += 1
        elif N % 2 == 0:
            N //= 2
            cnt += 1
        else:
            N -= 1
            cnt += 1
print(cnt)