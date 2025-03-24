# main.py

import streamlit as st
from link import data

st.title("🎓 YouTube 學習資源")

# 選擇主題
topic = st.selectbox("選擇你想學的主題", list(data.keys()))

# 顯示影片清單
st.subheader(f"【{topic}】相關影片")

for item in data[topic]:
    st.markdown(f"📺 [{item['title']}]({item['url']})")
