import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# CSV 파일 로드
data = pd.read_csv('./data/AAPL_2024_09_19.csv')

# 날짜 형식 변환
data['Date'] = pd.to_datetime(data['Date'])

# 최근 1년 데이터로 필터링
one_year_ago = pd.to_datetime('today') - pd.DateOffset(years=1)
data = data[data['Date'] >= one_year_ago]

# RSI와 MACD 계산 함수 정의
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

# RSI와 MACD 계산
data['RSI_14'] = calculate_rsi(data)
data = calculate_macd(data)

# 차트 시각화
st.write("### RSI 및 MACD 분석")

# RSI 차트
plt.figure(figsize=(10, 4))
plt.plot(data['Date'], data['RSI_14'], label='RSI 14-day', color='green')
plt.axhline(70, color='red', linestyle='--', label='과매수 (70)')
plt.axhline(30, color='blue', linestyle='--', label='과매도 (30)')
plt.title('RSI 14-day')
plt.legend()
st.pyplot(plt)

# MACD 차트
plt.figure(figsize=(10, 4))
plt.plot(data['Date'], data['MACD'], label='MACD', color='blue')
plt.plot(data['Date'], data['MACD_signal'], label='Signal Line', color='red', linestyle='--')
plt.bar(data['Date'], data['MACD_hist'], label='MACD Histogram', color='gray', width=1)
plt.title('MACD 및 시그널 라인')
plt.legend()
st.pyplot(plt)

# RSI 및 MACD 상태 분석
st.write("### 매매 신호 분석")

macd_current = data['MACD'].iloc[-1]
signal_current = data['MACD_signal'].iloc[-1]
rsi_current = data['RSI_14'].iloc[-1]

if macd_current > signal_current and rsi_current < 30:
    st.success("매수 신호: MACD가 시그널 라인 위에 있고 RSI가 과매도 상태입니다.")
elif macd_current < signal_current and rsi_current > 70:
    st.warning("매도 신호: MACD가 시그널 라인을 하향 돌파하고 RSI가 과매수 상태입니다.")
else:
    st.info("추세가 안정적인 상태입니다.")
