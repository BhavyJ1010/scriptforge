import cv2

from engine.preprocessing.loader import load_image
from engine.preprocessing.pipeline import preprocess_document


image = load_image("data/samples/3.jpeg")

result = preprocess_document(image)

cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Original", 500, 800)
cv2.imshow("Original", image)

cv2.namedWindow("Page", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Page", 500, 800)
cv2.imshow("Page", result["page"])

cv2.namedWindow("Binary", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Binary", 500, 800)
cv2.imshow("Binary", result["binary"])


cv2.waitKey(0)
cv2.destroyAllWindows()