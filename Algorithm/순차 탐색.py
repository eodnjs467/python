# 순차 탐색
# 탐색은 여러 데이터 중에서 원하는 데이터를 찾아내는 것을 의미
# 데이터가 담겨있는 리스트를 앞에서부터 하나씩 비교해서 원하는 데이터를 찾는 방법


from random import *
rand_data_list = []
for num in range(10):
    rand_data_list.append(randint(1, 100))
def sequential_search(data, search):
    print(data)
    for i in range(len(data)):
        if data[i] == search:
            return i
    return -1

sequential_search(rand_data_list, 23)