"""
=========================================================
Algorithm : Contrast Enhancement
=========================================================

Description:
Enhances image intensity by multiplying every pixel by
a scaling factor while clipping values between 0 and 255.

Formula:
    I' = clip(α × I)

where:
    α = Contrast scaling factor
    I = Original pixel intensity

Input:
    - Grayscale image (uint8)

Output:
    - Contrast-enhanced image
    - Side-by-side comparison image

Applications:
    • Microscopy preprocessing
    • Medical imaging
    • Image enhancement
    • Computer vision pipelines

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
raw_image=cv2.imread("../images/practise_image.webp",cv2.IMREAD_GRAYSCALE)
contrasted_image=np.clip(raw_image.astype(np.int16)*2,0,255).astype(np.uint8)
diff=np.hstack((raw_image,contrasted_image))
cv2.imwrite("../results/contrast/contrast.png",diff)
cv2.imshow("old vs edited",diff)
cv2.waitKey(0)
cv2.destroyAllWindows()