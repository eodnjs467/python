def solution(n, lost, reserve):
    answer = 0
    # tmp = len(reserve)
    cnt = 0
    if lost not in reserve:
        for i in range(len(reserve)):
            for j in range(len(lost)):
                if reserve[i]+1 == lost[j] or reserve[i]-1 == lost[j]:
                    cnt += 1
                    lost[j] = 0
                    reserve[i] = 0
        answer = n+cnt-len(lost)
    elif lost in reserve:
        lost.pop(lost.index(lost in reserve))
        reserve.pop(reserve.index(lost in reserve))
        for i in range(reserve):
            if lost == reserve[i]+1 or lost == reserve[i]-1:
                cnt +=1
        answer = n+cnt-len(lost)
    return answer

solution(5, [2, 4], [1, 3, 5])



def solution(n, lost, reserve):
    new_reserve = set(reserve) - set(lost)
    new_lost = set(lost) - set(reserve)

    for i in new_reserve:
        if i-1 in new_lost:
            new_lost.remove(i-1)
        elif i+1 in new_lost:
            new_lost.remove(i+1)
    return n-len(new_lost)