# 병합 정렬
# 재귀용법을 활용한 정렬 알고리즘
#     1. 리스트를 절반으로 잘라 비슷한 크기의 두 부분의 리스트로 나눈다.
#     2. 각 부분 리스트를 재귀적으로 합병 정렬을 이용해 정렬한다.
#     3. 두 부분 리스트를 다시 하나의 정렬된 리스트로 합병한다.
#     split 해서 merge(합병) 하는 함수 2개



def merge(left, right):
    tmp = []
    l_point, r_point = 0, 0
    while len(left)>l_point and len(right)>r_point:         #right 리스트 , left 리스트 둘 다 남아있을 경우
        if left[l_point] > right[r_point]:
            tmp.append(right[r_point])
            r_point += 1
        else:
            tmp.append((left[l_point]))
            l_point += 1
    while len(left)>l_point:                                # left 리스트만 남아있을 경우
        tmp.append(left[l_point])
        l_point += 1
    while len(right)>r_point:                               # right 리스트만 남아있을 경우
        tmp.append(right[r_point])
        r_point += 1
    return tmp

def split(data):
    if len(data) <= 1:
        return data
    medium = len(data)//2
    left = split(data[:medium])
    right = split(data[medium:])
    return merge(left, right)

import random
data_list = random.sample(range(100), 10)
split(data_list)
