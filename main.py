import streamlit as st

st.title('Hello World!')

clicked = st.button('Click Me!')

if clicked:
    st.write('感谢你点击了我人生中第一个网站！')
    st.write('Thank you for clicking on the first website in my life!')