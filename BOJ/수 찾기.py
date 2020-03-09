# https://www.acmicpc.net/problem/1920

def binary(data, search, low, high):
    if low > high:
        return False

    mid = (low + high)//2

    if data[mid] == search:
        return True
    elif data[mid] < search:
        return binary(data, search, mid+1, high)
    else:
        return binary(data, search, low, mid-1)

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
a.sort()

for i in b:
    if binary(a, i, 0, n-1):
        print(1)
    else:
        print(0)




def binary(data, search):
    if len(data)==1 and data[0]==search: return True
    if len(data)==1 and data[0]!=search: return False

    mid = len(data)//2

    if data[mid] == search:
        return True
    elif data[mid] < search:
        return binary(data[mid:], search)
    else:
        return binary(data[:mid], search)