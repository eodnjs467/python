import math

def Sosu(num):
    if num ==1:
        return False
    for k in range(2,int(math.sqrt(num))+1):
        if num / k == 1:
            break
        elif num % k == 0:
            return False
    return True

num1,num2 = map(int,input().split())
for k in range(num1,num2+1):
    if Sosu(k) ==True:
        print(k)