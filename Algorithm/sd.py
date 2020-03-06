
min_data = 100000
for i in input().split():
    data = int(i)
    if abs(data) < abs(min_data):
        if abs(data) == abs(min_data):
            if data > 0:
                min_data = data
        min_data = data
    if data ==0:
        print('0')
        break
print(min_data)