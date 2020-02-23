# https://www.acmicpc.net/problem/1316
# sorted(a, key=a.find)
# key = a.find 는 a ㅇ요소중 들어온 순서대로 정렬함 ex abbbba 들어오면 a가 첫번째로 들어와서 a를 나열 후 b나열
#   ex gabbwa 하면 g 나열 후 a 나열 후 b 나열 후 w나열 들어온 순서대로 정렬 후 반환

N = int(input())
ans = 0
for i in range(N):
    word = input()
    if list(word) == sorted(word, key=word.find):
        ans += 1
print(ans)