##제어문(while)

##while 조건문 :
##    수행할 문장1
##    수행할 문장2
##    ...

##열 번 찍어 안 넘어가는 나무 없다
treeHit = 0
while treeHit < 10 :
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다." %treeHit)
    if treeHit == 10 : print("나무 넘어갑니다.")

prompt = """
    1. Add
    2. Del
    3. List
    4. Quit
    ...
    Enter number: """

number = 0
while number != 4:
    print(prompt)
    number = int(input())

coffee = 10
money = 300
while money :
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee -1
    print("남은 커피의 양은 %d 개 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break


coffee = 10
while True :
    money = int(input("돈을 넣어주세요"))
    if money == 300:
        print("커피를 줍니다.")
        coffee -= 1
        print("남은 커피는 %d 개 입니다." % coffee)
    elif money > 300:
        print("거스름돈 %d 받으세요" % (money-300))
        coffee -=1
        print("남은 커피는 %d 개 입니다." % coffee)
    else:
        print("돈이 부족합니다.")
        print("남은 커피는 %d 개 입니다." % coffee)
    if coffee == 5:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break


a = 0
while a < 10:
    a+=1
    if a % 2 == 0 : continue
    print(a)

#무한루프
while True:
    print("Ctrl + C 를 눌러야 while문을 빠져나갈 수 있습니다.")
