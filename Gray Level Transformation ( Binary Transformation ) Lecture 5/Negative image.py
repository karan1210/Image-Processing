import cv2 
import numpy as np 
import matplotlib.pyplot as plt

img = cv2.imread('Right_eye_retina_web.jpg')

img_bgr = cv2.imread('Right_eye_retina_web.jpg')

# Negative image
img_negative = 255 - img


# Get height and width of the image

height, width, _ =  img_bgr.shape 

for i in range(0, height - 1): 
	for j in range(0, width - 1): 
		
		# Get the pixel value 
		pixel = img_bgr[i, j] 
		 
		
		# 1st index contains red pixel 
		pixel[0] = 255 - pixel[0] 
		
		# 2nd index contains green pixel 
		pixel[1] = 255 - pixel[1] 
		
		# 3rd index contains blue pixel 
		pixel[2] = 255 - pixel[2] 
		
		# Store new values in the pixel 
		img_bgr[i, j] = pixel 


# Plotting Images

titles = ['img','Negative','Negative image with logic']

images = [img, img_negative, img_bgr]

for i in range(3):
    plt.subplot(1,3,i+1),plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
