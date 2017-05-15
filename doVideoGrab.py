
import cv2
import urllib 
import numpy as np
from PIL import Image

def runStream():
	stream=urllib.urlopen('http://192.168.43.1:8080/video')

	bytes=''
	while True:
	    bytes+=stream.read(1024)
	    a = bytes.find('\xff\xd8')
	    b = bytes.find('\xff\xd9')
	    if a!=-1 and b!=-1:
		jpg = bytes[a:b+2]
		bytes= bytes[b+2:]
		i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.CV_LOAD_IMAGE_COLOR)
		image = makeContour(i)
		cv2.imshow('Contour',image)
		if cv2.waitKey(1) ==27:
		    exit(0)  

"""
import cv2
import urllib 
import numpy as np
e
stream=open('http://192.168.43.1:8080/video','rb')
bytes=''
while True:
    bytes+=stream.read(1024)
    a = bytes.find('\xff\xd8')
    b = bytes.find('\xff\xd9')
    if a!=-1 and b!=-1:
        jpg = bytes[a:b+2]
        bytes= bytes[b+2:]
        i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.CV_LOAD_IMAGE_COLOR)
        cv2.imshow('i',i)
        if cv2.waitKey(1) ==27:
            exit(0)   
"""

def auto_canny(image, sigma=0.33):
	# compute the median of the single channel pixel intensities
	v = np.median(image)
 
	# apply automatic Canny edge detection using the computed median
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edged = cv2.Canny(image, lower, upper)
 
	# return the edged image
	return edged

def makeContour(image):
	#crop_img = image[0:480, 0:480] # Crop from x, y, +w pixels, +h pixels (Max 480,640)
	
	crop_img=image
	gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (3, 3), 0)
	
	# detect edges in the image
	#edged = cv2.Canny(gray, 10, 250)
	
	edged = auto_canny(gray)
		
	
	
	#Display to screen
	#cv2.imshow("cropped", crop_img)
	#return crop_img

	#resized_image = cv2.resize(edged, (16, 16))
	#resized_image =  cv2.resize(resized_image, (200, 200))
	#return resized_image
	return edged
	
"""
	# construct and apply a closing kernel to 'close' gaps between 'white'
	# pixels
	kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
	closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
	
	# find contours (i.e. the 'outlines') in the image and initialize the
	# total number of books found
	(cnts, _) = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	total = 0

	# loop over the contours
	for c in cnts:
		# approximate the contour
		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.02 * peri, True)

		# if the approximated contour has four points, then assume that the
		# contour is a book -- a book is a rectangle and thus has four vertices
		if len(approx) == 4:
			cv2.drawContours(image, [approx], -1, (0, 255, 0), 4)
			total += 1

	return image
"""


runStream()

