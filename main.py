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
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import streamlit as st
import pandas as pd

# CSV 로드 (전처리된 파일 불러오기)
df = pd.read_csv('processed_weather_data.csv')

# 지역 라벨 인코딩 (필수: 머신러닝은 문자열을 처리 못함)
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['지역_encoded'] = le.fit_transform(df['지역'])

# 입력값(X)와 예측대상(y) 나누기
X = df[['평균기온', '최저기온', '최고기온', '합계강수량']]
y = df['지역_encoded']

# 학습/테스트 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 모델 훈련
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 예측 및 정확도
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# 결과 출력
st.subheader("📊 머신러닝으로 지역 예측")
st.write(f"랜덤포레스트 분류기 정확도: **{accuracy*100:.2f}%**")

# 사용자 입력을 받아 예측도 가능하게 할 수 있음 (선택사항)
st.markdown("### 🔍 기온과 강수량으로 지역 예측 테스트")
avg_temp = st.number_input("평균기온 입력", value=13.0)
min_temp = st.number_input("최저기온 입력", value=-10.0)
max_temp = st.number_input("최고기온 입력", value=35.0)
rain = st.number_input("합계강수량 입력", value=1100.0)

if st.button("예측하기"):
    pred = model.predict([[avg_temp, min_temp, max_temp, rain]])
    pred_region = le.inverse_transform(pred)[0]
    st.success(f"🌎 예측된 지역: {pred_region}")


