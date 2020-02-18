TC = int(input())
A = int(input())
ans = []
for i in range(TC, 0, -1):
    tmp = A // (10**(i-1))
    ans.append(tmp)
    A = A - tmp*(10**(i-1))
print(sum(ans))
