import cv2
import numpy as np

img = cv2.imread("image.jpeg")

height, width, channels = img.shape
print("shape (height, width, channels):", img.shape)

if img is None:
    raise FileNotFoundError("File not found")
print("shape (height, width, channels):", img.shape)
print("dimensions (ndim):", img.ndim)
print("data type (dtype):", img.dtype)
print("total number in RAM:", img.size)

top_left_pixel = img[height-1, 50]
top_right_pixel = img[50, width-1]

print(top_left_pixel)
print(top_right_pixel)

img_rgb = img[:, :, ::-1]

comparison = np.hstack([img_rgb, img])
cv2.imshow("LEFT: RGB, RIGHT: BGR",comparison)
cv2.waitKey(0)
cv2.destroyAllWindows()

