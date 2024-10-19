# 1. curl을 사용하여 TA-Lib 소스 파일을 다운로드
curl -O http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz

# 2. tar 명령어로 압축 해제 (Windows 10 이상에서 가능)
tar -xvzf ta-lib-0.4.0-src.tar.gz

# 3. 디렉토리 이동
cd ta-lib

# 4. Windows에서는 .whl 파일을 이용하여 설치 (빌드 필요 없음)
# 아래 링크에서 .whl 파일 다운로드 (Python 버전과 OS에 맞는 파일 다운로드 필요):
# https://www.lfd.uci.edu/~gohlke/pythonlibs/#ta-lib
# .whl 파일 설치
pip install "C:\path_to_your_downloaded_whl_file\TA_Lib‑0.4.0‑cp311‑cp311‑win_amd64.whl"

# 5. Python에서 talib 라이브러리 임포트 및 함수 출력 테스트
python -c "import talib; print(talib.get_functions())"



# !wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz
# !tar -xzvf ta-lib-0.4.0-src.tar.gz
# %cd ta-lib
# !./configure --prefix=/usr
# !make
# !make install
# !pip install Ta-Lib
# import talib