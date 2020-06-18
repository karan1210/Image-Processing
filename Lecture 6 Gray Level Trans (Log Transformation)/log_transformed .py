import cv2 
import numpy as np 
import matplotlib.pyplot as plt

# Open the image. 
img = cv2.imread('Right_eye_retina_web.jpg') 

# Apply log transform with "C = 1"
c = 1 
log_transformed = c * np.log(1 + img) 
c_1 = np.array(log_transformed, dtype = np.uint8)

# Apply log transform with "C = 25"
c = 25 
log_transformed = c * np.log(1 + img) 
c_25 = np.array(log_transformed, dtype = np.uint8)

# Apply log transform with "C = 50"
c = 50 
log_transformed = c * np.log(1 + img) 
c_50 = np.array(log_transformed, dtype = np.uint8)

# Apply log transform with "C = 75"
c = 75 
log_transformed = c * np.log(1 + img) 
c_75 = np.array(log_transformed, dtype = np.uint8)

# Apply log transform with "C = 150"
c = 150 
log_transformed = c * np.log(1 + img) 
c_150 = np.array(log_transformed, dtype = np.uint8)

# Apply log transform with "Perfect C". 
c = 255/(np.log(1 + np.max(img))) 
log_transformed = c * np.log(1 + img) 

# Specify the data type. 
c_perfect = np.array(log_transformed, dtype = np.uint8) 


#Plotting Images
titles = ['Original img','log transform with "C = 1"','log transform with "C = 25"','log transform with "C = 50"','Apply log transform with "C = 75"','Apply log transform with "C = 150"','Apply log transform with "perfect C"']
images = [img, c_1, c_25, c_50, c_75, c_150, c_perfect]

for i in range(7):
    plt.subplot(3,3,i+1),plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()






