import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

# Streamlit 앱 제목
st.title('Stock Price Visualization')

# 유저로부터 티커 입력 받기
ticker_symbol = st.text_input('Enter Stock Ticker', 'AAPL')

# yfinance를 사용해 데이터 불러오기
stock_data = yf.Ticker(ticker_symbol)
hist_data = stock_data.history(period="1y")  # 지난 1년간의 데이터

# 불러온 데이터 보여주기
st.write(f"### {ticker_symbol} Stock Data (Last 1 Year)")
st.dataframe(hist_data)

# 종가(Closing Price) 차트 그리기
st.write(f"### {ticker_symbol} Closing Price Chart")

plt.figure(figsize=(10, 4))
plt.plot(hist_data.index, hist_data['Close'], label='Closing Price')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.title(f'{ticker_symbol} Closing Price (Last 1 Year)')
plt.legend()

st.pyplot(plt)