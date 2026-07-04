import cv2
import numpy as np
raw_image=cv2.imread("../images/practise_image.webp",cv2.IMREAD_GRAYSCALE)
contrasted_image=np.clip(raw_image.astype(np.int16)*2,0,255).astype(np.uint8)
diff=np.hstack((raw_image,contrasted_image))
cv2.imshow("old vs edited",diff)
cv2.waitKey(0)
cv2.destroyAllWindows()