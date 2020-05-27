# Hello Everyone

# Welcome to the Image processing using python by Karan Patel

# Lecture 1: https://youtu.be/cQtvE2q_VuE (How to read, save, plot and convert the image into gray)


# Import Libraries

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read the image

img = cv2.imread('Lenna.png')
plt.imshow(img)
plt.show()

img_flip = cv2.flip(img,0)
plt.imshow(img_flip)
plt.show()

video = cv2.VideoCapture(0) # If you are using external cam then make it 1

while(True):
    
    # Capture frame
    ret, frame = video.read()
    
    frame = cv2.flip( frame, 1 )

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Plotting the frames
    cv2.imshow('frame',gray)
    cv2.imshow('color_frame',frame)
    
    # define waitkey
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# when everything good to go

video.release()
cv2.destroyAllWindows()
    
