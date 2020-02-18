# 이진 탐색
# 받은 값 정렬 후 이진 탐샘 ㄱㄱㄱ
# 데이터와 찾을 값 data_list, find_data
# func 함수(data_list, find_data)만들고
# data_list의 중간 값을 find_data 와 비교해서
# mid(data_list) == find_data : return mid(data_list)
#     find_data<mid(data_list):
#     [:mid(data_list)]
# else: dd

def binary_search(data, search):
    # print(data)
    if len(data) == 1 and data[0] == search: return True        #입력 데이터의 수 중 남은 데이터가 1개 이고, 그 데이터와 찾을값과 같으면 True
    if len(data) == 1 and data[0] != search: return False       # " " " " False

    mid = len(data)//2
    if data[mid] == search:                                     #데이터의 중간 값과 찾을 값이 같으면 True
        return True
    else:
        if search < data[mid]:                                  #데이터의 중간 값이 찾을 값 보다 크면 중간부터 오른쪽끝까지 버려
            return binary_search(data[:mid], search)
        else:
            return binary_search(data[mid:], search)

import random
data_list = random.sample(range(100), 10)
data_list.sort()
data_list
binary_search(data_list, )