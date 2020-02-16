#삽입 정렬
# 1. 삽입 정렬은 두 번째 인덱스부터 시작
# 2. 해당 인덱스(key 값) 앞에 있는 데이터(B)부터 비교해서 key 값이 더 작으면, B 값을 뒤 인덱스로 복사
# # 3. 이를 key 값이 더 큰 데이터를 만날때까지 반복, 그리고 큰 데이터를 만난 위치 바로 뒤에 key 값을 이동
# 데이터 길이 조건체크 턴
#     2       1       1
#     3       2       2
#     4       3       3
A = [2, 6, 3, 1, 7,50, 49, 55]

def insertsort(data):
    for i in range(len(A)-1):
        for j in range(i+1, 0, -1):
            if data[j] < data[j-1]:
                data[j], data[j-1] = data[j-1], data[j]
            else:
                break
    return data

insertsort(A)