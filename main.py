import pandas as pd
import streamlit as st
import plotly.express as px

# CSV 데이터 불러오기
df = pd.read_csv('processed_weather_data.csv', encoding='utf-8-sig')

st.title("📊 지역별 기온 및 강수량 시각화")

# 지역 선택
selected_region = st.selectbox("📍 지역 선택", df['지역'])

# 선택된 지역 필터링
region_data = df[df['지역'] == selected_region]

# 기온 관련 시각화
st.subheader(f"🌡️ {selected_region}의 평균, 최저, 최고 기온")
fig_temp = px.bar(
    region_data.melt(id_vars='지역', value_vars=['평균기온', '최저기온', '최고기온']),
    x='variable', y='value', color='variable',
    labels={'variable': '기온 구분', 'value': '기온(℃)'}
)
st.plotly_chart(fig_temp)

# 강수량 시각화
st.subheader(f"🌧️ {selected_region}의 연간 강수량")
st.metric(label="합계 강수량 (mm)", value=f"{region_data['합계강수량'].values[0]:.1f}")

