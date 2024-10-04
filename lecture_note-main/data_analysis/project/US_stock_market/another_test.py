import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import streamlit as st
from datetime import datetime, timedelta

# 데이터 불러오기 및 날짜 필터링
data = pd.read_csv('./data/AAPL_2024_09_19.csv')
data['Date'] = pd.to_datetime(data['Date'])

# 최근 1년의 데이터로 필터링
one_year_ago = datetime.now() - timedelta(days=365)
data = data[data['Date'] >= one_year_ago]

# RSI 및 MACD 계산 함수 정의
def calculate_rsi(data, window=14):
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

def calculate_macd(data, short_window=12, long_window=26, signal_window=9):
    data['EMA12'] = data['Close'].ewm(span=short_window, adjust=False).mean()
    data['EMA26'] = data['Close'].ewm(span=long_window, adjust=False).mean()
    data['MACD'] = data['EMA12'] - data['EMA26']
    data['MACD_signal'] = data['MACD'].ewm(span=signal_window, adjust=False).mean()
    data['MACD_hist'] = data['MACD'] - data['MACD_signal']
    return data

# RSI 및 MACD 계산
data['RSI_14'] = calculate_rsi(data)
data = calculate_macd(data)

# 최신 값 추출
latest_rsi = data['RSI_14'].iloc[-1]
latest_macd = data['MACD'].iloc[-1]
latest_signal = data['MACD_signal'].iloc[-1]

# Streamlit 화면 시작
st.title("📊 Stock Buy/Sell Recommendation System")

# RSI 차트 시각화
st.write("### RSI 14-day Chart (Last 1 Year)")

plt.figure(figsize=(10, 5))
plt.plot(data['Date'], data['RSI_14'], label='RSI 14-day', color='blue')

# 과매수 및 과매도 라인 (영어로 변경)
plt.axhline(70, color='red', linestyle='--', label='Overbought (70)')
plt.axhline(30, color='green', linestyle='--', label='Oversold (30)')

# X축을 월 단위로 설정
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

# X축 레이블 회전
plt.gcf().autofmt_xdate()

# 제목 및 범례 표시
plt.title('RSI 14-day (Last 1 Year)')
plt.legend()

# Streamlit에서 차트 표시
st.pyplot(plt)

# MACD 차트 시각화
st.write("### MACD Chart (Last 1 Year)")

plt.figure(figsize=(10, 5))
plt.plot(data['Date'], data['MACD'], label='MACD', color='blue')
plt.plot(data['Date'], data['MACD_signal'], label='Signal Line', color='red', linestyle='--')
plt.bar(data['Date'], data['MACD_hist'], label='MACD Histogram', color='gray', width=1)

# X축을 월 단위로 설정
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

# X축 레이블 회전
plt.gcf().autofmt_xdate()

# 제목 및 범례 표시
plt.title('MACD and Signal Line (Last 1 Year)')
plt.legend()

# Streamlit에서 차트 표시
st.pyplot(plt)
