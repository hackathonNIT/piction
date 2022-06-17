import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

x=[]
y1=[]
popt=[]

def func1(X, *params):
    Y = np.zeros_like(X)
    for i, param in enumerate(params):
        Y = Y + np.array(param*(np.sin(i*i* X )))
    return Y


def WriteFunc1():
    Y = ""
    for i,param in enumerate(popt):
        if i!=0:
          if param >= 0:
            Y = Y + "+"
          Y=Y+str(param)+"*"+"sin("+str(i*i)+"x)"
    return Y


def getSinRegression(X,Y1):
    global x
    x=np.array(X)
    y1=np.array(Y1)
    x=x.astype(float)
    y1=y1.astype(float)
    print(x)
    global popt
    popt, pcov=curve_fit(func1,x, y1, p0=[1]*len(x))

def plotRegression():
    plt.figure("picture function")
    plt.plot(x,func1(x,*popt),label="RegressionFunction")
    print(x)
    plt.xlabel("num")
    plt.ylabel("f")
    plt.legend()
    #plt.savefig("/content/drive/MyDrive/hackason/results/"+fileName+".png")
    # グリッド表示
    plt.grid()

    # グラフ表示
    plt.show()

