## 예외처리
##try ~ except

# try:
#     ...
# except 발생오류 as 오류 메세지 변수
#     ...

try:
    4/0
except ZeroDivisionError as e:
    print(e)

try:
    a = [1, 2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)

## 오류 회피하기
try:
    f = open("나없는 파일", 'r')
except FileNotFoundError:
    pass


## 오류 일부러 발생 시키기
class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    # pass
    def fly(self):
        print("very fast")

eagle = Eagle()
eagle.fly()

## 예외 만들기
class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."

def say_nick(nick):
    if nick=="바보":
        raise MyError()
    print(nick)

say_nick("천사")
say_nick("바보")

try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)
