import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


import streamlit as st
import altair as alt
import plotly.express as px
from bokeh.plotting import figure

# 멀티 페이지용 제목
st.set_page_config(page_title='Hello, penguins!',
                   page_icon='🐧')
st.sidebar.header('Hello, penguins!🐧')

st.header('Penguins 데이터셋을 이용한 시각화 예제')

penguins = pd.read_csv('../data/penguins.csv')
st.write(penguins.head())

x_var = st.selectbox('X 축에 사용할 변수는?',
                     ['island','bill_length_mm','bill_depth_mm','flipper_length_mm','body_mass_g','sex','year'])

y_var = st.selectbox('Y 축에 사용할 변수는?',
                     ['island','bill_length_mm','bill_depth_mm','flipper_length_mm','body_mass_g','sex','year'])


alt_chart = (
    alt.Chart(penguins, title='Penguins 데이터셋 산점도')
    .mark_circle()
    .encode(x=x_var, y=y_var, color='species')
    .interactive()
)
st.altair_chart(alt_chart)

# 막대 그래프
st.bar_chart(penguins.iloc[:, 1:7])

