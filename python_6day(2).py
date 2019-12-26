##클래스

result = 0

def add(num):
    global result
    result = result + num
    return result

print(add(3))

## 계산기 2개시
result1 = 0
result2 = 0

def add1(num):
    global result1
    result1 += num
    return result1

def add2(num):
    global result2
    result2 += num
    return result2

print(add2(4))
print(add1(7))
print(add2(5))

## 클래스 구조 만들기, 생성자
class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
a = FourCal()
a.setdata(5, 2)
a.sub()
a = FourCal(4, 2)
a.sub()

## 상속 class 클래스 이름(상속할 클래스 이름)
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result
a = MoreFourCal(4,0)
a.div()

## 메서드 오버라이딩
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0 :
            return 0
        else:
            return self.first / self.second

a = SafeFourCal(4, 0)
a.div()

## 클래스 변수
class Family:
    lastname = "김"

print(Family.lastname)

a = Family()
b = Family()
print(a.lastname)
print(b.lastname)
Family.lastname = "박"

id(Family.lastname)
id(a.lastname)
id(b.lastname)