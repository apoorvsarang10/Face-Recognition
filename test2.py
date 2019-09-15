import cv2
import os
import numpy as np
from PIL import Image

detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

path = 'A'
count = 0

imagePaths = [os.path.join(path,f) for f in os.listdir(path)]

faceSamples=[]
ids = []

# For each person, enter one numeric face id
#face_id = input('\n enter user id end press <return> ==>  ')
"""
for imagePath in imagePaths:
    #PIL_img = Image.open(imagePath).convert('L') # convert it to grayscale
    #img_numpy = np.array(PIL_img,'uint8')
    id = str(os.path.split(imagePath)[1])
    path0 = path + '/' + id
    if id.split(".")[0] == str(face_id):
	imagePaths1 = [os.path.join(path0,f) for f in os.listdir(path0)]
	imagePaths1 = sorted(list(imagePaths1))
    	for imagePath1 in imagePaths1:
	    id1 = str(os.path.split(imagePath1)[1])
	    print(id1)
	    PIL_img = Image.open(imagePath1).convert('L') # convert it to grayscale
    	    img_numpy = np.array(PIL_img,'uint8')
	    img_numpy = cv2.resize(img_numpy, (32,32)).flatten()
	    faces = face_detector.detectMultiScale(img_numpy)

    	    for (x,y,w,h) in faces:
            	faceSamples.append(img_numpy[y:y+h,x:x+w])
        	ids.append(id)
		cv2.imwrite("B/User." + str(face_id) + '.' + str(count) + ".jpg", img_numpy[y:y+h,x:x+w])
		count += 1
"""
for imagePath in imagePaths:
	PIL_img = Image.open(imagePath).convert('L') # convert it to grayscale
        img_numpy = np.array(PIL_img,'uint8')
	
	img_numpy = cv2.flip(img_numpy,-1)

        id = str(os.path.split(imagePath)[-1].split(".")[1])
        faces = detector.detectMultiScale(img_numpy)
	print("\nFirst image: \n")
	print(faces)
	print("\nBefore loop: \n")
	if len(faces)==0:
		for angle in np.arange(0, 45, 1):
			rotated = imutils.rotate_bound(img_numpy, angle)
			cv2.imshow("Rotated (Correct)", rotated)
			cv2.waitKey(0)
			faces = detector.detectMultiScale(img_numpy)
			print(faces)
			if len(faces)>0:
				break