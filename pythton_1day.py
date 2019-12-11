print("Hello World!")

#수와 계산
print(10+5)

#값 추가하기(.append)
clovers = []
clovers.append("클로버")
print(clovers)
clovers.append("하트2")
print(clovers)
clovers.append("클로버3")
print(clovers)

#값에 접근하기
print(clovers[1])
clovers[1] = "클로버2"
print(clovers)

#값 제거하기(.del)
print(clovers[1])
del clovers[1]
print(clovers[1])
print(clovers)

#'콜라맛', '포도맛' 사탕을 candies 에 추가하시오
# candies에서 '박하맛' 사탕을 제거하시오
candies = ["딸기맛","레몬맛", "수박맛", "박하맛", "우유맛"]
candies.append("콜라맛")
candies.append("포도맛")
print(candies)
del candies[3]

#여러 값 가져오기(리스트[시작index : 끝index+1]
week = ['월', '화', '수', '목', '금', '토', '일']
print(week)
print(week[2:5])

#정렬하기(리스트.sort()
animals = ['체셔고양이', '오리', '도도새']
animals.sort()
print(animals)

#개수 세기(리스트.count(세어볼 값))
cards = ['하트', '클로버', '하트', '다이아']
print(cards.count("하트"))
print(cards.count('클로버'))

#for문 for 변수 in 리스트 : 실행할 명령
for num in range(500):
    print("안녕 거북이", num)

players = ['공작부인', '흰 토끼', '하트잭', '모기장수']
for player in players:
    print(player + "퇴장!! 나가세요")
    print(player, "퇴장 나가세요!")

#문자열 반복하기(for 변수 in 문자열 : 실행할 명령)
for letter in '체셔고양이' :
    print(letter)

#_-----------------------------2019-12-11일 pyhthon study 1day -----------------------------------