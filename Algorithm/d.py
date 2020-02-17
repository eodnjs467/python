def merge(left, right):
    merged = list()
    left_point, right_point = 0, 0

    #case1: left/ right 남아있을 때
    while len(left) > left_point and len(right) > right_point:
        if left[left_point] > right[right_point]:
            merged.append(right[right_point])
            right_point+=1
        else:
            merged.append(left[left_point])
            left_point+=1
    #case2: left 만 남았을 때
    while len(left) > left_point:
        merged.append(left[left_point])
        left_point+=1
    while len(right) > right_point:
        merged.append(right[right_point])
    return merged

def mergesplit(data):
    if len(data) <= 1:
        return data
    medium = int(len(data)/2)
    left = mergesplit(data[:medium])
    right = mergesplit(data[medium:])
    return merge(left, right)

import random

data_list = random.sample(range(100), 10)
# data_list1 = [1, 70, 30, 33, 20, 54, 24, 64, 12, 3, 5, 6,2]
mergesplit(data_list)