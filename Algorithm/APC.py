#https://www.acmicpc.net/problem/17224

# 문제의 개수 N, 역량 L, 최대 해결문제 수 K,
N, L, K = map(int, input().split())

#어려운 문제hard, 쉬운문제 easy
easy , hard = 0, 0

for i in range(N):
    sub1, sub2 = map(int, input().split())
    if sub2<=L:
        hard+=1
    elif sub1<=L:
        easy+=1

#hard 점수계산
ans = min(hard, K)*140      #최대 풀 수 있는문제는 K개 이므로 hard 문제 맞춘게 K를 넘어가면 안됨.

#easy 점수 계산
if hard<K:                          # 최대 풀 수 있는 문제 K 개보다 hard 문제 푼게 적으면 easy문제 푼거 더해야하니까
    ans += min(K-hard, easy)*100    # hard 푼만큼 점수에다가 (K - hard)최대문제 - 어려운문제 or 쉬운문제 푼 개수 중 작은거 골라야함

print(ans)