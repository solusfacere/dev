import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


# 날짜 형식 변환
data['Date'] = pd.to_datetime(data['Date'])

# 최근 1년 데이터로 필터링
one_year_ago = pd.to_datetime('today') - pd.DateOffset(years=1)
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

# 1. RSI 점수 계산 (점수 범위 -5에서 +5)
if latest_rsi < 30:
    rsi_score = 5  # 강한 매수 신호
elif latest_rsi <= 50:
    rsi_score = 2  # 약한 매수 신호
elif latest_rsi <= 70:
    rsi_score = 0  # 중립
else:
    rsi_score = -5  # 강한 매도 신호

# 2. MACD 점수 계산 (점수 범위 -5에서 +5)
macd_score = 0
if latest_macd > 0:
    macd_score += 3  # 상승 추세
else:
    macd_score -= 3  # 하락 추세

if latest_macd > latest_signal:
    macd_score += 2  # MACD 상향 돌파 -> 매수 신호
else:
    macd_score -= 2  # MACD 하향 돌파 -> 매도 신호

# 3. 최종 점수 합산 (-10 ~ +10)
final_score = rsi_score + macd_score

# Streamlit 화면 시작
st.title("📊 주식 매수/매도 추천 및 청산 타이밍 시스템")

# 차트 시각화
st.write("### RSI 및 MACD 차트")

# RSI 차트 시각화
plt.figure(figsize=(10, 4))
plt.plot(data['Date'], data['RSI_14'], label='RSI 14-day', color='green')
plt.axhline(70, color='red', linestyle='--', label='과매수 (70)')
plt.axhline(30, color='blue', linestyle='--', label='과매도 (30)')
plt.title('RSI 14-day')
plt.legend()
st.pyplot(plt)

# MACD 차트 시각화
plt.figure(figsize=(10, 4))
plt.plot(data['Date'], data['MACD'], label='MACD', color='blue')
plt.plot(data['Date'], data['MACD_signal'], label='Signal Line', color='red', linestyle='--')
plt.bar(data['Date'], data['MACD_hist'], label='MACD Histogram', color='gray', width=1)
plt.title('MACD 및 시그널 라인')
plt.legend()
st.pyplot(plt)

# 최종 점수 및 매수/매도 추천 표시
st.write("### 매수/매도 추천 및 점수 상세 내역")

# 4. 최종 점수에 따른 매매 신호 출력
if final_score >= 6:
    st.success("강력한 **매수** 신호입니다.")
elif final_score <= -6:
    st.error("강력한 **매도** 신호입니다.")
else:
    st.info("현재는 **중립** 상태입니다. 신중한 의사결정이 필요합니다.")

# 점수 상세 내역 출력
st.write(f"**RSI 점수**: {rsi_score} (현재 RSI: {latest_rsi:.2f})")
st.write(f"**MACD 점수**: {macd_score} (현재 MACD: {latest_macd:.4f}, 시그널 라인: {latest_signal:.4f})")
st.write(f"**최종 점수**: {final_score}")

# 청산 타이밍 결정
st.write("### 청산 타이밍 및 근거")
if latest_macd < latest_signal:
    st.warning(f"**MACD가 시그널 라인을 하향 돌파**했습니다. 청산 고려 필요.")
    st.write(f"MACD 값: {latest_macd:.4f}, 시그널 라인 값: {latest_signal:.4f}")
elif latest_rsi > 70:
    st.warning(f"**RSI가 70을 초과하여 과매수 상태**입니다. 청산 고려 필요.")
    st.write(f"현재 RSI 값: {latest_rsi:.2f}")
else:
    st.success("현재 청산 필요성이 낮습니다.")
    st.write("현재 MACD와 시그널 라인 간 차이 및 RSI 상태는 청산 필요성이 없음을 시사합니다.")

# 지표 설명
st.write("#### 지표 설명")
st.write("""
- **RSI (Relative Strength Index)**: 주식의 과매수 또는 과매도 상태를 나타냅니다. 30 이하일 때는 과매도, 70 이상일 때는 과매수로 간주됩니다.
- **MACD (Moving Average Convergence Divergence)**: 단기 이동 평균과 장기 이동 평균의 차이로, 주가 추세의 변화를 파악하는 데 사용됩니다.
- **청산 타이밍**: MACD가 시그널 라인을 하향 돌파하거나 RSI가 70 이상일 때는 청산 타이밍을 고려합니다.
""")
