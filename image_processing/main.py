import cv2
import numpy as np
image=cv2.imread("../images/practise_image.webp",cv2.IMREAD_GRAYSCALE)
print(image.size)
print(image.ndim)
print(image)
print(image[0,0])
print(image.shape)
print(image.dtype)
print(image[100,200])
print(image[256,0])
print(image[0])

