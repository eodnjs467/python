# 함수 내부에 정의된 또 다른 함수
# 중첩함수는 해당 함수가 정의된 함수 내에서만 호출 및 반환 가능(로컬)

def outer_func():
    print("call outer_func function")

    def inner_func():                       # 중첩함수 정의
        return 'call inner_func function'

    print(inner_func())                     # 중첩함수 호출 // 해당 함수 내에서 호출 가능

outer_func()


def outer_func(num):
    def inner_func():                       # 중첩함수에서 외부 함수의 변수 접근 가능
        print(num)
        return 'complex'

    return inner_func

fn = outer_func(10)
print(fn())