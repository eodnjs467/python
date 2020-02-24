# https://programmers.co.kr/learn/courses/30/lessons/42583
def solution(bridge_length, weight, truck_weights):
    answer = 0
    dari = []
    for i in truck_weights:
        q_truck = i
        while q_truck:
            if len(dari) == bridge_length:
                dari.pop()
            if (sum(dari) + q_truck) <= weight:
                dari.insert(0, q_truck)             #insert(a,b) a 위치에 b를 입력한다.
                q_truck = 0
                answer +=1
            else:
                dari.insert(0, 0)
                answer += 1
    answer += bridge_length
    return answer

a, b, c = int(input()), int(input()), list(map(int, input().split()))

solution(a, b, c)