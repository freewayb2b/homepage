import streamlit as st
import requests as rq
import pandas as pd



link = 'https://1drv.ms/x/s!Ap1U9e4-CgPGhcZ2MjrIMmz9riJXZQ'
link2 = 'https://1drv.ms/x/s!Ap1U9e4-CgPGhcZ2MjrIMmz9riJXZQ?view=1'

df = rq.get(url=link2)

# df = pd.read_excel(link2)

st.table(df)

