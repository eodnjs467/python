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


import collections

def printer_q(deq, m):
    cnt = 0
    while True:
        if deq[0][0] == max(deq, key=lambda x: x[0])[0]:
            cnt += 1
            if deq[0][1] == m:
                print(cnt)
                break
            else:
                deq.popleft()
        else:
            deq.rotate(-1)


TC = int(input())

for i in range(TC):
    n, m = list(map(int, input().split()))
    queue = list(map(int, input().split()))
    deq = collections.deque([(i, idx) for idx, i in enumerate(queue)])
    printer_q(deq, m)
