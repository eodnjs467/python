TC = int(input())

for _ in range(TC):
    H, W, N = list(map(int, input().split()))
    if N%H ==0:
        floor = H*100
        ho = N//H
    else:
        floor = (N%H)*100
        ho = N//H +1
    print(floor + ho)