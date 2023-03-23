import streamlit as st
import pandas as pd
import numpy as np
import time
import seaborn as sn

st.set_page_config(layout='wide')

st.title('Concise | Your NSE Stock Guide ')
st.subheader('Get Quotes, see historical data. Act smart.')
st.write('You can choose a stock ticker to access the various charts and break down by period')




stocks_data = pd.read_csv("./stocks/data.csv")
option = st.sidebar.selectbox('Choose a Ticker', stocks_data["ticker"].unique())

stocks_data_filtered = stocks_data[stocks_data["ticker"] == option]

st.markdown(stocks_data_filtered.iloc[0]["company"]+"  "+"<strong>$"+stocks_data_filtered.iloc[0]["ticker"]+"</strong>",unsafe_allow_html=True)

st.line_chart(stocks_data_filtered,x="date",y="price",height=400)

