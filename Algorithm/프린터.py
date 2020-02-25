# https://programmers.co.kr/learn/courses/30/lessons/42587?language=python3

import collections


def solution2(priorities, location):
    ans = 0
    deq = collections.deque(priorities)
    tmp = []
    while deq:

        for idx in deq:
            if deq[0] < idx:
                deq.rotate(-1)
            else:
                ans += 1
                tmp.append(0)
                break
    if tmp[location] == 0:
        return ans
    return ans








def solution(priorities, location):
    answer, c = 0, 0
    tmp = sorted(priorities, reverse=True)          #[ 3, 2,2,1 ]
    while True:
        for i , priority in enumerate(priorities):
            s = tmp[c]
            if priority == s:
                c+=1
                answer+=1
                if i == location:
                    print(answer)
                    break
        else:
            continue
        break
    return answer

for i in range(int(input())):
    num, location = list(map(int, input().split()))
    priorities = list(map(int, input().split()))
    solution(priorities, location)