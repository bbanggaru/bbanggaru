
import streamlit as st
import pandas as pd
import pydeck as pdk

st.title("배달 위치 시각화")

@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/bbanggaru/bbanggaru/refs/heads/main/delivery_data.csv"
    return pd.read_csv(url)

df = load_data()

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

