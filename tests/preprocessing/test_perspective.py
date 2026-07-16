import cv2

from engine.preprocessing.loader import load_image
from engine.preprocessing.resize import resize_image
from engine.preprocessing.grayscale import to_grayscale
from engine.preprocessing.blur import gaussian_blur
from engine.preprocessing.edges import detect_edges
from engine.preprocessing.morphology import morphological_close
from engine.preprocessing.contour_detection import (
    find_contours,
    sort_contours_by_area,
    approximate_contour,
)
from engine.preprocessing.perspective import (
    order_points,
    four_point_transform,
)


# Load image
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

approx = approximate_contour(sorted_contours[0])

print(f"Detected vertices: {len(approx)}")


# Perspective Transform
transformed = None

if len(approx) == 4:
    corners = approx.reshape(4, 2)

    ordered_corners = order_points(corners)

    transformed = four_point_transform(
        resized,
        ordered_corners
    )

else:
    print("Perspective transform skipped (page contour is not a quadrilateral).")


# Visualization
cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Original", 500, 800)
cv2.imshow("Original", resized)


if transformed is not None:
    cv2.namedWindow("Transformed", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Transformed", 500, 800)
    cv2.imshow("Transformed", transformed)


cv2.waitKey(0)
cv2.destroyAllWindows()