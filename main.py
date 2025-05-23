# main.py

import streamlit as st
from link_2025_may_23 import data

# Month options and corresponding data modules
month_options = {
    "June 2025": "link_2025_may_23",
}

# Select a month
selected_month = st.selectbox("選擇月份", list(month_options.keys()))
module_name = month_options[selected_month]

st.title("🎓 YouTube 學習資源")

# Select topic within the chosen month
topic = st.selectbox("選擇你想學的主題", list(data.keys()))

# Show video list
st.subheader(f"【{topic}】相關影片")
for item in data[topic]:
    st.markdown(f"📺 [{item['title']}]({item['url']})")
