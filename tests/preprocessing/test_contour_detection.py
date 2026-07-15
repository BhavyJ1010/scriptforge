import cv2

from engine.preprocessing.loader import load_image
from engine.preprocessing.resize import resize_image
from engine.preprocessing.grayscale import to_grayscale
from engine.preprocessing.blur import gaussian_blur
from engine.preprocessing.edges import detect_edges
from engine.preprocessing.morphology import morphological_close
from engine.preprocessing.contour_detection import (find_contours, sort_contours_by_area, approximate_contour)

image = load_image("data/samples/3.jpeg")

# Preprocessing Pipeline
resized = resize_image(image)
gray = to_grayscale(resized)
blurred = gaussian_blur(gray)
edged = detect_edges(blurred)
morphed = morphological_close(edged)

# Contour Detection
contours = find_contours(morphed)
sorted_contours = sort_contours_by_area(contours)

print(f"Total contours: {len(contours)}")
print("\nLargest contours:\n")

for contour in sorted_contours[:5]:
    approx = approximate_contour(contour)
    print(
        f"Area: {cv2.contourArea(contour):.1f}"
        f" | Vertices: {len(approx)}" )


# Visualization
contour_image = resized.copy()
cv2.drawContours(contour_image, contours, -1, (0,255,0), 2)

cv2.namedWindow("Contours", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Contours", 500, 800)
cv2.imshow("Contours", contour_image)

cv2.waitKey(0)
cv2.destroyAllWindows()