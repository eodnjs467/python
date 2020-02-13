N = int(input())

for i in range(N):
    print(' '*(i) + '*'*(N-i) + '*'*(N-i-1))
for i in range(N-1):
    print(' '*(N-i-2)+'*'*(i+2) + '*'*(i+1))
    # print(' '*(N-i-1) + '*'*i)
    # print(' '*i + '*'*(N-i) + '*'*(N-1-i))
    # print(' '*(N-1-i) + '*'*(i+1) + '*'*i)