# 튜블 자료형
#차이점 : 리스트는 [] 튜플은 ()로 둘러쌈. 리스트는 값을 생성, 삭제, 수정 가능. 튜플은 값 변경x
t1=()
t2=(1, )
t3=(1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))
#1개의 요소만을 가질 떄는 요소 귀에 콤마(,)를 반드시 붙여야 함, t4처럼 () 생략 가능


#딕셔너리 자료형 {key1:value1, key2:value2, ...} key는 변하지 않는 값, value는 변하는 값, 변하지 않는 값
dic = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
dic['name']
a={1:'hi'}
a = {'a':[1,2,3]}

#딕셔너리 쌍 추가, 요소 삭제
a = {1:'a'}
a[3] = 'b'
del a[1]

#딕셔너리 관련 함수(keys)
a = {'name' : 'pey', 'phone' : '0119993323' , 'birth' : '1118'}
a.keys()

for k in a.keys():
    print(k)

#리스트로 변환시
list(a.keys())

#value 리스트 만들기(values)
a.values()

# key, value 쌍 얻기(items), 쌍 모두 지우기 (clear)
a.items()
a.clear()

#key로 value 얻기(get)
a={'name':'pey', 'phone':'0119993323', 'birth':'11180000'}
a.get('name')
print(a.get['nokey'])
#get(x, '디폴트 값')
a.get('foo','bar')

#해당 key 딕셔너리 안에 있는지 조사 (in)
'name' in a
'email' in a

#집합자료형(set) 중복 허용x, 순서 x , 자료형의 중복을 제거하기 위한 필터역할로 종종 사용함.
s1 = set([1, 2, 3])
s2 = set("Hello")
l1 = list(s1)
t1 = tuple(s1)

#교집합(& or intersection), 합집합(union or | ), 차집합(- or difference)
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

s1 & s2
s1.intersection(s2)

s1 | s2
s1.union(s2)

s1 - s2
s2 - s1

#집합 자료형 함수들 값1개 추가(add), 여러 개 추가(update), 특정 값 제거(remove)
s1 = set([1, 2, 3])
s1.add(4)
s1

s1 = set([1, 2, 3])
s1.update([4, 5, 6])
s1
s1 = set([1, 2, 3])
s1.remove(2)
s1

#불 자료형 (True, False 첫 문자 대문자)
a = True
b = False

type(a)

1==1
2>1
2<1

a = [1, 2, 3, 4]
while a :
    print(a.pop())

bool('python')
bool('')

# 변수
a = [1, 2, 3]
id(a)
b=a
b
a is b
a[1] = 4
a
b
a = [1, 2, 3]
b = a[:]
a[1] = 4
a
b

#변수 만드는 여러가지 방법
a, b = ('python', 'life')
(a, b) = 'python', 'life'
[a, b] = ['python', 'life']
a = b = 'python'
a, b = 3, 5
a, b = b, a # 서로 값 변경 가능

#연습문제
#Q1
a, b, c = 80, 75, 55
(a+b+c)/3

#Q2
if (13%2)==1 :
    print('홀수')
else :
    print('짝수')

#Q3
a = '881120-1068234'
print(a[:6] + "\n" + a[7:])

#Q4
pin = "881120-1068234"
pin[7]

#Q5
a = "a:b:c:d"
a.replace(":" , "#" )

#Q6
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()

#Q7
a = ['Life', 'is', 'too', 'short']
result = " ".join(a)
print(result)

#Q8
t1 = (1, 2, 3)
t1 = t1 + (4, )
print(t1)

#Q9
#생략


#Q10
a = {'A':90, 'B':80, 'C':70}
a.pop('B')

#Q11
a = [1, 1, 1, 2, 2, 3, 3 ,3 ,4, 4, 5]
aSet = set(a)
b =  list(aSet)
print(b)

#Q12
a = b = [1, 2, 3]
a[1] = 4
print(b)
#b 는 a와 같아서 주소가 연결되있음 ㅇㅇㅇ