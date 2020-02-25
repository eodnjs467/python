def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        answer.append(sorted(array[int(commands[i][0])-1:int(commands[i][1])])[int(commands[i][2])-1])
    return answer

array, commands = [1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
solution(array, commands)

# a = [[j for j in input().split()] for i in range(int(input()))]           #2차원 배열 입력받기