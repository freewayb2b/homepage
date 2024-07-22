import streamlit as st
import requests as rq
import pandas as pd

#--------------------------------------------------------------------
#page-config

st.set_page_config(layout="wide",page_title="app teste")

link = "https://freewayb2b.shoppub.net/"

tb = rq.get(url=link)

st.table(tb)
