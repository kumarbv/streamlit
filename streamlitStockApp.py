# import streamlit as st
# import pandas as pd
# import yfinance as yf
# import numpy as np

# st.title("Performance of Stocks")

# myStocks = ['DRREDDY.NS','BIOCON.NS' ,'AXISBANK.NS', 'HDFCBANK.NS', 'HDFCLIFE.NS', 'ICICIBANK.NS', 'YESBANK.NS', 'ACC.NS', 'LT.NS', 'COLPAL.NS', 'DABUR.NS', 'ITC.NS', 'TATACONSUM.NS', 'INFY.NS', 'KPITTECH.NS', 'LTIM.NS',  'SONATSOFTW.NS', 'TCS.NS', 'AUROPHARMA.NS', 'CIPLA.NS', 'JBCHEPHARM.NS', 'PFIZER.NS', 'SUNPHARMA.NS', 'TORNTPHARM.NS', 'BPCL.NS', 'HINDPETRO.NS']
# tickers = myStocks

# # Download the data for each stock and store it in a dictionary
# data = {}
# start="2023-01-05"
# end="2023-04-05"

# for ticker in tickers:
#     data[ticker] = yf.download(ticker, start=start, end=end)

# # Extract the adjusted close prices for each stock and combine them into a single dataframe
# adj_close = pd.DataFrame()
# for ticker in tickers:
#     adj_close[ticker] = data[ticker]["Adj Close"]

# # Calculate the overall returns for each stock
# overall_returns = adj_close.iloc[-1] / adj_close.iloc[0] - 1

# # Sort the stocks based on their overall returns
# sorted_returns = overall_returns.sort_values(ascending=False)

# # Plot the overall returns for each stock
# #plt.bar(sorted_returns.index, sorted_returns.values)
# # df = pd.DataFrame(sorted_returns.index,sorted_returns.values)
# data = {"Stocks":sorted_returns.index.to_numpy(), "Values": sorted_returns.values}
# data = pd.DataFrame(data)
# data = data.set_index("Stocks")
# st.bar_chart(data)

# # Print the overall returns for each stock
# st.write("Overall Returns ({} - {}):".format(start, end))
# for ticker in sorted_returns.index:
#     st.write("{}: {:.2f}%".format(ticker, overall_returns[ticker] * 100))

import yfinance as yf
import pandas as pd
import streamlit as st
import plotly.express as px

# Set page title
st.set_page_config(page_title='Stock Analysis App')

# Set page header
st.header('Stock Analysis App')

# Create date range selector
start_date = st.date_input('Start date', value=pd.to_datetime('2021-01-01'))
end_date = st.date_input('End date', value=pd.to_datetime('2022-01-01'))

# Create stock ticker input
tickers = st.text_input('Enter stock tickers (comma-separated)', value='AAPL, GOOG, MSFT').upper().split(',')

# Fetch stock data from Yahoo Finance API
stock_data = yf.download(tickers, start=start_date, end=end_date, group_by='ticker')

# Calculate percent change in stock prices
pct_change = stock_data['Adj Close'].pct_change()

# Create bar chart of percent change in stock prices
fig = px.bar(pct_change.reset_index(), x='Date', y='Adj Close', color='ticker', barmode='group')

# Display bar chart
st.plotly_chart(fig)

# Create data table of percent change in stock prices
table_data = pd.concat([stock_data['Adj Close'].iloc[[0,-1]], (pct_change+1).prod()-1], axis=1)
table_data.columns = ['Start', 'End', '% Change']
st.write(table_data.style.format("{:.2%}"))
