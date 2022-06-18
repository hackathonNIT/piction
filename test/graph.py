from piction import WriteFunc1,getSinRegression,plotRegression,getPoint,getDetedge
import cv2

input = "test/img/test3.png"

img = cv2.imread(input)

x_data,y_data=getPoint(img,50)

print(x_data)
print(y_data)

getSinRegression(x_data,y_data)

#print(WriteFunc1())

plotRegression()

cv2.imshow("test",getDetedge())

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
