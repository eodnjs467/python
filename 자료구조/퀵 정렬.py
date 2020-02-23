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
    if len(data) <= 1: return data          #들어온 데이터가 1보다 작거나 같으면 정렬 필요가 없으므로 그대로 반환

    pivot = data[0]                         # 피봇 설정

    quick_left = [left for left in data[1:] if pivot > left]    # 피봇 기준 왼쪽 나눔
    quick_right = [right for right in data[1:] if pivot <= right]   # 피봇 기준 크면 오른 쪽 나눔

    return quick_con(quick_left) + [pivot] + quick_con(quick_right) # 왼쪽(재귀) + 피봇 + 오른쪽(재귀

aa = [4,2,5,22,55,33,77,124, 1]

quick(aa)
quick_con(aa)