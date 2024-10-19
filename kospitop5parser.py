import requests
from bs4 import BeautifulSoup
import pandas as pd

# 네이버 금융 KOSPI 시총 상위 종목 페이지 URL
url = "https://finance.naver.com/sise/sise_market_sum.naver?sosok=0"

# 웹 페이지 요청 및 파싱
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 종목명과 티커 정보를 담을 리스트
tickers = []

# 시총 상위 종목 테이블 추출
table = soup.find('table', {'class': 'type_2'})

# 테이블의 행들을 반복하며 상위 5개 종목의 정보를 가져옴
for row in table.find_all('tr')[2:7]:  # 첫 2개는 헤더 행, 그 다음 5개 추출
    cells = row.find_all('td')
    if len(cells) > 1:
        name = cells[1].text.strip()
        tickers.append(name)

print("KOSPI 시가총액 상위 5개 종목:")
print(tickers)
