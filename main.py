url="https://raw.githubusercontent.com/bbanggaru/bbanggaru/refs/heads/main/delivery_data.csv"
import streamlit as st
import pandas as pd
import pydeck as pdk

# 제목
st.title("배달 위치 시각화")

# 데이터 불러오기
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/사용자이름/저장소이름/main/Delivery%20-%20Delivery.csv"
    return pd.read_csv(url)

df = load_data()

# 지도 시각화
st.subheader("배달 위치 지도")
st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/streets-v11',
    initial_view_state=pdk.ViewState(
        latitude=df['Latitude'].mean(),
        longitude=df['Longitude'].mean(),
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
            'ScatterplotLayer',
            data=df,
            get_position='[Longitude, Latitude]',
            get_color='[200, 30, 0, 160]',
            get_radius=100,
        ),
    ],
))
