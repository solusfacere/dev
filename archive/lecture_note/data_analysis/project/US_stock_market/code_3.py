import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from datetime import datetime, timedelta

selected_ticker = st.text_input("분석할 종목 티커를 입력하세요", value='AAPL')
data = pd.read_csv(f'./data/{selected_ticker}_2024_09_19.csv')


# 날짜 형식 변환 및 RSI 값이 있는 행 필터링
data['Date'] = pd.to_datetime(data['Date'])
 
# start_date = st.date_input('시작 날짜', value=datetime.now() - timedelta(days=365))
# end_date = st.date_input('종료 날짜', value='2024/09/19')

# 종료 날짜와 시작 날짜 입력
start_date = st.date_input('시작 날짜', value=datetime(2023, 9, 19)).strftime('%Y-%m-%d')
end_date = st.date_input('종료 날짜', value=datetime(2024, 9, 19)).strftime('%Y-%m-%d')

# CSV 파일 로드
data = pd.read_csv('./data/AAPL_2024_09_19.csv')

# 날짜 형식 변환
data['Date'] = pd.to_datetime(data['Date']).dt.strftime('%Y-%m-%d')

# 데이터 필터링: 날짜 비교를 위한 형식 일치
data = data[(data['Date'] >= start_date) & (data['Date'] <= end_date)]


# # 최근 1년의 데이터로 필터링
# one_year_ago = datetime.now() - timedelta(days=365)
# data = data[data['Date'] >= one_year_ago]

rsi_data = data[['Date', 'RSI_14']].dropna()

# Streamlit 대시보드 시작
st.title("📊 RSI 분석 대시보드")

# 1. 기본 설명 섹션
st.write("""
### RSI 분석 (Relative Strength Index)
RSI는 주식의 과매수 또는 과매도 상태를 나타내는 지표로, 일반적으로 14일 이동 평균을 기반으로 계산됩니다.

- **RSI 값이 70 이상**: 과매수 상태로, 가격이 너무 빠르게 상승했을 가능성이 있으며 조정 가능성이 있습니다.
- **RSI 값이 30 이하**: 과매도 상태로, 가격이 과도하게 하락해 반등할 가능성이 있습니다.
""")

# 2. RSI 차트 시각화
st.write("### RSI 14일 차트")

# RSI 시각화
plt.figure(figsize=(10, 5))
plt.plot(rsi_data['Date'], rsi_data['RSI_14'], label='RSI 14')
plt.axhline(70, color='red', linestyle='--', label='과매수 (70)')
plt.axhline(30, color='green', linestyle='--', label='과매도 (30)')
plt.title('RSI 14-day')
plt.legend()

# Streamlit에서 차트 표시
st.pyplot(plt)

# 3. 현재 상태 알림
current_rsi = rsi_data['RSI_14'].iloc[-1]
if current_rsi > 70:
    st.warning(f"현재 RSI는 {current_rsi}로 과매수 상태입니다. 주가 조정 가능성이 있습니다.")
elif current_rsi < 30:
    st.info(f"현재 RSI는 {current_rsi}로 과매도 상태입니다. 반등 가능성이 있습니다.")
else:
    st.success(f"현재 RSI는 {current_rsi}로 안정적인 상태입니다.")

# 4. 추가 분석 데이터 섹션
st.write("### 추가 분석")
st.write(f"RSI 14일 기준으로 주식의 마지막 수치는 {current_rsi}입니다. 과매수 및 과매도 상태를 주의하며 투자 결정을 내리세요.")



# MACD 계산 함수
def calculate_macd(data, short_window=12, long_window=26, signal_window=9):
    data['EMA12'] = data['Close'].ewm(span=short_window, adjust=False).mean()
    data['EMA26'] = data['Close'].ewm(span=long_window, adjust=False).mean()
    data['MACD'] = data['EMA12'] - data['EMA26']
    data['MACD_signal'] = data['MACD'].ewm(span=signal_window, adjust=False).mean()
    data['MACD_hist'] = data['MACD'] - data['MACD_signal']
    return data

