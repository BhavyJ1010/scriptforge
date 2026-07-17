import cv2

from engine.preprocessing.loader import load_image
from engine.preprocessing.pipeline import preprocess_document
from engine.segmentation.connected_components import segment_characters
from engine.glyphs.cleaning import clean_glyph_boxes


image = load_image("data/samples/3.jpeg")

binary = preprocess_document(image)["binary"]

boxes = segment_characters(binary)

clean_boxes = clean_glyph_boxes(boxes)

print(f"Detected components : {len(boxes)}")
print(f"After cleaning      : {len(clean_boxes)}")
print(f"Removed             : {len(boxes)-len(clean_boxes)}")

canvas = cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)

for x, y, w, h in clean_boxes:

    cv2.rectangle(
        canvas,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        1
    )


cv2.namedWindow("Clean Segments", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Clean Segments", 500, 800)
cv2.imshow("Clean Segments", canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()