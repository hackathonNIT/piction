from piction import WriteFunc1,getSinRegression,getSinRegressionArray,plotRegression,getPoint,getPointArray,getDetedge
import cv2
import matplotlib.pyplot as plt

input = "test/img/test.png"

img = cv2.imread(input)

x_data,y_data=getPointArray(img)

print(x_data)

x,y =getSinRegressionArray(x_data,y_data)
# print(x_data)
# print(y_data)
print(x)
# getSinRegression(x_data,y_data)

# #print(WriteFunc1())

# plotRegression()
plt.figure("picture function")
for i in range(len(x)):
	plt.plot(x[i],y[i],label="RegressionFunction"+str(i))
#print(x)
plt.xlabel("num")
plt.ylabel("f")
plt.legend()
#plt.savefig("/content/drive/MyDrive/hackason/results/"+fileName+".png")
# グリッド表示
plt.grid()

# グラフ表示
plt.show()

cv2.imshow("test",getDetedge())

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
