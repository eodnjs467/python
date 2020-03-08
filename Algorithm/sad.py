sugar = int(input())
cnt = 0

while sugar:
    if sugar%5!=0:
        sugar -= 3
        if sugar<0:
            cnt = -1
            break
        cnt +=1
    elif sugar%5==0:
        sugar -=5
        cnt+=1
    elif sugar%5!=0 and sugar%3!=0:
        cnt = -1
print(cnt)