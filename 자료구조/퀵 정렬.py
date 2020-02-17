# 기준점(Pivot) 설정 후 기준점 보다 작으면 left , 크면 right 즉, left  pivot  right 가 됨

def quick(data):
    if len(data) <= 1:
        return data

    quick_l, quick_r = [], []
    pivot = data[0]

    for i in range(1, len(data)):
        if pivot > data[i]:
            quick_l.append(data[i])
        else:
            quick_r.append(data[i])
    return quick(quick_l) + [pivot] + quick(quick_r)

# list_conprehension 사용시

def quick_con(data):
    if len(data) <= 1: return data

    pivot = data[0]

    quick_left = [left for left in data[1:] if pivot > left]
    quick_right = [right for right in data[1:] if pivot <= right]

    return quick_con(quick_left) + [pivot] + quick_con(quick_right)

aa = [4,2,5,22,55,33,77,124, 1]

quick(aa)
quick_con(aa)