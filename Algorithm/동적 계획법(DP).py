# 대표적으로 피보나치

def fibo(num):
    if num <=1:
        return num
    return fibo(num-1) + fibo(num-2)
# 위 재귀함수를 사용하여 피보나치를 구현한 것을 dp 로 구현하면 아래와 같다.

def fibo_dp(num):
    cache = [0 for i in range(num+1)]           # cache 에 저장해놓고 씀
    cache[0] = 0
    cache[1] = 1

    for i in range(2, range(num+1)):
        cache[i] = cache[i-1] + cache[i-2]
    return cache[num]

def fibo_dp2(n):
    cache = [0, 1]

    for i in range(2, n+1):
        cache.append(cache[i-1] + cache[i-2])
    return cache[n]

fibo_dp2(10)