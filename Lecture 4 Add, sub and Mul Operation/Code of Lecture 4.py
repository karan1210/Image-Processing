import cv2
import numpy as np
from matplotlib import pyplot as plt


# Image Addition
img1 = cv2.imread("Image 2 Back.png");
img2 = cv2.imread("Image 2.png");

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

height, width , color_scale = img1.shape

dim = (width, height)

# resize image
img2 = cv2.resize(img2, dim, interpolation = cv2.INTER_AREA)

print( 'Original Dimensions img1 : ', img1. shape)
print( 'Original Dimensions img2 : ', img2. shape)

add_img = cv2.add(img1, img2);

# Image Subtraction

sub_img = cv2.subtract(img1, img2);

# Image Multiply
mult_img = cv2.multiply(img1, img2)


titles = ['image 1','image 2','Added image','image 1','image 2','Subtract image', 'image 1','image 2','Multiply image']
images = [img1, img2, add_img, img1, img2, sub_img, img1, img2, mult_img]

for i in range(9):
    plt.subplot(3,3,i+1),plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
