import yfinance as yf
import streamlit as st

st.write("""

# Simple **Stock Price App**
Shown are the stock closing price and volume of Google INC.
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = 'GOOGL'

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)


#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)


st.write("""

### Major share holders

""")
# show major holders
tickerData.major_holders


st.write("""

### Major institutional holders

""")
# show institutional holders
tickerData.institutional_holders

st.write("""
### Recomendations to invest 
""")
#get recommendation data for ticker
tickerData.recommendations