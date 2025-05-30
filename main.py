import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
import pydeck as pdk

st.title("배달 위치 군집 분석")

@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/bbanggaru/bbanggaru/refs/heads/main/delivery_data.csv"  # 여기에 raw URL 넣기
    return pd.read_csv(url)

df = load_data()

# 좌표 정보만 추출해서 클러스터링
coords = df[['Latitude', 'Longitude']]

# 군집 수 조절 가능
num_clusters = st.slider("군집 수 (K)", 1, 10, 3)

kmeans = KMeans(n_clusters=num_clusters, random_state=42)
df['Cluster'] = kmeans.fit_predict(coords)

# 색상 매핑 (군집별)
color_map = [
    [255, 0, 0], [0, 255, 0], [0, 0, 255],
    [255, 255, 0], [255, 0, 255], [0, 255, 255],
    [100, 100, 100], [200, 100, 0], [100, 0, 200], [50, 150, 50]
]
df['Color'] = df['Cluster'].apply(lambda x: color_map[x % len(color_map)])

st.subheader("군집별 배달 위치 지도")

st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/light-v9',
    initial_view_state=pdk.ViewState(
        latitude=df['Latitude'].mean(),
        longitude=df['Longitude'].mean(),
        zoom=11,
        pitch=45,
    ),
    layers=[
        pdk.Layer(
            'ScatterplotLayer',
            data=df,
            get_position='[Longitude, Latitude]',
            get_fill_color='Color',
            get_radius=100,
            pickable=True
        ),
    ],
))

# 데이터프레임도 같이 출력
st.subheader("클러스터가 추가된 데이터")
st.dataframe(df)

