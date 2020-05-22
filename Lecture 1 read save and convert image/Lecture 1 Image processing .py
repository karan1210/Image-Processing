#!/usr/bin/env python
# coding: utf-8

# # How can you read, convert to gray and save image in python 
# # By Karan Patel

# In[15]:


import numpy as np
import cv2
from matplotlib import pyplot as plt

# Load an color image 
img = cv2.imread('lenna.png')

# Load an Gray scale image 
img_gray = cv2.imread('lenna.png',0)


# In[17]:


# Show the iamge BRG 

cv2.imshow('image',img)

cv2.waitKey(0)

cv2.destroyAllWindows()


# In[18]:


# Show the image Gray
cv2.imshow('image gray',img_gray)

cv2.waitKey(0)

cv2.destroyAllWindows()


# In[19]:


plt.imshow(img_gray, cmap = 'gray', interpolation = 'bicubic')

plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis

plt.show()


# ## Sum it up
# 
# 
# Below program loads an image in Color form, displays it, Convert it into gray and save the image if you press ‘s’ and exit, or simply exit without saving if you press ESC key.

# In[21]:


cv2.imshow('image',img)

k = cv2.waitKey(0)

if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
    
elif k == ord('s'): # wait for 's' key to save and exit
    img_gray = cv2.imread('lenna.png',0)
    cv2.imwrite('lenna_gray.png',img_gray)
    cv2.destroyAllWindows()


# In[ ]:




