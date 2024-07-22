import streamlit as st
import requests as rq
import pandas as pd
from bs4 import BeautifulSoup

#--------------------------------------------------------------------
#page-config

st.set_page_config(layout="wide",page_title="app teste")

link = "https://freewayb2b.shoppub.net/"

response = requests.get(link)

tb = BeautifulSoup(response.text, 'html.parser')



st.table(tb)
