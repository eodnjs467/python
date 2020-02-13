
TC = int(input())

for i in range(TC):
    score, bonus = 0, 0         # 한 번 수행 후 각자 점수 내야하므로 0 으로 초기화
    OX = list(input())
    for j in range(len(OX)):
        if OX[j] == 'O':
            bonus += 1
            score += bonus
        else:
            bonus = 0
    print(score)