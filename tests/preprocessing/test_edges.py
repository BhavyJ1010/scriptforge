import cv2

from engine.preprocessing.edges import detect_edges
from engine.preprocessing.loader import load_image
from engine.preprocessing.resize import resize_image
from engine.preprocessing.grayscale import to_grayscale
from engine.preprocessing.blur import gaussian_blur

image = load_image("data/samples/3.jpeg")

resized = resize_image(image)
gray = to_grayscale(resized)
blurred = gaussian_blur(gray)
edged = detect_edges(blurred)

cv2.namedWindow("Blurred", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Blurred", 500, 800)
cv2.imshow("Blurred", blurred)

cv2.namedWindow("edges", cv2.WINDOW_NORMAL)
cv2.resizeWindow("edges", 500, 800)
cv2.imshow("edges", edged)

cv2.waitKey(0)
cv2.destroyAllWindows()