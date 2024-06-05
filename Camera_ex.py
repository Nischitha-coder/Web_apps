import streamlit as st
from PIL import Image

camera = st.camera_input("Camera")
print(camera)

if camera:
    img = Image.open(camera)
    gray_img = img.convert("L")
    st.image(gray_img)
