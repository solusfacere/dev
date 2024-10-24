import requests
from bs4 import BeautifulSoup
import pandas as pd
from yahoo_fin import stock_info as si

def get_nasdaq_top5_market_cap():
    # Step 1: Get NASDAQ ticker symbols using yahoo_fin
    nasdaq_tickers = si.tickers_nasdaq()
    
    # Step 2: Fetch market cap for each ticker and store the results
    market_caps = []
    for ticker in nasdaq_tickers[:50]:  # Limit to first 50 tickers to avoid request limitations
        try:
            data = si.get_quote_table(ticker)
            market_cap = data.get("Market Cap")
            market_caps.append((ticker, market_cap))
        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")

    # Step 3: Sort by market cap to get top 5 companies
    def parse_market_cap(market_cap_str):
        if market_cap_str.endswith('T'):
            return float(market_cap_str[:-1]) * 1e12
        elif market_cap_str.endswith('B'):
            return float(market_cap_str[:-1]) * 1e9
        elif market_cap_str.endswith('M'):
            return float(market_cap_str[:-1]) * 1e6
        return 0
    
    sorted_market_caps = sorted(market_caps, key=lambda x: parse_market_cap(x[1]), reverse=True)
    top_5 = sorted_market_caps[:5]
    
    # Step 4: Display the results
    for rank, (ticker, market_cap) in enumerate(top_5, start=1):
        print(f"{rank}. {ticker}: {market_cap}")

# Run the function to get the top 5 NASDAQ companies by market cap
get_nasdaq_top5_market_cap()
