# https://programmers.co.kr/learn/courses/30/lessons/42577

import collections
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    print(list(answer.keys())[0])



def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i, j in zip(participant, completion):       # zip()로 여러개 비교
        if i!=j:
            return i
    return participant[-1]





# def solution(participant, completion):
#     answer = ''
#     for i in completion:
#         participant.remove(i)
#     for i in participant:
#         answer += i
#         # print('{0}'.format(i))
#     return answer




participant= ['leo', 'kiki', 'eden']
completion = ['eden', 'kiki']
solution(participant, completion)