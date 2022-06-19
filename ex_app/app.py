import streamlit as st
from streamlit_drawable_canvas import st_canvas
import cv2
from piction import getPointArray ,getSinRegressionArray,WriteFunc1
import matplotlib.pyplot as plt

from firebase import getFunc,writeImage

if 'flag' not in st.session_state:
  st.session_state["flag"] = 0

st.title("Drawable Canvas")
st.markdown("""
Draw on the canvas, get the image data back into Python !
* Doubleclick to remove the selected object when not in drawing mode
""")
st.sidebar.header("Configuration")

# Specify brush parameters and drawing mode
b_width = st.sidebar.slider("Brush width: ", 1, 100, 10)
b_color = st.sidebar.color_picker("Enter brush color hex: ")
bg_color = st.sidebar.color_picker("Enter background color hex: ", "#eee")
drawing_mode = st.sidebar.checkbox("Drawing mode ?", True)

# Create a canvas component
canvas_result  = st_canvas(
fill_color="rgba(255, 165, 0, 0.3)",
stroke_width=10,
stroke_color="Black",
background_color="White",
# width = 150,
height= 150,
key="canvas",
)


if st.button("関数", key=0):
  st.session_state["flag"] = 1

# Do something interesting with the image data
if canvas_result.image_data is not None and st.session_state["flag"]==1:
	st.image(canvas_result.image_data)
	x_data,y_data=getPointArray(canvas_result.image_data)
	print(x_data)
	x,y=getSinRegressionArray(x_data,y_data)
	fig= plt.figure("your func")
	for i in range(len(x)):
		plt.plot(x[i],y[i],label="RegressionFunction"+str(i))
	plt.xlabel("num")
	plt.ylabel("f")
	plt.legend()
	#plt.savefig("/content/drive/MyDrive/hackason/results/"+fileName+".png")
	# グリッド表示
	plt.grid()
	st.pyplot(fig)
	writeImage(x,y,WriteFunc1())
	st.session_state["flag"]=0

if canvas_result.image_data is not None :
	st.markdown("""
	みんなの作った作品！
	""")
	print("start")
	funcs=getFunc(1)
	fig= plt.figure("sumple function")
	for func1 in funcs:
		for i in range(len(func1["x"])):
			plt.plot(func1["x"][i],func1["y"][i],label="RegressionFunction"+str(i))
	
	plt.xlabel("num")
	plt.ylabel("f")
	plt.legend()
	#plt.savefig("/content/drive/MyDrive/hackason/results/"+fileName+".png")
	# グリッド表示
	plt.grid()
	st.pyplot(fig)

	