# MACD 지표 계산
data = calculate_macd(data)

# Streamlit UI 시작
st.title("📊 MACD 분석 차트")

# 1. MACD 차트 시각화
st.write("### MACD 차트 (최근 1년)")

# MACD와 시그널 라인을 시각화
plt.figure(figsize=(10, 5))
plt.plot(data['Date'], data['MACD'], label='MACD', color='blue')
plt.plot(data['Date'], data['MACD_signal'], label='Signal Line', color='red', linestyle='--')
plt.bar(data['Date'], data['MACD_hist'], label='MACD Histogram', color='gray', width=1)
plt.title('MACD와 시그널 라인')
plt.legend()

# Streamlit에 MACD 차트 표시
st.pyplot(plt)

# 2. 최근 값으로 매도 신호 계산 및 수치 근거 표시
macd_current = data['MACD'].iloc[-1]
signal_current = data['MACD_signal'].iloc[-1]
date_current = data['Date'].iloc[-1]

# 매도 신호 발생 여부와 수치적 근거 표시
st.write("### 매도 타이밍 근거")
if macd_current < signal_current:
    st.warning(f"**매도 신호 발생**: {date_current}에 MACD가 시그널 라인을 하향 돌파했습니다.")
    st.write(f"현재 MACD 값: {macd_current:.4f}")
    st.write(f"현재 시그널 라인 값: {signal_current:.4f}")
    st.write("하락 추세 전환 가능성이 있으므로 매도 신호로 해석할 수 있습니다.")
else:
    st.success(f"**매도 신호 없음**: {date_current}에 MACD가 시그널 라인 위에 있습니다.")
    st.write(f"현재 MACD 값: {macd_current:.4f}")
    st.write(f"현재 시그널 라인 값: {signal_current:.4f}")
    st.write("하락 추세가 나타나지 않았으므로 매도 신호가 없습니다.")


# MACD 계산 함수
def calculate_macd(data, short_window=12, long_window=26, signal_window=9):
    # 단기 지수 이동 평균 (EMA12)
    data['EMA12'] = data['Close'].ewm(span=short_window, adjust=False).mean()
    
    # 장기 지수 이동 평균 (EMA26)
    data['EMA26'] = data['Close'].ewm(span=long_window, adjust=False).mean()
    
    # MACD 라인: EMA12 - EMA26
    data['MACD'] = data['EMA12'] - data['EMA26']
    
    # 시그널 라인: MACD의 9일 지수 이동 평균
    data['MACD_signal'] = data['MACD'].ewm(span=signal_window, adjust=False).mean()
    
    # MACD 히스토그램: MACD - 시그널 라인
    data['MACD_hist'] = data['MACD'] - data['MACD_signal']
    
    return data

# MACD 계산
data = calculate_macd(data)

# Streamlit UI 구성
st.title("📈 MACD 계산 및 값 확인")

# 1. 기본 설명 섹션
st.write("""
### MACD 계산 과정
MACD는 주가의 단기 이동 평균(12일)과 장기 이동 평균(26일) 간의 차이로 계산됩니다. 
또한, MACD 값의 9일 이동 평균을 시그널 라인으로 사용하며, 
이 두 값의 차이는 MACD 히스토그램으로 나타납니다.
""")

# 2. 계산된 값 표시 (최근 값들)
st.write("### 최근 계산된 값")
latest = data.tail(1)
st.write(f"**EMA12 (단기 이동평균)**: {latest['EMA12'].values[0]:.4f}")
st.write(f"**EMA26 (장기 이동평균)**: {latest['EMA26'].values[0]:.4f}")
st.write(f"**MACD 값**: {latest['MACD'].values[0]:.4f}")
st.write(f"**시그널 라인 값**: {latest['MACD_signal'].values[0]:.4f}")
st.write(f"**MACD 히스토그램**: {latest['MACD_hist'].values[0]:.4f}")