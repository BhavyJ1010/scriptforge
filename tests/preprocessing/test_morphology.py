import cv2

from engine.preprocessing.morphology import morphological_close
from engine.preprocessing.loader import load_image
from engine.preprocessing.resize import resize_image
from engine.preprocessing.grayscale import to_grayscale
from engine.preprocessing.blur import gaussian_blur
from engine.preprocessing.edges import detect_edges

image = load_image("data/samples/3.jpeg")

resized = resize_image(image)
gray = to_grayscale(resized)
blurred = gaussian_blur(gray)
edged = detect_edges(blurred)
morphed = morphological_close(edged)

cv2.namedWindow("Edges", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Edges", 500, 800)
cv2.imshow("Edges", edged)

cv2.namedWindow("morphed", cv2.WINDOW_NORMAL)
cv2.resizeWindow("morphed", 500, 800)
cv2.imshow("morphed", morphed)

cv2.waitKey(0)
cv2.destroyAllWindows()