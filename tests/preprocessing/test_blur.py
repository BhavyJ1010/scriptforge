import cv2

from engine.preprocessing.blur import gaussian_blur
from engine.preprocessing.loader import load_image
from engine.preprocessing.resize import resize_image
from engine.preprocessing.grayscale import to_grayscale

image = load_image("data/samples/4.jpeg")

resized = resize_image(image)
gray = to_grayscale(resized)
blurred = gaussian_blur(gray)

cv2.namedWindow("Gray", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Gray", 500, 800)
cv2.imshow("Gray", gray)

cv2.namedWindow("Blurred", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Blurred", 500, 800)
cv2.imshow("Blurred", blurred)

cv2.waitKey(0)
cv2.destroyAllWindows()