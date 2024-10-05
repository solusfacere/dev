import pandas as pd
import plotly.graph_objs as go
import streamlit as st
from datetime import datetime, timedelta

# 데이터 불러오기
data = pd.read_csv('./data/AAPL_2024_09_19.csv')
data['Date'] = pd.to_datetime(data['Date'])

# 최근 1년의 데이터로 필터링
one_year_ago = datetime.now() - timedelta(days=365)
data = data[data['Date'] >= one_year_ago]

# RSI 계산 함수 정의
def calculate_rsi(data, window=14):
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

# MACD 계산 함수 정의
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

# Streamlit 화면 시작
st.title("📊 Interactive Stock Candlestick Chart with RSI, Volume, and MACD")

# 캔들스틱 차트
fig = go.Figure()

# 캔들스틱 추가
fig.add_trace(go.Candlestick(x=data['Date'],
                             open=data['Open'],
                             high=data['High'],
                             low=data['Low'],
                             close=data['Close'],
                             name='Candlestick'))

# 이동평균선 (20일, 50일) 추가
fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'].rolling(window=20).mean(),
                         mode='lines', name='20-day MA', line=dict(color='blue')))
fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'].rolling(window=50).mean(),
                         mode='lines', name='50-day MA', line=dict(color='orange')))

# 레이아웃 설정 (줌, 팬 등)
fig.update_layout(title='Candlestick Chart with Moving Averages',
                  xaxis_title='Date', yaxis_title='Price',
                  xaxis_rangeslider_visible=False)

# RSI 차트 추가
fig.add_trace(go.Scatter(x=data['Date'], y=data['RSI_14'],
                         mode='lines', name='RSI 14-day', yaxis='y2', line=dict(color='purple')))

# 거래량 차트 추가
fig.add_trace(go.Bar(x=data['Date'], y=data['Volume'], name='Volume', yaxis='y3', opacity=0.4))

# MACD 차트 추가
fig.add_trace(go.Scatter(x=data['Date'], y=data['MACD'], mode='lines', name='MACD', yaxis='y4', line=dict(color='blue')))
fig.add_trace(go.Scatter(x=data['Date'], y=data['MACD_signal'], mode='lines', name='Signal Line', yaxis='y4', line=dict(color='red')))
fig.add_trace(go.Bar(x=data['Date'], y=data['MACD_hist'], name='MACD Histogram', yaxis='y4', marker_color='gray', opacity=0.4))

# 보조축 설정 (RSI, 거래량, MACD)
fig.update_layout(
    yaxis2=dict(title='RSI', overlaying='y', side='right', position=0.85, range=[0, 100]),
    yaxis3=dict(title='Volume', overlaying='y', side='right', position=0.95),
    yaxis4=dict(title='MACD', overlaying='y', side='right', position=0.75)
)

# Streamlit에서 차트 표시
st.plotly_chart(fig)
