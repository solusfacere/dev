import os  # os 모듈을 import하여 파일 탐색 기능 사용
import streamlit as st
from dataloader import TickerLoader  # 데이터 로더 클래스
from model import Model  # 인사이트 도출을 위한 모델 클래스

# 세션 상태에서 ticker 값을 False로 초기화
st.session_state["ticker"] = False

# 제목을 표시
st.write("# 📈Nasdaq Stock Market DashBoard")

# 추천 티커 목록 정의 (미리 정의된 인기 티커들)
recommended_tickers = ['AAPL', 'GOOGL', 'TSLA', 'NVDA', 'AMZN']

st.session_state["ticker"] = st.text_input("ticker input", "AAPL")
 
# 사용자가 ticker를 입력한 경우 실행
if st.session_state["ticker"]:
    # 데이터 로더 객체 생성 및 데이터 로드
    tl = TickerLoader()
    data = tl.get_data(min_days=2500, streamlit_tqdm=True)  # 최소 2500일 이상의 데이터 로드
    
    # 선택한 티커에 해당하는 데이터 필터링
    chart_data = data.query(f"ticker == '{st.session_state['ticker']}'")

    # 지표 (Indicator) 섹션 표시
    st.write("### Indicator")
    
    # 사용될 보조 지표들 정의
    indi_cols = ["SMA_20", "SMA_200", "RSI_14", "MACD", "MACD_signal"]
      
    # 차트 (Chart) 섹션 표시
    st.write("### Chart")
    
    # 126일 동안의 High, Low, SMA_20, SMA_100 데이터를 시각화
    st.line_chart(chart_data[["High", "Low", "SMA_20", "SMA_100"]].iloc[-126:])
    
    # 구분선
    st.write("---")
    
    # 인사이트 (Insight) 섹션 표시
    st.write("### Insight")
    
    # 모델을 사용하여 인사이트를 도출
    with st.spinner("Thinking... plz wait"):
        insight = Model(chart_data).get_insight()
        st.write(insight)
    
    # **추천 이유** 섹션 추가
    st.write("---")
    st.write("### Why we recommend this ticker")
    
    # 각 티커에 대한 간단한 추천 이유 추가
    if selected_ticker == 'AAPL':
        st.write("Apple Inc. (AAPL)는 안정적인 기술 지표를 유지하고 있으며, 최근 강한 상승세를 보이고 있어 매수 추천을 드립니다.")
    elif selected_ticker == 'GOOGL':
        st.write("Alphabet Inc. (GOOGL)는 검색 시장 점유율이 높은 안정적인 기업으로, 기술 지표상 장기 상승 가능성이 높습니다.")
    elif selected_ticker == 'TSLA':
        st.write("Tesla Inc. (TSLA)는 전기차 시장의 리더로, 최근의 하락세에도 불구하고 장기적인 성장 잠재력을 보유하고 있습니다.")
    elif selected_ticker == 'NVDA':
        st.write("NVIDIA Corp. (NVDA)는 AI 및 반도체 산업의 선두주자로, 기술적 지표가 강세를 보이고 있어 매수 추천을 드립니다.")
    elif selected_ticker == 'AMZN':
        st.write("Amazon.com, Inc. (AMZN)는 전자상거래 및 클라우드 서비스 분야에서 강력한 시장 지위를 유지하고 있어 장기적으로 긍정적인 평가를 받고 있습니다.")

