import streamlit as st
import pandas as pd
import yfinance as yf

st.write("""
Simple Stock Price App
""")

ticker = 'GOOG'
tickerData = yf.Ticker(ticker)
tickerDf = tickerData.history(period='1d', start='2023-01-01', end='2023-04-05')
st.line_chart(tickerDf.close)
st.line_chart(tickerDf.Volume)
