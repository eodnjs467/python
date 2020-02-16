
def bubblesort(data):
    for i in range(len(data)-1):                                    # 데이터 길이 -1 만큼 양옆 체크 , 턴 //n번 만큼 반복 안에서
        ck = False
        for j in range(len(data)-i-1):                              # -i : 1 턴 후마다 체크하는게 1개씩 줄어들음 // n번 만큼 반복
            if data[j] > data[j + 1]:                               #                                   n*n이 시간복잡도가 됨
                data[j], data[j + 1] = data[j + 1], data[j]
                ck = True
        if ck == False:
                break
    return data

A = list(map(int, input().split()))
bubblesort(A)

#버블정렬 시간복잡도 O(n^2)