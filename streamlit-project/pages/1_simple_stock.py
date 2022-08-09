import streamlit as st
import pandas as pd
import yfinance as yf

st.write("""
    # Simple Stock Price

    Shown are the stock closing price and volume of Google!!

""")

symbol = "GOOGL"
ticker = yf.Ticker(symbol)

tickerDf = ticker.history(period="max")

st.write(tickerDf)
st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)