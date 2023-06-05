import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np

# タイトル表示
st.title('先端課題039 streamlit')


st.write('グラフの表示')
# Please write your code!!

df = pd.read_csv("../data/data.csv")
st.write(df)


st.write('ファイルのアップロード&表示')
# Please write your code!!

uploaded_file = st.file_uploader("ファイルアップロード", type='png')
try:
    image = Image.open(uploaded_file)
    img_array = np.array(image)
    st.image(img_array, use_column_width=True)
    st.balloons()
except Exception:
    # 画像ファイルの読み込みエラー防止
    pass
