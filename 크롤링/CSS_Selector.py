import requests
from bs4 import BeautifulSoup

res = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(res.content, 'html.parser')

# 태그 검색
soup.find('title')

# select 함수는 리스트 형태로 전체 반환
title = soup.select('title')[0]
print(title)
print(title.get_text())
# 띄어쓰기가 있다면 하위 태그를 검색
title = soup.select('html head title')[0]
print(title.get_text())
# 띄어쓰기가 있다면 하위 태그를 검색
# 이때 바로 직계의 자식이 아니여도 관계없음
title = soup.select('html title')[0]
print(title.get_text())
# > 를 사용하는 경우 바로 아래의 자식만 검색
# 바로 아래 자식이 아니기 때문에 에러 발생
title = soup.select('html > title')[0]
print(title.get_text())

# .은 태그의 클래스를 검색
# class가 article_view인 태그 탐색
body = soup.select('.article_view')[0]
print(type(body), len(body))
for p in body.find_all('p'):
    print(p.get_text())
# div태그 중 class가 article_view인 태그 탐색
body = soup.select('div.article_view')[0]
print(type(body), len(body))
for p in body.find_all('p'):
    print(p.get_text())
# div 태그 중 id가 harmonyContainer인 태그 탐색
container = soup.select('#harmonyContainer')
print(container)
# div태그 중 id가 mArticle 인 태그의 하위 태그 중 아이디가 article_title인 태그
title = soup.select('div#mArticle  div#harmonyContainer')[0]
print(title.get_text())
import re

res = requests.get('http://media.daum.net/economic/')

soup = BeautifulSoup(res.content, 'html.parser')

# a태그이면서 href 속성을 갖는 경우 탐색, 리스트 타입으로 links 변수에 저장됨
links = soup.select('a[href]')

for link in links:
    # print (link) # 스포츠
    # print (link['href']) # http://sports.media.daum.net/sports
    if re.search('http://\w+', link['href']):  # http:// 문자열 이후에 숫자 또는 문자[a-zA-Z0-9_]가 한 개 이상 있는 데이터와 매치됨
        print(link['href'])