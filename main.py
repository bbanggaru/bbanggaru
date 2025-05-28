import streamlit as st
import pandas as pd
import plotly.express as px

st.title("빵가루 데이터 시각화 대시보드")

@st.cache_data
def load_data():
    url = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY"
    df = pd.read_csv(url)
    return df

df = load_data()

st.subheader("데이터 미리보기")
st.dataframe(df)

st.subheader("Plotly 시각화")

x_axis = st.selectbox("X축 컬럼 선택", df.columns)
chart_type = st.selectbox("차트 유형 선택", ["Histogram", "Bar", "Line", "Scatter"])

fig = None
if chart_type == "Histogram":
    fig = px.histogram(df, x=x_axis)
elif chart_type == "Bar":
    fig = px.bar(df, x=x_axis)
elif chart_type == "Line":
    fig = px.line(df, x=x_axis)
elif chart_type == "Scatter":
    y_axis = st.selectbox("Y축 컬럼 선택", df.columns)
    fig = px.scatter(df, x=x_axis, y=y_axis)

if fig:
    st.plotly_chart(fig, use_container_width=True)
