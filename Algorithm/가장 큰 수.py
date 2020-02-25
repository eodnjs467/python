# https://programmers.co.kr/learn/courses/30/lessons/42746
# lambda 함수 활용법, 내림차순 정렬 해서 사용하는게 제일 큰 값이 나옴
# String 의 사전 크기를 알게됨 8999보다 9 가 큼
# x*3 한 이유는 numbers의 원소 값이 1,000이하여서 백의 자리수 까지만 비교하면 됨 .
# int형이라 join 후 str로 출력

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    answer = str(int(''.join(numbers)))
    return answer
