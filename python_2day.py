""" 1장 ~ 2.2장(문자열 자료형) 몰랐던 것만 정리."""

#format 함수.
"I am {0} apples. sicl {day} days".format(3, day=2)

#공백 채우기(:^ ==중앙정렬, :>, :<).
"{0:=^10}".format("hi")

#f문자열, 딕셔너리 f문자열 포매팅
name="홍길동"
age="30"
f"나의 이름은 {name}이고, 나이는 {age}이다."
d={'name':'박보검', 'age':'25'}
f"나의 이름은 {d['name']}이고, 나이는 {d['age']}이다."

