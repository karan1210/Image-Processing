import cv2 
import numpy as np
import matplotlib.pyplot as plt

# Open and read the image.

img = cv2.imread('Right_eye_retina_web.jpg') 

images = [img]

# Trying 6 gamma values. 
for gamma in [0.1, 0.5, 1.5, 2.5, 10, 20]:
	
	# Apply gamma correction. 
	gamma_corrected = np.array(255*(img / 255) ** gamma, dtype = 'uint8') 

	# Save edited images. 
	cv2.imwrite('gamma_transformed'+str(gamma)+'.jpg', gamma_corrected)
	images.append(gamma_corrected)


#Plotting Images
titles = ['Original img','gamma_transformed gamma = 0.1','gamma_transformed gamma = 0.5','gamma_transformed gamma = 1.5','gamma_transformed gamma = 2.5','gamma_transformed gamma = 10','gamma_transformed gamma = 20']

for i in range(7):
    plt.subplot(3,3,i+1),plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
