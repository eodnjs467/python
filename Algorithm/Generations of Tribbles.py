#https://www.acmicpc.net/problem/9507

def koong(n):
    cache = [1, 1, 2, 4]
    for j in range(4, n+1):
        cache.append(cache[j-1] + cache[j-2] + cache[j-3] + cache[j-4])
    print(cache[n])
    return cache[n]

for i in range(int(input())):
    koong(int(input()))