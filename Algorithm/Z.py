#https://www.acmicpc.net/problem/1074

N ,r, c = map(int, input().split())
# Z : 0,0 을 기준으로 x, y의 숫자

def Z(sz, x, y):
    if sz == 1:
        return 0
    sz //=2
    for i in range(2):
        for j in range(2):
            if x < sz * (i+1) and y < sz * (j+1):
                return (i*2+j) * sz*sz + Z(sz, x-sz*i, y-sz*j)  #sz * sz 는 사각형 넓이는 사이즈 *사이즈
    # (0,0), (0,1), (1,0), (1,1) -> i, j 가 1,0 일땐 2 , i, j 가 1, 1 일땐 3
    # 0, 1, 2, 3 -> i*2+j = r

print(Z(2**N, r, c))