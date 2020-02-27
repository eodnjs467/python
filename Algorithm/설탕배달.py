# https://www.acmicpc.net/problem/2839
# 3으로 나눠서 나머지가 5이면  5로나눠 서 ans +1
# 반대로도 ㅇㅇ 때론 간단하게 풀어쓰자
sugar = int(input())
answer = 0
while sugar>0:
    if sugar%5 != 0:
        sugar -= 3
        if sugar<0:
            answer = -1
            break
        answer+=1
    elif sugar%5 == 0:
        answer += 1
        sugar -= 5
    elif sugar%5!=0 and sugar%3!=0:
        answer = -1
print(answer)

                            #개수 세는 count 함수 사용
A = int(input())
B = int(input())
C = int(input())
tmp = str(A*B*C)

for i in range(0, 10):
    print(tmp.count(str(i)))