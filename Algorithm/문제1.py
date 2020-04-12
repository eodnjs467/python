import sys

print("시작 : ")
start = int(sys.stdin.readline())

print("종료 : ")
end = int(sys.stdin.readline())

print("배수 : ")
odd = int(sys.stdin.readline())
sum = 0


for i in range(1, end//4+1):
    if i*4<start: continue
    else: sum += i*4

print(sum)