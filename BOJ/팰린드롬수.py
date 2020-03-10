# https://www.acmicpc.net/problem/1259

# import sys

# for i in sys.stdin:
while True:
    word = input()
    if word == '0':
        break
    if word == word[::-1]:
        print('yes')
    else: print('no')