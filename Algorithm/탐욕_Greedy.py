# 500, 100, 50, 1원으로 N원을 최소한의 동전으로 나타내라

coin_lst = [500, 1, 50, 100]
def coin(N, coin_lst):
    total_coin = 0
    coin_lst.sort(reverse=True)
    for coin in coin_lst:
        total_coin += N//coin
        N -= (N//coin)*coin
    return total_coin

coin(4720, coin_lst)


N = 1000 - int(input())
coin_lst = [500, 100, 50, 10, 5, 1]
def coin(N, coin_lst):
    total_coin = 0
    for coin in coin_lst:
        total_coin += N//coin
        N -= (N//coin)*coin
    return total_coin
coin(N, coin_lst)