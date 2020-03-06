def solution(num, k):
    answer = []
    number = list(num)
    while len(answer) != len(number)-k:
        tmp = []
        for i in range(len(number)-k, -1, -1):
            # print(number[i])
            tmp.append(number[i])
        answer.append(max(tmp))
        number.pop(number.index(max(tmp)))
        if len(answer) == k:
            print(answer)
            break
        k-=1
    return answer

# : k 까지 하난 만들어놓고
# k -1 하고 하나씩 추가해주자
# ex  k 를 기준으로 왼 오 나누고 왼에서 탐색해서 max 값 찾으면 answer 에 추가 하고 max 값을 0으로 만들어 그다음 오른쪽꺼 빼서 왼쪽
# 어펜드

k = 5
for i in range(k-1, -1, -1):
    print(i)
for i in range(len(number)-k-1, -1, -1):
    print(i)