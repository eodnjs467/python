# 재귀용법
# 함수 안에서 동일한 함수를 호출하는 형태

# 일반적인 형태 1
# def function(입력):
#     if 입력 > 일정값 :
#         return function(입력-1)
#     else:
#         return 일정값 or 입력값 or 특정값
#
# 일반적인 형태 2
# def function(입력):
#     if 입력<=일정값:
#         return 일정값 or 입력값 or 특정값
#     function(입력보다 작은 값)
#     return 결과값


# 팩토리얼
# 함수 n 은 n >1 dlaus return n*(n-1)
# n =1 이면 return n
def factorial(data):
    if data >1:
        return data * factorial(data-1)
    else:
        return 1

factorial(5)

#연습2
def mul(data):
    if data<=1:
        return data
    return data * mul(data - 1)
mul(5)

# 연습3
def sum_list(data):
    if len(data) ==1 :
        return data[0]
    return data[0] + sum_list(data[1:])

n = [3, 4, 2, 5, 1, 4, 4]
sum_list(n)

# 연습4
def func(num):
    print(num)
    if num ==1:
        return num
    elif num%2 != 0:
        return func(3*num+1)
    else:
        return func(num//2)

func(3)