##함수

## def 함수명(매개변수):
## 수행할 문장1
## 수행할 문장2 ...

def add(a, b):
    return a + b

a, b = 3, 4
c = add(a, b)
print(c)

def add(a, b):     ## a,b 는 매개변수
    return a+b

print(add(3, 4))    ## 3, 4 는 인수

## 일반적인 함수
def add(a, b):
    result = a+b
    return result

def say():
    return 'Hi'
a = say()
print(a)

##결괏값이 없는 함수
def add(a, b):
    print("%d, %d 의 합은 %d 입니다," % (a, b, (a+b)))
add(3, 5)
a = add(3, 4)
print(a)

def say():
    print('Hi')
say()

def add(a, b):
    return a+b
result = add(a=3, b=7)
print(result)

## 여러 개의 입력값을 받는 함수 만들기
## def 함수이름(*매개변수):
## 수행할 문장 ...

def add_many(*args):        ## *을 붙이면 입력값을 모두 모아서 튜플로 만들어 줌.
    result = 0
    for i in args:
        result = result + i
    return result

result = add_many(1, 2, 3)
print(result)
result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result)

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result

result = add_mul('add', 1, 2, 3, 4, 5)
print(result)
result = add_mul('mul', 1, 2, 3, 4, 5)
print(result)

## 키워드 파라미터 -> 매개변수 앞에 ** 붙이면 딕셔너리가 되고,
# key=value형태의 결괏값이 딕셔너리에 저장됨.
def print_kwargs(**kwargs):
    print(kwargs)
print_kwargs(a=1)

## 함수 리턴값은 언제나 하나!
def add_and_mul(a, b):
    return a+b, a*b
result = add_and_mul(3, 4)
result
result1, result2 = add_and_mul(3, 4)
result1, result2

## return의 다른 쓰임새 return 단도긍로 써서 함수를 빠져나갈 수 있음.
def say_nick(nick):
    if nick=="바보":
        return
    print("나의 별명은 %s 입니다." % nick)
say_nick('야호')
say_nick('바보')

## 매개변수에 초깃값 미리 설정하기
def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d 살 입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
say_myself("박응용", 27)


def say_intro(name, old, sex):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d 살 입니다." % old)
    if sex == 0:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_intro("대원", 25, 0)

a=1
def vartest(a):
    a = a+1
vartest(a)
print(a)

## 함수 안에서 함수 밖의 변수를 변경하는 법

## return 사용하기
a = 2
def vartest(a):
    a = a+1
    return a
a = vartest(a)
print(a)

## global 명령어 사용하기
a = 1
def vartest():
    global a
    a = a+1
vartest()
print(a)

## lambda 함수
## lambda 매개변수1, 매개변수2, ... : 매개변수를 이용한 표현식
add = lambda a, b : a+b
result  = add(3, 4)
print(result)