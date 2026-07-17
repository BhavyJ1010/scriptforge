import cv2

from engine.preprocessing.loader import load_image
from engine.preprocessing.pipeline import preprocess_document
from engine.segmentation.connected_components import segment_characters

image = load_image("data/samples/3.jpeg")

binary = preprocess_document(image)["binary"]

boxes = segment_characters(binary)

canvas = cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)

for x, y, w, h in boxes:
    cv2.rectangle(
        canvas,
        (x, y),
        (x+w, y+h),
        (0,255,0),
        2
    )

cv2.namedWindow("Segmented", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Segmented", 500, 800)
cv2.imshow("Segmented", canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()