# 1. 해쉬 구조
# Hash Table : 키(Key)에 데이터를 저장하는 데이터 구조
#     Key를 통해 바로 데이터를 받아올 수 있으므로, 속도가 획기적으로 빨라짐
#     보통 배열로 미리 Hash Table 사이즈만큼 생성 후에 사용
#     파이썬의 경우 딕셔너리 사용하면 됨
#
# 2. 알아둘 용어
# 해쉬(Hash) : 임의 값을 고정 길이로 변환하는 것
# 해쉬 테이블(Hash Table) : 키 값의 연산에 의해 직접 접근이 가능한 데이터 구조
# 해싱 함수(Hashing Function) : Key에 대해 산술 연산을 이용해 데이터 위치를 찾을 수 있는 함수
# 해쉬 값(Hash Value) or 해쉬 주소(Hash Address) : Key를 해싱함수로 연산해서 값을 알아냄
#
# 자료구조 해쉬테이블의 장단점과 주요 용도
# 장점
#     데이터 저장/읽기 속도가 빠르다.(검색속도가 바르다.)
#     해쉬는 키에 대한 데이터가 있는지(중복)확인이 쉬움
# 단점
#     일반적으로 저장공간이 좀 더 많이 필요하다.
#     여러 키에 해당하는 주소가 동일할 경우 충돌을 해결하기 위한 별도 자료구조가 필요함
# 주요 용도
#     검색이 많이 필요한 경우
#     저장, 삭재, 읽기가 빈번한 경우
#     캐쉬 구현시 (중복 확인이 쉽기 때문)


3.
hash_table = list([i for i in range(10)])
hash_table

def hash_func(key):
    return key%5

data1 = 'Andy'
data2 = 'Dave'
data3 = 'Trump'

##ord() : 문자의 ASCII 코드 리턴
print(ord(data1[0]), ord(data2[0], ord(data3[0])))
print(ord(data1[0]), hash_func(ord(data1[0])))

def storage_data(data, value):
    key = ord(data[0])
    hash_address = hash_func(key)
    hash_table[hash_address] = value

storage_data('Andy', '01055553333')

def get_data(data):
    key = ord(data[0])
    hash_address = hash_func(key)
    return hash_table[hash_address]

get_data('Andy')


# 리스트 변수를 활용해서 해쉬 테이블 구현해보기
# 1. 해쉬 함수 : key % 8
# 2. 해쉬 키 생성 : hash(data)

hash_table = list([0 for i in range(8)])

def get_key(data):
    return hash(data)
