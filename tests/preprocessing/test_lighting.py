import cv2

from engine.preprocessing.loader import load_image
from engine.preprocessing.resize import resize_image
from engine.preprocessing.grayscale import to_grayscale
from engine.preprocessing.lighting import normalize_lighting

image = load_image("data/samples/3.jpeg")
resized = resize_image(image)
gray = to_grayscale(resized)

normalized = normalize_lighting(gray)

cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Original", 500, 800)
cv2.imshow("Original", image)

cv2.namedWindow("Gray", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Gray", 500, 800)
cv2.imshow("Gray", normalized)

cv2.waitKey(0)
cv2.destroyAllWindows()