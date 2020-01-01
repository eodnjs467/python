# 스택
# 데이터를 제한적으로 접근할 수 있는 구조
#   한 쪽 끝에서만 자료를 넣거나 뺄 수 있는 구조
# 가장 나중에 쌓은 데이터를 가장 먼저 빼낼 수 있는 구조

# 스택 구조
# 스택은 LIFO(Last-in, First-out) 또는 FILO(First-in, Last-out) 데이터 관리 방식을 따름
#     LIFO:마지막에 넣은 데이터를 가장 먼저 추출하는 데이터 관리 정책
#     FILO : 처음에 넣은 데이터를 가장 마지막에 추출하는 데이터 관리 정책
# 대표적인 스택의 활용
#     컴퓨터 내부의 프로세스 구조의 함수 동작방식
# 주요기능
#     push() : 데이터를 스택에 넣기
#     pop() : 데이터를 스택에서 꺼내기


# 자료구조 스택의 장단점
# 장점
#     구조가 단순해서, 구현이 쉽다.
#     데이터 저장/ 읽기 속도가 빠르다
# 단점(일반적인 스택 구현시)
#     데이터 최대 갯수를 미리 정해여한다.
#         파이썬의 경우 재귀함수는 1000번까지만 호출 가능
#     저장 공간의 낭비가 발생할 수 있음
#         미리 최대 갯수만큼 저장 공간을 확보해야함

# 파이썬 리스트 기능에서 제공하는 메서드로 스택 사용해보기(append(push), pop) 메서드 제공
data_stack = list()
data_stack.append(1)
data_stack.append(2)
data_stack
data_stack.pop()

# 연습1 : 리스트 변수로 스택을 다루는 pop, push 함수 사용하지 않고 직접 구현
stack_list = list()
def push(data):
    stack_list.append(data)

def pop():
    data = stack_list[-1]
    del stack_list[-1]
    return data

for index in range(10):
    push(index)

pop()