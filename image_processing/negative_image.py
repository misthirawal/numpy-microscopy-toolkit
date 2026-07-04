"""
=========================================================
Algorithm : Negative Image Transformation
=========================================================

Description:
Generates the negative of a grayscale image by inverting
every pixel intensity.

Formula:
    I' = 255 - I

where:
    I  = Original pixel intensity
    I' = Negative pixel intensity

Input:
    - Grayscale image (uint8)

Output:
    - Negative image
    - Side-by-side comparison image

Applications:
    • Medical X-ray analysis
    • Microscopy image enhancement
    • Satellite image processing
    • Feature visualization

Time Complexity:
    O(n)

Space Complexity:
    O(n)

Author:
    Pihu

Project:
    NumPy Microscopy Toolkit
=========================================================
"""
import cv2
import numpy as np
image= cv2.imread("../images/practise_image.webp",cv2.IMREAD_GRAYSCALE)
new=255-image
comparison=np.hstack((image,new))
cv2.imwrite("../results/negative/comparison.png", comparison)
cv2.imshow("old vs new",comparison)
cv2.waitKey(0)
cv2.destroyAllWindows()