A = [3, 4, 1]
B = [3, 1, 2]

A = {i: '있습니다' for i in A}

for i in B:
    print(A.get(i, '없습니다.'))
