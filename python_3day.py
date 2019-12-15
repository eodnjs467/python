#공백 지우기(strip)
a="   hi    "
a.lstrip()

#문자열 바꾸기(replace)
a = "Life is too short"
a.replace("Life", "Your leg")

#문자열 나누기(split)
a = 'Life is too short'
a.split("t")
b = "a:b:c:d"
b.split(":")

#리스트 인덱싱, 슬라이싱
a = [1, 2, 3]
a[0] + a[2]

a = [1, 2, ['a', 'b', ['Life', 'is']]]
a[2][2][0]
str(a[0]) + a[2][1]
a[0:2]
a[:3]
a*3

#리스트 길이 구하기(len)
a = [1, 2, 3]
len(a)

#리스트 요소 삭제하기(del)
a = [1, 2, 3]
del a[1]

#요소 추가하기(append)
a  = [1, 2, 3, 4]
a.append(5)
a

#정렬 (sort(), reverse())


#리스트 요소 삽입, 제거(insert, remove)
a = [1, 2, 3, 4]
a.insert(0, 5)
a.remove(3)
a

#리스트 요소 끄집어내기(pop)
a = [1,2 ,3]
a.pop()
a

#리스트 확장(extend)
a = [1, 2, 3]
a.extend([4, 5])
b = [6, 7]
a.extend(b)
a