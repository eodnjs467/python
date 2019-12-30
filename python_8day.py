##외장함수

#sys 모듈은 파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈이다.
import sys
print(sys.argv)
sys.exit

#pickle은 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈이다.
import pickle
f = open("test.txt", "wb")
data = {1: 'python', 2: 'you need'}
pickle.dump(data, f)
f.close()

import pickle
f = open("test.txt", "rb")
data = pickle.load(f)
print(data)

#shutil은 파일을 복사해 주는 파이썬 모듈이다.
import shutil
shutil.copy("src.txt", "dst.txt")

#glob 가끔 파일을 읽고 쓰는 기능이 있는 프로그램을 만들다 보면
# 특정 디렉터리에 있는 파일 이름 모두를 알아야 할 때가 있다. 이럴 때 사용하는 모듈이 바로 glob이다.
import glob
glob.glob("c:/doit/mark*")  #c:/doit 디렉터리에 있는 파일 중 mark로 시작하는 파일을 모두 찾아라

#tempfile 파일을 임시로 만들어서 사용할 때 유용한 모듈이
#tempfile.TemporaryFile()은 임시 저장 공간으로 사용할 파일 객체를 돌려준다. 이 파일은 기본적으로 바이너리 쓰기 모드(wb)를 갖는다.
# f.close()가 호출되면 이 파일 객체는 자동으로 사라진다.
import tempfile
filename = tempfile.mktemp()
filename

import tempfile
f = tempfile.TemporaryFile()
f.close()

#time
#   -time   UTC(Universal Time Coordinated 협정 세계 표준시)를 사용하여 현재 시간을 실수 형태로 돌려주는 함수이다.
import time
time.time()

#   -localtime  time.localtime은 time.time()이 돌려준 실수 값을 사용해서 연도, 월, 일, 시, 분, 초, ... 의 형태로 바꾸어 주는 함수이다.
time.localtime(time.time())

#   -asctime, -ctiome,  -strftime
#-sleep
import time
for i in range(10):
    print(i)
    time.sleep(1)

#calendar는 파이썬에서 달력을 볼 수 있게 해주는 모듈이다.
import calendar
print(calendar.calendar(2015))
calendar.prcal(2015)
calendar.prmonth(2015, 12)  #2015년 12월 달력만 보여줌
calendar.weekday(2015, 12, 31)  #해당 날짜의 요일을 알려줌 0 - 월, 1 - 화, ...

#random은 난수(규칙이 없는 임의의 수)를 발생시키는 모듈이다
import random
random.random()
random.randint(1, 10)   #randint 를 사용하여 1에서 10 사이의 정수 중 난수 값을 돌려줌.
random.randint(1, 55)

import random
def random_pop(data):
    number = random.randint(0, len(data)-1)
    return data.pop(number)
if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    while data:
        print(random_pop(data))

def random_pop(data):
    number = random.choice(data)
    data.remove(number)
    return number

import random
data = [1, 2, 3, 4, 5]
random.shuffle(data)
data

#webbrowser는 자신의 시스템에서 사용하는 기본 웹 브라우저를 자동으로 실행하는 모듈이다.
import webbrowser
webbrowser.open("http://google.com")
webbrowser.open_new("http://google.com")

#스레드를 다루는 threading 모듈
import time
import threading

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s\n" % i)
print("Start")

threads = []
for i in range(5):
    t = threading.Thread(target=long_task)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

print("End")




##연습문제

#Q1
class Calculater:
    def __init__(self):
        self.value = 0
    def add(self, val):
        self.value +=val
class UpgradeCalculater(Calculater):
    def minus(self, val):
        self.value -= val
cal = UpgradeCalculater()
cal.add(10)
cal.minus(7)
print(cal.value)

#Q2
class MaxLimitiCalculater(Calculater):
    def add(self, val):
        if (self.value + val) >= 100:
            self.value = 100
        else:
            self.value += val
cal = MaxLimitiCalculater()
cal.add(50)
cal.add(60)
print(cal.value)

#Q3
False
True

#Q4
list(filter(lambda x: x > 0, [1, -2, 3, -5, 8, -3]))

#Q5
int(0xea)

#Q6
list(map(lambda x: x*3, [1, 2, 3, 4]))

#Q7
max([-8, 2, 7, 5, -3, 5, 0, 1])
min([-8, 2, 7, 5, -3, 5, 0, 1])

#Q8
round(17/3, 4)

#Q9


#Q10


#Q11


#Q12
import time
time.strftime()


#Q13