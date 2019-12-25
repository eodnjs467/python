#제어문

##  if 조건문:
##      수행할 문장1
##      수행할 문장2
##  else :
##      수행할 문자a
##      수행할 문자b

## 3000원 이상의 돈을 가지고 있으면 택시를 타고 그렇지 않으면 걸어가라.
money = 2000

if money>=3000 :
    print('택시를 타라')
else :
    print('걸어가라')

## 3000원 이상 있거나 카드가 있다면 택시를 타고 그렇지 않으면 걸어가라.
money = 2000
card = True

if money>=3000 or card :
    print('택시타라')
else:
    print('걸어가라')

## 주머니에 돈이 있으면 택시를 타고, 없으면 걸어가라.
pocket = ['paper', 'cellphone', 'money']

if 'money' in pocket:
    print('택시타라')
else:
    print('걸어가라')


#### 주머니에 돈이 있으면 가만히 있고, 돈이 없으면 카드를 꺼내라.
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass
else:
    print('카드를 꺼내라')

####주머니에 돈이 있으면 택시를 타고,
# 주머니에 돈은 없지만 카드가 있으면 택시를 타고, 돈도 없고 카드도 없으면 걸어 가라

pocket = ['paper', 'handphone']
card = True
if 'money' in pocket:
    print('택시타라')
elif card:
    print('택시타라')
else:
    print('걸어가라')

if 'money' in pocket: pass
else: print('카드를 꺼내라')


## 조건부 표현식( 조건문이 참인 경우  if 조건문 else 조건문이 거짓인 경우)
score = 76
if score >=60:
    message = "success"
else:
    message = "failure"
print(message)

message = 'success' if score>=60 else 'failure'
print(message)
