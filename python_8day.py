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