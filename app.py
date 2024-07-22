import streamlit as st
import requests as rq
import pandas as pd



link = "https://1drv.ms/x/s!Ap1U9e4-CgPGhcZ2MjrIMmz9riJXZQ?e=ZUqqMA"


df = rq.get(url=link)

df = pd.DataFrame(df)

st.table(df)

