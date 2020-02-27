N, M = list(map(int, input().split()))

A = list(map(int, input().split()))
result = 0
for i in range(len(A)):
    for j in range(i+1, len(A)):
        for k in range(j+1, len(A)):
            sum = A[i] + A[j] + A[k]
            if sum <= M:
                result = max(result, sum)
print(result)


import collections
TC = int(input())

for i in range(TC):
    n, m = list(map(int, input().split()))
    queue = list(map(int, input().split()))
    deq = collections.deque([(i, idx) for idx, i in enumerate(queue)])      # 특정 인덱스 번호를 저장하고 궁금할때 enumerate
    cnt = 0                                                                 # idx, i 해놓고 deq에 (i, idx) 한 이유는
    while True:                                                             # 밑에 람다 함수에서 i값을 비교해야 하므로
        if deq[0][0] == max(deq, key=lambda x: x[0])[0]:                    # 위에 (i, idx) 에서 괄호 이유는
            cnt += 1                                                          # deq[0]에 (i, idx) 두개가 하나로 들어가야해서
            if deq[0][1] == m:                                              # 근데 max(deq, key=lambda x: x[0])[0] 이거말고
                print(cnt)                                                  # deq[0]max(deq, key=lambda x: x[0])
                break                                                       # 이건 안되나?
            else:
                deq.popleft()
        else:
            deq.rotate(-1)


# 맥스 값이랑 [0][0] == 같으면 카운트 +1  하고 빼줄건데 그전에 카운트 +1 후 만약 값이 찾는 값이라면 카운트 출력
# 아닌경우 그냥 빼버려 ㅇㅇ 같지도 않으면 걍 돌려
# 조건문의 경우 참 거짓 경우 미리 적어놓고 그 안에 조건이 또 필요하면 그 후에 적자

# 1 2 3 4 5 6 7 //3 6 2

N, K = list(map(int, input().split()))
yosepus, ans = [], []
tmp = 0
for i in range(1, len(N+1)):
    yosepus.append(i)
N = yosepus
for i in range(1, len(N)):
    if K * i > len(N) :
        tmp = (i*K)%K
    else:
        tmp = K*i-1
    if len(yosepus) != 1:
        ans.append()
        print(ans)
    if len(yosepus) ==1:
        ans.append(yosepus[0])
        print(ans)
        break
ans




N, K = map(int, input().split())
yosepus = [i for i in range(1, N+1)]
ans = []
tmp = K-1
for i in range(N):
    if len(yosepus) > tmp:
        ans.append(yosepus.pop(tmp))
        tmp += K-1
    elif len(yosepus) < tmp:
        tmp %= len(yosepus)
        ans.append(yosepus.pop(tmp))
        tmp += K-1
print(ans)




















N, K = map(int, input().split())
jose = list(range(1, N+1))
ans = []
tmp = K - 1
while True:
    ans.append(jose.pop(tmp))
    if not jose:
        break
    tmp = (tmp+K-1)%len(jose)

print('<'+', '.join(map(str, ans)) + '>')















a = [23, 4, 5]
a.index(23)



def solution(heights):
    answer = [0]*len(heights)
    while heights:
        right = heights.pop()
        for i in range(len(heights)-1, -1, -1):
            if right<heights[i]:
                answer[len(heights)] = i+1
    return answer
solution([6, 9, 5, 7, 4])


def solution(bridge_length, weight, truck_weights):
    answer = 0
    dari = []
    for i in truck_weights:
        q_truck = i
        while q_truck:
            if len(dari) == bridge_length:
                dari.pop(0)
            if sum(dari)+q_truck <= weight:
                dari.append(q_truck)
                answer += 1
                q_truck=0
            else:
                answer +=1
                dari.append(0)
    answer += bridge_length
    return answer

solution(100, 100, [10])




def solution(progresses, speeds):
    answer = []
    while progresses:
        ck = False
        tmp = 0
        for i in range(progresses):
            progresses[i] += speeds[i]
        while len(progresses)!=0 and progresses[0]>=100:
            ck = True
            progresses.pop(0)
            speeds.pop(0)
            tmp += 1
        if ck == True:
            answer.append(tmp)
    return answer









N = int(input())
word_lst = []
for i in range(N):
    word = input()
    word_cnt = len(word)
    word_lst.append((word, word_cnt))
word_lst = sorted(set(word_lst), key=lambda word: (word[1], word[0]))
for word in word_lst:
    print(word[0])







N, M = list(map(int, input().split()))
cards = list(map(int, input().split()))
result = 0
for i in range(len(cards)):
    for j in range(i+1, len(cards)):
        for k in range(j+1, len(cards)):
            sum = cards[i]+cards[j]+cards[k]
            if sum<=M:
                result = max(result, sum)
print(result)


