for i in range(int(input())):
    score, bonus = 0, 0
    quiz = input()
    for j in quiz:
        if j == 'O':
            bonus += 1
            score += bonus
        else:
            bonus = 0
    print(score)