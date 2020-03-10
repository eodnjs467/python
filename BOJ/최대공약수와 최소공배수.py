# https://www.acmicpc.net/problem/2609

def gcd(a, b):
    if b==0: return a
    else: return gcd(b, a%b)

def lcm(a, b):
    g = gcd(a, b)
    return g * (a//g) * (b//g)

a, b = map(int, input().split())
print(gcd(a, b))
print(lcm(a, b))