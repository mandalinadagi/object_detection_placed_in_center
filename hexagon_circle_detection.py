#!/usr/bin/env python
# coding: utf-8

import argparse
import cv2 
import numpy as np
from matplotlib import pyplot as plt

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())


#imagepath = '/home/mandalinadagi/Desktop/Nut Analysis-20190530T191112Z-001/Nut Analysis/images/10-11-2017 - 9.38.49_'

#img = cv2.imread(imagepath + '3' + '.bmp')

#plt.imshow(img)

# load the image, clone it for output, and then convert it to grayscale
img = cv2.imread(args["image"])
output1 = img.copy()
output2 = img.copy()

# to investigate shape of the object in center
mask = np.zeros(img.shape[:2],np.uint8)

bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

rect = (90, 100, 300, 340)

cv2.grabCut(img,mask,rect,bgdModel,fgdModel,3,cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# detect circles in the image
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100, param1=50,param2=60,minRadius=75,maxRadius=110)
print(circles)

if circles is None: 
	img[img > 200] = 255
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	_, threshold = cv2.threshold(gray, 250, 255, cv2.THRESH_BINARY)
	_, contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	for cnt in contours:
		approx = cv2.approxPolyDP(cnt, 0.007*cv2.arcLength(cnt, True), True)
		area = cv2.contourArea(cnt)

		if area <30000.0 and area > 27000.0:
			#print(area)
			cv2.drawContours(output1, [approx], 0, (255, 0, 0), 5)
			x = approx.ravel()[0]
			y = approx.ravel()[1]
			cv2.putText(output1, "Hexagon", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 2,(255,0,0),5)
			break

	# show the output image
	plt.imshow(output1)
	plt.xticks([]), plt.yticks([]) 
	plt.show()
	file1 = open("output.txt", "w")
	file1.write("The output of an image called " + str(args["image"]) + " is a hexagon\n")
	file1.close()

else:
	circles = np.uint16(np.around(circles))
	for i in circles[0,:]:
		# draw the outer circle
		cv2.circle(output2,(i[0],i[1]),i[2],(255,0, 0),5)
		# draw the center of the circle
		cv2.circle(output2,(i[0],i[1]),2,(255,0,0),5)
		#plt.imshow(gray)

	# show the output image
	plt.imshow(output2)
	plt.xticks([]), plt.yticks([]) 
	plt.show()
	file1 = open("output.txt", "w")
	file1.write("The output of an image called " + str(args["image"]) + " is a circle\n")
	file1.close()






