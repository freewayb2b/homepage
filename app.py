import streamlit as st
import requests as rq
import pandas as pd



# link = "https://1drv.ms/x/s!Ap1U9e4-CgPGhcZ2MjrIMmz9riJXZQ?e=ZUqqMA=view"
link = 'https://1drv.ms/x/s!Ap1U9e4-CgPGhcZ2MjrIMmz9riJXZQ'

# df = rq.get(url=link,data='id="Sheet0_0_0_1"')

df = pd.read_excel(link)

st.table(df)

