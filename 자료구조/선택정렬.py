#선택정렬
# 1. 주어진 데이터 중, 최소값을 찾음
# 2. 해당 최소 값을 데이터 맨 앞에 위치한 값과 교체함
# 3. 맨 앞의 위치를 뺀 나머지 데이터를 동일한 방법으로 반복함

def seletsort(data):
    for i in range(len(data)-1):                        # 비교인덱스가 0부터  비교끝 인덱스가 data 길이 -1
        ck = False
        for j in range(i+1, len(data)):                 # 비교 시작 인덱스가 하나 씩 추가되니까 ㅇㅇ..
            if data[i] > data[j]:                       # i 부터 끝까지j 전부 비교 후 i 가 더 작으면 바꿔
                data[i], data[j] = data[j], data[i]
                ck = True
        if ck == False:
            break
    print(data)
    return data

seletsort(list(map(int, input().split())))