############## Task1.1 - ArUco Detection ##############
### YOU CAN EDIT THIS FILE FOR DEBUGGING PURPOSEs, SO THAT YOU CAN TEST YOUR ArUco_library.py AGAINST THE VIDEO Undetected ArUco markers.avi###
### BUT MAKE SURE THAT YOU UNDO ALL THE CHANGES YOU HAVE MADE FOR DEBUGGING PURPOSES BEFORE TESTING AGAINST THE TEST IMAGES ###

import numpy as np
import cv2
import cv2.aruco as aruco
import time
import Arlib


image_list = ["../Test_images/Test_image1.png","../Test_images/Test_image2.png"]
test_num = 1

for image in image_list:
	img = cv2.imread(image)
	Detected_ArUco_markers = Arlib.detect_ArUco(img)									## detecting ArUco ids and returning ArUco dictionary
	angle = Arlib.Calculate_orientation_in_degree(Detected_ArUco_markers)				## finding orientation of aruco with respective to the menitoned scale in Problem_statement.pdf
	#print angle
	#img = Arlib.mark_ArUco(img,Detected_ArUco_markers,angle)	
	Arlib.mark_ArUco(img,Detected_ArUco_markers,angle)	
	cv2.imshow('result',img)					## marking the parameters of aruco which are mentioned in the Problem_Statement.pdf
	result_image = "../Test_images/Result_image"+str(test_num)+".png"
	cv2.imwrite(result_image,img)									## saving the result image
	test_num = test_num +1
	#cv2.waitKey(0)

'''
import numpy as np
import cv2
import cv2.aruco as aruco
import time
import Arlib


cap = cv2.VideoCapture('Undetected ArUco Markers.avi')
test_num = 1

while cap.isOpened():
	ret , frame = cap.read()
	Detected_ArUco_markers = Arlib.detect_ArUco(frame)									## detecting ArUco ids and returning ArUco dictionary
	angle = Arlib.Calculate_orientation_in_degree(Detected_ArUco_markers)				## finding orientation of aruco with respective to the menitoned scale in Problem_statement.pdf
	#print angle
	#img = Arlib.mark_ArUco(img,Detected_ArUco_markers,angle)	
	Arlib.mark_ArUco(frame,Detected_ArUco_markers,angle)	
	cv2.imshow('result',frame)					## marking the parameters of aruco which are mentioned in the Problem_Statement.pdf
	result_image = "../Test_images/Result_image"+str(test_num)+".png"
	cv2.imwrite(result_image,frame)									## saving the result image
	test_num = test_num + 1
	#cv2.waitKey(0)

'''