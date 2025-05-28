# app.py
import streamlit as st
import pandas as pd
import plotly.express as px

# 페이지 설정
st.set_page_config(
    page_title="Plotly 시각화 예제",
    page_icon="📊",
    layout="wide"
)

st.title("데이터 시각화 대시보드")

@st.cache_data
def load_data():
    # Google Drive 다운로드 URL
    url = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY"
    df = pd.read_csv(url)
    return df

df = load_data()
st.subheader("원본 데이터 미리보기")
st.dataframe(df.head())

# 사이드바: 시각화 옵션
st.sidebar.header("시각화 설정")
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
all_cols = df.columns.tolist()

# 1) Scatter Plot
st.sidebar.subheader("Scatter Plot")
x_col = st.sidebar.selectbox("X축 선택", numeric_cols, index=0)
y_col = st.sidebar.selectbox("Y축 선택", numeric_cols, index=1)
color_col = st.sidebar.selectbox("색상(카테고리) 선택", [None] + all_cols)

st.subheader("Scatter Plot")
fig_scatter = px.scatter(
    df,
    x=x_col,
    y=y_col,
    color=color_col if color_col else None,
    title=f"{x_col} vs {y_col}"
)
st.plotly_chart(fig_scatter, use_container_width=True)

# 2) Histogram
st.sidebar.subheader("Histogram")
hist_col = st.sidebar.selectbox("히스토그램 변수", numeric_cols, index=0)
bins = st.sidebar.slider("빈 개수", min_value=5, max_value=100, value=30)

st.subheader("Histogram")
fig_hist = px.histogram(
    df,
    x=hist_col,
    nbins=bins,
    title=f"{hist_col} 분포도"
)
st.plotly_chart(fig_hist, use_container_width=True)

# 3) Bar Chart (카테고리별 집계)
st.sidebar.subheader("Bar Chart")
cat_col = st.sidebar.selectbox("카테고리 변수", all_cols, index=0)
agg_col = st.sidebar.selectbox("집계할 수치 변수", numeric_cols, index=0)
agg_func = st.sidebar.selectbox("집계 함수", ["sum", "mean", "count"], index=1)

st.subheader("Bar Chart")
if agg_func == "count":
    df_bar = df.groupby(cat_col).size().reset_index(name="count")
    fig_bar = px.bar(df_bar, x=cat_col, y="count", title=f"{cat_col}별 개수")
else:
    df_bar = df.groupby(cat_col)[agg_col].agg(agg_func).reset_index()
    fig_bar = px.bar(df_bar, x=cat_col, y=agg_col, title=f"{cat_col}별 {agg_col}의 {agg_func}")

st.plotly_chart(fig_bar, use_container_width=True)
