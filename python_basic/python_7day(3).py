##내장 함수

##abs    abs(x)는 어떤 숫자를 입력받았을 때, 그 숫자의 절댓값을 돌려주는 함수이다.
abs(3)
abs(-3)
abs(-1.2)

#all    all(x)는 반복 가능한(iterable) 자료형 x를 입력 인수로 받으며 이 x가 모두 참이면 True,
# 거짓이 하나라도 있으면 False를 돌려준다.
all([1,2 ,3])
all([1, 2, 3, 0])

#any    any(x)는 x 중 하나라도 참이 있으면 True를 돌려주고,
# x가 모두 거짓일 때에만 False를 돌려준다. all(x)의 반대이다.
any([1, 2, 3, 0])
any([0, ""])

#chr    chr(i)는 아스키(ASCII) 코드 값을 입력받아 그 코드에 해당하는 문자를 출력하는 함수이다.
chr(97)
chr(48)

#dir    dir은 객체가 자체적으로 가지고 있는 변수나 함수를 보여 준다.
# 다음 예는 리스트와 딕셔너리 객체 관련 함수(메서드)를 보여 주는 예이다.
dir([1, 2, 3])
dir({'1', 'a'})

#divmod divmod(a, b)는 2개의 숫자를 입력으로 받는다.
# 그리고 a를 b로 나눈 몫과 나머지를 튜플 형태로 돌려주는 함수이다.
divmod(7, 3)

#enumerate  이 함수는 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 받아
# 인덱스 값을 포함하는 enumerate 객체를 돌려준다.
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)

#eval   실행 가능한 문자열(1+2, 'hi' + 'a' 같은 것)을 입력으로 받아
# 문자열을 실행한 결괏값을 돌려주는 함수이다.
eval('1+2')
eval("'hi' + 'a'")
eval('divmod(4, 3)')

def positive(l):
    result = []
    for i in l:
        if i>0:
            result.append(i)
    return result
print(positive([1, -3, 2, 0, -5, 6]))

def positive(x):
    return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))
list(filter(lambda x: x>0, [1, -3, 2, 0, -5, 6]))

#hex    hex(x)는 정수 값을 입력받아 16진수(hexadecimal)로 변환하여 돌려주는 함수이다.
hex(234)
hex(3)

#id     id(object)는 객체를 입력받아 객체의 고유 주소 값(레퍼런스)을 돌려주는 함수이다.
a = 3
id(a)
id(3)
b = a
id(b)

#input  input([prompt])은 사용자 입력을 받는 함수이다.
# 매개변수로 문자열을 주면 다음 세 번째 예에서 볼 수 있듯이 그 문자열은 프롬프트가 된다.
a = input()
b = input("Enter : ")
b

#int int(x)는 문자열 형태의 숫자나 소수점이 있는 숫자 등을 정수 형태로 돌려주는 함수로, 정수를 입력으로 받으면 그대로 돌려준다.
int('3')
int(3.4)
int('11', 2)
int('1A', 16)

#isinstance isinstance(object, class )는 첫 번째 인수로 인스턴스, 두 번째 인수로 클래스 이름을 받는다.
# 입력으로 받은 인스턴스가 그 클래스의 인스턴스인지를 판단하여 참이면 True, 거짓이면 False를 돌려준다.
class Person: pass

a = Person()
isinstance(a, Person)
b =3
isinstance(b, Person)

#len    len(s)은 입력값 s의 길이(요소의 전체 개수)를 돌려주는 함수이다.
len("python")
len([1, 2, 3])
len((1, 'a'))

#list   list(s)는 반복 가능한 자료형 s를 입력받아 리스트로 만들어 돌려주는 함수이다.
list("python")
list((1, 2, 3))
a = [1, 2, 3]
b = list(a)
b

# map   map(f, iterable)은 함수(f)와 반복 가능한(iterable) 자료형을 입력으로 받는다.
# map은 입력받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려주는 함수이다.
def two_times(x):
    return x * 2
list(map(two_times, [1,2 ,3 ,4]))

#max    max(iterable)는 인수로 반복 가능한 자료형을 입력받아 그 최댓값을 돌려주는 함수이다.
max([1, 2, 3])
max("python")

#oct    oct(x)는 정수 형태의 숫자를 8진수 문자열로 바꾸어 돌려주는 함수이다.
oct(34)
oct(12345)

#open   pen(filename, [mode])은 "파일 이름"과 "읽기 방법"을 입력받아 파일 객체를 돌려주는 함수이다.
# 읽기 방법(mode)을 생략하면 기본값인 읽기 전용 모드(r)로 파일 객체를 만들어 돌려준다.
# moed -> w 쓰기모드, r 읽기모드, a추가모드, b 바이너리모드(b는 wra와 함께 사용)
f = open("binary_file", "rb")
fread = open("read_mode.txt", "r")

#ord(c) 아스키 코드 값을 돌려줌.
#pow(x,y) x의 y제곱한 결과값을 돌려줌
pow(2,4)

#range
list(range(0, -10, -2))

#round  round(number[, ndigits]) 함수는 숫자를 입력받아 반올림해 주는 함수이다.
round(4.6)
round(5.678, 2)

#sorted(iterable) 함수는 입력값을 정렬한 후 그 결과를 리스트로 돌려주는 함수이다.
sorted([3, 1, 2])
sorted((3, 2, 1))

#str(object)은 문자열 형태로 객체를 변환하여 돌려주는 함수이다.
str(3)
str('r'.upper())

#sum
sum([1, 2, 3])
sum((4, 5, 6))

#tuple  tuple(iterable)은 반복 가능한 자료형을 입력받아 튜플 형태로 바꾸어 돌려주는 함수이다.
tuple("abd")

#type(object)은 입력값의 자료형이 무엇인지 알려 주는 함수이다.
type("str")
type([])
type(open("test", "w"))

#zip(*iterable)은 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수이다.
list(zip([1, 2, 3], [4, 5, 6]))
list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9]))
list(zip("abc", "def"))