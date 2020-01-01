##반목문 (for)

## for 변수 in 리스트(또는 튜플, 문자열) :
##  수행할 문장1
##  수행할 문장2
##  ...

test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)

##총 5명의 학생이 시험을 보았는데 시험 점수가 60점이 넘으면 합격이고 그렇지 않으면 불합격이다.
# 합격인지 불합격인지 결과를 보여 주시오.

marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number+=1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)

marks = [90, 25, 67, 45, 80]
number = 0

for mark in marks:
    number +=1
    if mark < 60:
        continue
    print("%d번 학생 합격을 축하합니다." % number)

a = range(10)
a
a = range(1, 11)

add = 0
for i in range(1, 11):
    add = add + i
print(add)

marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("%d번 학생 합격을 축하합니다." % (number+1))


## for, range를 이용한 구구단

for i in range(2,10):
    for j in range(1, 10):
        print(i*j, end = " ")
    print('')

##print(i*j, end=" ")와 같이 매개변수 end를 넣어 준 이유는
# 해당 결괏값을 출력할 때 다음줄로 넘기지 않고 그 줄에 계속해서 출력하기 위해서이다.
##print(' ')는 2단, 3단 등을 구분하기 위해 두 번째 for문이 끝나면
# 결괏값을 다음 줄부터 출력하게 해주는 문장이다.

##리스트 내포 사용하기
a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num*3)
print(result)

a = [1, 2, 3, 4]
result = [num * 3 for num in a]

## 표현식 for 항목 in 반복가능객체 if 조건문]

a = [1, 2, 3, 4]
result = [num *3 for num in a if num % 2 == 0]
result

result = [x*y for x in range(2, 10)
          for y in range(1, 10)]

##연습문제
#Q1
shirt
need

#Q2
num = 0
hap = 0
while num < 1000:
    hap = hap + num
    num = num +3
print(hap)

#Q3
i = 0
while i<5 :
    i = i+1
    print("*"*i)

#Q4
for i in range(1, 101):
    print(i)

#Q5
a = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum = 0
for i in range(len(a)):
    sum = sum + a[i]
print(int(sum/len(a)))


#Q6
numbers = [1, 2, 3, 4, 5]
result = [n * 2 for n in numbers if n % 2 == 1]
result

