N, X = map(int, input().split())
A = list(map(int, input().split()))
ans = [idx for idx in A if X > idx]
for i in ans: print(i, end=' ')