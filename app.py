import streamlit as st
from PIL import Image
st.title("Counting Fish Web Application") 
#st.sidebar.success("Select a page above")
result = st.button("Click Here")
if result:
    image = Image.open('result2.jpg')
    st.image(image, caption='Result for Counting')






