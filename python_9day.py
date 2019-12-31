##3과 5의 배수 합하기

result = 0
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        result += i
print(result)

#게시판 페이징 하기 // 총 페이지 수 : (총 건수/ 한 페이지당 보여줄 건수 )+1
def getTotalPage(m, n):
    total = (m/n)+1
    return total
a = getTotalPage(5, 10)
int(a)

## 간단한 메모장 만들기
import sys
option = sys.argv[1]

if option == '-a':
    memo = sys.argv[2]
    f = open('memo.txt', 'a')
    f.write(memo)
    f.write('\n')
    f.close()
elif option == '-v':
    f = open('memo.txt')
    memo = f.read()
    f.close()
    print(memo)
