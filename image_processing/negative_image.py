import cv2
import numpy as np
image= cv2.imread("../images/practise_image.webp",cv2.IMREAD_GRAYSCALE)
new=255-image
comparison=np.hstack((image,new))
cv2.imshow("old vs new",comparison)
cv2.waitKey(0)
cv2.destroyAllWindows()