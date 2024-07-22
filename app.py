import streamlit as st
import requests as rq
import pandas as pd



# link = "https://1drv.ms/x/s!Ap1U9e4-CgPGhcZ2MjrIMmz9riJXZQ?e=ZUqqMA=view"
link = 'https://onedrive.live.com/edit.aspx?resid=C6030A3EEEF5549D!90998&cid=c6030a3eeef5549d&CT=1721644678966&OR=ItemsView'

df = rq.get(url=link)

# df = pd.DataFrame(df)

st.table(df)

