from firebase_admin import credentials,initialize_app,firestore
import streamlit as st
import numpy as np
import random

if 'firebase_initialize' not in st.session_state:
	st.session_state["firebase_initialize"] = 1
	cred = credentials.Certificate(r"ex_app/pictionsample-firebase-adminsdk-31wwv-45922fca88.json")
	initialize_app(cred,{'storageBucket': 'gs://pictionsample.appspot.com'})


def getArray1(x,y):
	x_ret=[]
	y_ret=[]
	for i in range(len(x)):
		x_ret[len(x_ret):len(x_ret)] =x[i]
		y_ret[len(y_ret):len(y_ret)] =y[i]
		x_ret.append(-1)
		y_ret.append(-1)
	return np.array(x_ret),np.array(y_ret)
	

def getArray2(x,y):
	x_sub=[]
	y_sub=[]
	x_ret=[]
	y_ret=[]
	for i in range(len(x)):
		if x[i]==-1:
			x_ret.append(x_sub)
			y_ret.append(y_sub)
			x_sub=[]
			y_sub=[]
		else:
			x_sub.append(x[i])
			y_sub.append(y[i])
	return np.array(x_ret),np.array(y_ret)



	


def readImage():
	db = firestore.client()
	docs=db.collection('functions').stream()
	funcs=[]
	for doc in docs:
		data =doc.to_dict()
		funcs.append({"x":data["x"],"y":data["y"],"func":data["func"]})
	return funcs

def getFunc(num=0):
	funcs=readImage()
	print("get")
	ret =[]
	print("f")
	for i in range(min(num,len(funcs))):
		f1=random.choice(funcs)
		fx,fy=getArray2(np.fromstring(f1["x"], dtype = "float64"), np.fromstring(f1["y"], dtype = "float64"))
		print(fx)
		
		ret.append({"x":fx,"y":fy,"func":f1["func"]})
	return ret

def writeImage(x,y,func_str):
	db = firestore.client()
	doc = db.collection('functions').document()
	x1,y1=getArray1(x,y)
	x_np=np.array(x1)
	y_np=np.array(y1)
	x_bin=x_np.tostring()
	y_bin=y_np.tostring()
	doc.set({
		'x':x_bin,
		'y':y_bin,
		'func':func_str
	})
	return

