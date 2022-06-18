import streamlit as st
from streamlit_drawable_canvas import st_canvas
import streamlit.components.v1 as components
from streamlit_webrtc import webrtc_streamer
from PIL import Image
import cv2

from piction import getPoint




st.image("img/title.png")

st.markdown("あなたの書いた絵を関数に変換してみませんか？  \n")

#st.sidebar.header("設定")


# Specify brush parameters and drawing mode
st.sidebar.image("img/logo.png")
st.sidebar.image("img/title.png")
b_width = st.sidebar.slider("ペンのサイズ: ", 1, 100, 10)
b_color = st.sidebar.color_picker("ペンの色: ")

# Create a canvas component
canvas_result  = st_canvas(
fill_color="rgba(255, 165, 0, 0.6)",
stroke_width=b_width,
stroke_color=b_color,
background_color="White",
width = 700,
height= 500,
key="canvas",
)

# Do something interesting with the image data
if canvas_result.image_data is not None:
	st.image(canvas_result.image_data)
	x,y=getPoint(canvas_result.image_data)
	print(len(x))
