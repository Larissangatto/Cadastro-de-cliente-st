import streamlit as st 
from utils.csv_handler import read_csv


st.title("Customer Search")
st.divider()
df=read_csv()
st.dataframe(df)