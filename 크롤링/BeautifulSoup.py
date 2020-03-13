# HTML의 태그를 파싱해서 필요한 데이터만 추출하는 함수를 제공하는 라이브러리
import requests
from bs4 import BeautifulSoup

res = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')         # 영화랭킹
html = res.text
soup = BeautifulSoup(html, 'html.parser')                       # BeautifulSoup(HTML데이터, 파싱방법)

for tag in soup.select('div[class=tit3]'):
    print(tag.text.strip())









# -------------------------------------------------------------



import requests
from bs4 import BeautifulSoup

# 1) reqeusts 라이브러리를 활용한 HTML 페이지 요청
# 1-1) res 객체에 HTML 데이터가 저장되고, res.content로 데이터를 추출할 수 있음
res = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')

# print(res.content)
# 2) HTML 페이지 파싱 BeautifulSoup(HTML데이터, 파싱방법)
# 2-1) BeautifulSoup 파싱방법
soup = BeautifulSoup(res.content, 'html.parser')

# 3) 필요한 데이터 검색
title = soup.find_all('div', class_='tit3')

# 4) 필요한 데이터 추출
for i in range(5):
    print(i+1, "위", title[i].get_text().strip())