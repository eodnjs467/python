for i in range(int(input())):
    R, S = input().split()
    P = ""
    for j in range(R):             #S가 j 에 하나씩 들어감 ... 문자를 반복에 집어넣고 곱할 생각을 하자 ...
        P += int(R)*j       #R 을 숫자로해서 반복 ㄱ
    print(P)
                            #순간 S[i] 로 반복문 해서 곱하기 r 하려함 .. 그렇게 되면 S[-1] 이 공백일수도 있음 ....
                            #바보새기 ..... 이런걸로 시간 날리다니 . . . 

