#i have tweaked with this file a little so you may want to go through the code and see line 140 in particular
#if you want to run the code then change the other file too i have attached my other file too so you may know what to change
############## Task1.1 - ArUco Detection ##############

import numpy as np
import cv2
import cv2.aruco as aruco
import sys
import math
import time

def detect_ArUco(img):
	## function to detect ArUco markers in the image using ArUco library
	## argument: img is the test image
	## return: dictionary named Detected_ArUco_markers of the format {ArUco_id_no : corners}, where ArUco_id_no indicates ArUco id and corners indicates the four corner position of the aruco(numpy array)
	## 		   for instance, if there is an ArUco(0) in some orientation then, ArUco_list can be like
	## 				{0: array([[315, 163],
	#							[319, 263],
	#							[219, 267],
	#							[215,167]], dtype=float32)}

    Detected_ArUco_markers = {}
    
    ## enter your code here ##
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_5X5_250)
    parameters = aruco.DetectorParameters_create()

    corners , ids , _ = aruco.detectMarkers(gray,aruco_dict,parameters=parameters)
    
    for i in range(len(ids)):
    	Detected_ArUco_markers[str(ids[i])] = corners[i]  

    return Detected_ArUco_markers


def Calculate_orientation_in_degree(Detected_ArUco_markers):
	## function to calculate orientation of ArUco with respective to the scale mentioned in Problem_Statement.pdf
	## argument: Detected_ArUco_markers  is the dictionary returned by the function detect_ArUco(img)
	## return : Dictionary named ArUco_marker_angles in which keys are ArUco ids and the values are angles (angles have to be calculated as mentioned in the ProblemStatement.pdf)
	##			for instance, if there are two ArUco markers with id 1 and 2 with angles 120 and 164 respectively, the 
	##			function should return: {1: 120 , 2: 164}

	ArUco_marker_angles = {}
	## enter your code here ##
	for ids in Detected_ArUco_markers:
		for corner in Detected_ArUco_markers[ids]:
			topListx = []
			topListy = []
			for i in range(4):
				xcenter = int((corner[0][0]+corner[2][0])/2)							#determining x coordinate of center by midpoint theorem
				ycenter = int((corner[0][1]+corner[2][1])/2)							#determining y coordinate of center by midpoint theorem

				topListx.append(corner[i][0])					#making a list of corners x axis
				topListy.append(corner[i][1])
				#print topList
				#print "works"

			xtop1 = max(topListx)								#top right
			ytop2 = min(topListy)								#top left

			for i in range(4):
				if corner[i][0] == xtop1: 	
					ytop1 = corner[i][1]
					
				if corner[i][1] == ytop2:
					xtop2 = corner[i][0]

			lcenterx = int((xtop2+xtop1)/2)											#determining y coordinate of an edge to draw line
			lcentery = int((ytop2+ytop1)/2)											#determining x coordinate of an edge to draw line
			
			slope = -1*( xcenter - lcenterx )/float(( ycenter - lcentery ))
			angle = 90 - int(57.3*math.atan(slope))
			ArUco_marker_angles[ids] = angle


	return ArUco_marker_angles	## returning the angles of the ArUco markers in degrees as a dictionary


def mark_ArUco(img,Detected_ArUco_markers,ArUco_marker_angles):
	## function to mark ArUco in the test image as per the instructions given in problem_statement.pdf 
	## arguments: img is the test image 
	##			  Detected_ArUco_markers is the dictionary returned by function detect_ArUco(img)
	##			  ArUco_marker_angles is the return value of Calculate_orientation_in_degree(Detected_ArUco_markers)
	## return: image namely img after marking the aruco as per the instruction given in Problem_statement.pdf

    ## enter your code here ##

    #print Detected_ArUco_markers

    for ids in Detected_ArUco_markers:
    	#print ids
    	for corner in Detected_ArUco_markers[ids]:
	    	
    		topListx = []
    		topListy = []

    		for i in range(4):
    			cv2.circle(img,(corner[i][0],corner[i][1]),7,(10*i,50*i,30*i),-1)

    			xcenter = int((corner[0][0]+corner[2][0])/2)
    			ycenter = int((corner[0][1]+corner[2][1])/2)
    			cv2.circle(img,(xcenter,ycenter),7,(0,0,255),-1)

    			topListx.append(corner[i][0])
    			topListy.append(corner[i][1])
    		
    		xtop1 = max(topListx)
    		ytop2 = min(topListy)

    		for i in range(4):
    			if corner[i][0] == xtop1:
    				ytop1 = corner[i][1]

    			if corner[i][1] == ytop2:
    				xtop2 = corner[i][0]

    		lcenterx = int( ( xtop2 + xtop1 ) / 2 )			
    		lcentery = int( ( ytop2 + ytop1 ) / 2 )
    		
    		cv2.circle(img,(lcenterx,lcentery),7,(100,100,100),-1)
    		cv2.line(img,(xcenter,ycenter),(lcenterx,lcentery),(255,0,0),5)

    		#cv2.circle(img,(corner[2][0],corner[2][1]),30,(0,0,255),4)
	    	x = int(corner[2][0]-15)
	    	y = int(corner[2][1]+15)
	    	k = ids
	    	ids = str(ids)
	    	ids = ids[1]
	    	cv2.putText(img,ids,(x,y),cv2.FONT_HERSHEY_COMPLEX,1.5,(0,0,255),2)

    		#cv2.circle(img,(corner[0][0],corner[0][1]),30,(0,255,0),4)
	    	x = int(corner[0][0]-25)
	    	y = int(corner[0][1]+15)
	    	angle = str(ArUco_marker_angles[k])
	    	#ids = ids[1]
	    	cv2.putText(img,angle,(x,y),cv2.FONT_HERSHEY_COMPLEX,1.3,(0,255,0),2)



	#return img

