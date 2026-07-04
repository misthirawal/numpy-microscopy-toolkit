"""
=========================================================
Algorithm : Brightness Enhancement
=========================================================

Description:
Increases the brightness of a grayscale image by adding
a constant value to every pixel while ensuring pixel
values remain within the valid range [0, 255].

Formula:
    I' = clip(I + β)

where:
    I  = Original pixel intensity
    β  = Brightness value
    clip() limits values between 0 and 255

Input:
    - Grayscale image (uint8)

Output:
    - Brightened image
    - Side-by-side comparison image

Applications:
    • Low-light microscopy
    • Medical imaging
    • Satellite imagery
    • Image preprocessing

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
image=cv2.imread("../images/practise_image.webp",cv2.IMREAD_GRAYSCALE)
new=np.clip(image+50,0,255)
diff=np.hstack((image,new))
cv2.imwrite("../results/brightness/brightness_comparison.png",diff)
cv2.imshow("old vs new",diff)
cv2.waitKey(0)
cv2.destroyAllWindows()

