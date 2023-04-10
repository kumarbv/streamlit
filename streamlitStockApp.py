import streamlit as st
import pandas as pd
import yfinance as yf
import numpy as np

st.title("Performance of Stocks")

myStocks = ['DRREDDY.NS','BIOCON.NS' ,'AXISBANK.NS', 'HDFCBANK.NS', 'HDFCLIFE.NS', 'ICICIBANK.NS', 'YESBANK.NS', 'ACC.NS', 'LT.NS', 'COLPAL.NS', 'DABUR.NS', 'ITC.NS', 'TATACONSUM.NS', 'INFY.NS', 'KPITTECH.NS', 'LTIM.NS',  'SONATSOFTW.NS', 'TCS.NS', 'AUROPHARMA.NS', 'CIPLA.NS', 'JBCHEPHARM.NS', 'PFIZER.NS', 'SUNPHARMA.NS', 'TORNTPHARM.NS', 'BPCL.NS', 'HINDPETRO.NS']
tickers = myStocks

# Download the data for each stock and store it in a dictionary
data = {}
start="2023-01-05"
end="2023-04-05"

for ticker in tickers:
    data[ticker] = yf.download(ticker, start=start, end=end)

# Extract the adjusted close prices for each stock and combine them into a single dataframe
adj_close = pd.DataFrame()
for ticker in tickers:
    adj_close[ticker] = data[ticker]["Adj Close"]

# Calculate the overall returns for each stock
overall_returns = adj_close.iloc[-1] / adj_close.iloc[0] - 1

# Sort the stocks based on their overall returns
sorted_returns = overall_returns.sort_values(ascending=False)

# Plot the overall returns for each stock
#plt.bar(sorted_returns.index, sorted_returns.values)
# df = pd.DataFrame(sorted_returns.index,sorted_returns.values)
# my_list = [1, 2, 3, 4, 5]
# my_new_list = [i * 5 for i in my_list]

data = {"Stocks":sorted_returns.index.to_numpy(), "Values": sorted_returns.values*100}
data = pd.DataFrame(data)
st.dataframe(data)
data = data.set_index(data[0])
st.bar_chart(data)

# Print the overall returns for each stock
st.write("Overall Returns ({} - {}):".format(start, end))
for ticker in sorted_returns.index:
    st.write("{}: {:.2f}%".format(ticker, overall_returns[ticker] * 100))
