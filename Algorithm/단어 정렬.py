# https://www.acmicpc.net/problem/1181

N = int(input())
word_lst = []

for i in range(N):
    word = input()
    word_cnt = len(word)
    word_lst.append((word, word_cnt))

word_lst = sorted(set(word_lst), key=lambda word: (word[1], word[0]))

for word in word_lst:
    print(word[0])




# --------------------------------------------------------------------

words = list(set([input() for _ in range(int(input()))]))
words.sort(key = lambda x : (len(x),x))
print('\n'.join(words))

for _ in range(10):
    print(_)