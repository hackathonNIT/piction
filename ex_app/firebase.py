from firebase_admin import credentials,initialize_app,firestore
import streamlit as st
import numpy as np
import random

if 'firebase_initialize' not in st.session_state:
	st.session_state["firebase_initialize"] = 1
	cred = credentials.Certificate(r"pictionsample-firebase-adminsdk-31wwv-45922fca88.json")
	initialize_app(cred,{'storageBucket': 'gs://pictionsample.appspot.com'})



def getFunc(num=0):
	funcs=readImage()
	if num==0 or len(funcs)<=num:
		return funcs
	ret =[]
	for i in range(num):
		ret.append(random.choice(funcs))
	return ret
	


def readImage():
	db = firestore.client()
	docs=db.collection('functions').stream()
	funcs=[]
	for doc in docs:
		data =doc.to_dict()
		x=np.fromstring(data["x"], dtype = "float64")
		y=np.fromstring(data["y"], dtype = "float64")
		func_str=data["func"]
		funcs.append({"x":x,"y":y,"func":func_str})
	return funcs


def writeImage(x,y,func_str):
	db = firestore.client()
	doc = db.collection('functions').document()
	x_bin=x.tostring()
	y_bin=y.tostring()
	doc.set({
		'x':x_bin,
		'y':y_bin,
		'func':func_str
	})
	return

