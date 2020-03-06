n = int(input())
mok=n//2
quf, k = 0, 1
print('*'*n)
for i in range(1, n//2):
    print("*"*(mok-quf) + ' '*k + '*'*(mok-quf))
    k += 2
    quf+=1
for i in range(1, n//2+1):
    print('*'*i + ' '*(k) + '*'*i)
    k-=2
print("*"*n)

# ---------------------------------------------------------------------------------------
# 오늘의 느낀점
# 1. 아틀라스네트웍스? 라는 회사야 너넨 정말 예의도 없고 어처구니가 없다. 너네같은 회사 처음 봐 인성이 덜 됐어;;
# 진짜 오늘 화 엄청 나더라 면전에다 대고 뭐라하려다가 참았어 나와서 느낀게 너네같은 예의도 없고 쓰레기같은 좆소기업
# 방향으로는 오줌도 안쌀거야 욕을 엄청 하고싶은데 참을게 내가 후기는 꼭 쓸게 ^^
#
# 2. 긴장하지말고 천천히 짠거 복붙하려 하지말고 그냥 새로해 그게 편하다



for i in range(n):
    for j in range(n):
        print('*', end='')
    print('')



mok=n//2
quf = 0
k = 1
print('*'*n)
for i in range(1, n//2):
    print("*"*(mok-quf) + ' '*k + '*'*(mok-quf))
    k += 2
    quf+=1
for i in range(1, n//2+1):
    print('*'*i + ' '*(k) + '*'*i)
    k-=2
print("*"*n)

for i in range(n):
    for j in range(n):
        print('*', end='')
    print('')