import streamlit as st
import qrcode
import numpy as np
from PIL import Image

st.title('QRコード自動生成')
url = st.text_input('QRコードを生成したいURL:')

if st.button('QRコード生成'):
    _img = qrcode.make(url)
    _img.save('qrcode.png')
    img = Image.open('qrcode.png')
    st.image(img)
