# https://www.acmicpc.net/problem/1874

n = int(input())
cnt = 1
stack, result = [], []

for i in range(1, n+1):
    data = int(input())
    while cnt <= data:
        stack.append(cnt)
        cnt += 1
        result.append('+')
    if stack[-1] == data:
        stack.pop()
        result.append('-')
    else:
        print("NO")
        exit(0)
print('\n'.join(result))


# exit : interactive interpreter shell에서
# sys.exit : program에서
# 파일에서
# #myfile.py - 파이썬 파일 안에서
# import sys
# exit()#안됨
# sys.exit() #됨
#
# 쉘에서
# $ python
# Python 2.7.11 (default, Dec  5 2015, 14:44:53)
# [GCC 4.2.1 Compatible Apple LLVM 7.0.0 (clang-700.1.76)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> exit() #됨
# $



#
# 1.
# break
#
# -switch문 / 반복문에서
# 중괄호를
# 빠져나오게
# 함.
#
# 2.
# return
#
# -함수에서
# 빠져나오게
# 함.
#
# -그
# 아래
# 코드는
# 실행하지
# 않음.
#
# 3.
# exit
#
# -main함수가
# 아닌
# 곳에서도
# 프로그램을
# 종료시킴(그렇군!)
#
# -main함수에서
# return 0
# 한
# 것과
# 동일
#
# -exit(0)
# 정상적인
# 종료
#
# exit(1)
# 비정상적인
# 종료(에러가
# 발생함을
# 보여줌)
