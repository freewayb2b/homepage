import streamlit as st
import requests as rq
import pandas as pd



link = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQAP3t48A4W5Afz-GJ7Jk7-uu7k7zVwIBB5CvuT_OIgooLFg9I0S9nmWYCkq3SwBQ/pub?gid=436659431&single=true&output=csv'


df = pd.read_excel(link)

st.table(df)

