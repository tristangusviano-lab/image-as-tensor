import cv2
import numpy as np

img = cv2.imread("image.jpeg")

if img is None:
    raise FileNotFoundError("File not found")

height, width, channels = img.shape
print("shape (height, width, channels):", img.shape)

cropped = img[(height//4):3*(height//4), (width//4):3*(width//4)]

cv2.imshow("Cropped Image", cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
