# https://programmers.co.kr/learn/courses/30/lessons/42586
def solution(progresses, speeds):
    answer = []
    while progresses:
        ck = False
        cnt = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        while len(progresses)!=0 and progresses[0]>=100:
            ck = True
            cnt +=1
            progresses.pop(0)
            speeds.pop(0)
        if ck ==True:
            answer.append(cnt)
    return answer