import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import streamlit as st

# pip install konlpy WordCloud
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud

# 멀티 페이지용 제목
st.set_page_config(page_title='Hello, textmining',
                   page_icon='📑')
st.sidebar.header('Hello, textmining!📑')

st.title('텍스트마이닝 시각화 📑')

# 폰트 및 형태소 분석기 초기화
fontpath = 'c:/Windows/Fonts/malgun.ttf'
twitter = Okt()

with open('./data/trump_ko.txt', encoding='utf-8') as f:
    tdocs = f.read()

with open('./data/stevejobs_ko.txt', encoding='utf-8') as f:
    sdocs = f.read()

option1 = st.selectbox('워드 클라우드할 텍스르를 선택하세요',
                       ['도람프 연설문', '스티브 잡스 연설문'])
docs = tdocs if option1 == '도람프 연설문' else sdocs

st.write(docs[:300])

# 워드 클라우드 시각화1
tokens = twitter.nouns(docs)
words = [t for t in tokens if len(t) > 1]

with st.spinner('워드클라우드 생성중...'):
    wc = Counter(words)
    wc = dict(wc.most_common())  # 가장 많은 순으로 정렬

    wcimg = WordCloud(font_path=fontpath, background_color='white',
                      width=640, height=480).generate_from_frequencies(wc)
    fig = plt.figure()
    ax = plt.imshow(wcimg, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(fig)

# 워드 클라우드 시각화2
