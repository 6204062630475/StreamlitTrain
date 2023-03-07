import streamlit as st
import pandas as pd
df = pd.read_csv('History.csv')
st.write(df)
st.line_chart(df,x="Count-id",y=["Fish"])