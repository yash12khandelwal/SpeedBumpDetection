import os
import cv2

collection = '/home/yash/Desktop/temp1/'
collection_save = '/home/yash/Desktop/temp/'
arr = os.listdir(collection)
for i in arr:	
	image = cv2.imread(collection + str(i), 1)
	resized = cv2.resize(image, (200, 200))
	cv2.imwrite(collection_save + i, resized)
