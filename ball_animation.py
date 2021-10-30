# import the necessary packages
import numpy as np
import cv2
import imutils
import time
low_red = np.array([50, 130, 60])
high_red = np.array([179, 255, 255])
pts = []
vs = cv2.imread("ball static.png")
cv2.waitKey(1)
hsv = cv2.cvtColor(vs, cv2.COLOR_BGR2HSV)

mask = cv2.inRange(hsv, low_red, high_red)
mask = cv2.erode(mask, None, iterations=2)
mask = cv2.dilate(mask, None, iterations=2)

cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
center = None
if len(cnts) > 0:

    c = max(cnts, key=cv2.contourArea)
    ((x, y), radius) = cv2.minEnclosingCircle(c)
    M = cv2.moments(c)
    center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
    if radius > 10:
        cv2.circle(vs, (int(x), int(y)), int(radius),
                   (0, 255, 255), 2)
        cv2.circle(vs, center, 5, (0, 0, 255), -1)
pts.append(center)
for i in range(1, len(pts)):
    if pts[i - 1] is None or pts[i] is None:
        continue
cv2.imshow("Frame", vs)
key = cv2.waitKey(1) & 0xFF
cv2.destroyAllWindows()
print(pts)
# print(pts[2][1])
y = []
for x in pts:
    y.append(x[1])


print(y)