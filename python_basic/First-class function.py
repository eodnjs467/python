# First-class 함수: 함수 자체를 인자로 다른 함수에 전달, 다른 함수의 결과값으로 리턴, 함수를 변수에 할당할 수 있는 함수

def calc_square(digit):
    return digit * digit

calc_square(2)
func1 = calc_square     # func1 이라는 변수에 함수를 할당.
print(calc_square)
func1(2)                # func1 변수는 calc_square 함수를 가리키고, 인자도 넣어서 결과 얻을 수 있음

class MyClass:
    def my_class(self):
        print('안녕')
        pass

object1 = MyClass()
my_class1 = object1.my_class
my_class1()

