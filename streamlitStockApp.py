import streamlit as st
import pandas as pd
import yfinance as yf

st.title("Simple Google Price App")

ticker = 'GOOG'
tickerData = yf.Ticker(ticker)
tickerDf = tickerData.history(period='1d', start='2023-01-01', end='2023-04-05')
st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
