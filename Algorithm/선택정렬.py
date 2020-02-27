a = [34,55,43,12,63,4,32,21,22,6,5,7,3,8,1]
# sorted(a, reverse=True)
for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        if a[i]>a[j]:
            a[i], a[j] = a[j], a[i]
print(a)

# 삽입 정렬은 특정 수를 넣는게 아니라 그냥 뒤에서 앞으로 ex) 2번부터 1번 3번부터 2,1 번 4번부터 3,2,1 번 비교
a = [34,55,43,12,63,4,32,21,22,6,5,7,3,8,1]
for i in range(1, len(a)+1):
    for j in range(i-1, 0, -1):
        if a[j]<a[j-1]:
            a[j], a[j-1] = a[j-1], a[j]
print(a)

#버블정렬
a = [34,55,43,12,63,4,32,21,22,6,5,7,3,8,1]
for i in range(len(a)-1):
    for j in range(len(a)-1):
        if a[j]>a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print(a)

#퀵정렬    0번 인덱스를 pivot으로 설정 후 pivot 보다 작으면 왼쪽 크면 오른쪽
def quick_sort(data):
    if len(data) <= 1: return data

    pivot = data[0]

    quick_left = [left for left in data[1:] if pivot > left]
    quick_right = [right for right in data[1:] if pivot <= right]

    return quick_sort(quick_left) + [pivot] + quick_sort(quick_right)
a = [34,55,43,12,63,4,32,21,22,6,5,7,3,8,1]
quick_sort(a)

#병합정렬       반으로 나워서 오른쪽 왼쪽  합칠땐