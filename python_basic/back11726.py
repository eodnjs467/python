n = int(input())

nemo = [0] * 1001
nemo[0] = 1
nemo[1] = 1
nemo[2] = 2

for i in range(3, n+1):
    nemo[i] = nemo[i-1] + nemo[i-2]

print(nemo[n] % 10007)