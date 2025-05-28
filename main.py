streamlit
pandas
plotly

import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Plotly 시각화 대시보드")

@st.cache_data
def load_data():
    url = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY"
    df = pd.read_csv(url)
    return df

df = load_data()
st.dataframe(df)

fig = px.histogram(df, x=df.columns[0])
st.plotly_chart(fig)
