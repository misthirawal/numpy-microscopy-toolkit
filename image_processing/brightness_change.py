import cv2
import numpy as np
image=cv2.imread("../images/practise_image.webp",cv2.IMREAD_GRAYSCALE)
new=np.clip(image+50,0,255)
diff=np.hstack((image,new))
cv2.imshow("old vs new",diff)
cv2.waitKey(0)
cv2.destroyAllWindows()

