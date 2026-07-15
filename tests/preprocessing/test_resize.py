import cv2

from engine.preprocessing.loader import load_image
from engine.preprocessing.resize import resize_image

image = load_image("data/samples/2.jpeg")

resized = resize_image(image)

print("Original:", image.shape)
print("Resized :", resized.shape)

cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Original", 500, 800)
cv2.imshow("Original", image)

cv2.namedWindow("Resized", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Resized", 500, 800)
cv2.imshow("Resized", resized)

cv2.waitKey(0)

cv2.destroyAllWindows()