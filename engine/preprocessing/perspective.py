import cv2
import numpy as np

def order_points(points):
    """
    Order points as:
    top-left,
    top-right,
    bottom-right,
    bottom-left
    """

    rect = np.zeros((4, 2), dtype="float32")

    s = points.sum(axis=1)

    rect[0] = points[np.argmin(s)] #top-left
    rect[2] = points[np.argmax(s)] #bottom-right

    diff = np.diff(points, axis=1)

    rect[1] = points[np.argmin(diff)] #top-right
    rect[3] = points[np.argmax(diff)] #bottom-left

    return rect

def four_point_transform(image, corners):
    """
    Apply perspective transform using four ordered corners.
    """
    (tl, tr, br, bl) = corners
    width_top = np.linalg.norm(tr - tl)
    width_bottom = np.linalg.norm(br - bl)

    max_width = int(max(width_top, width_bottom))

    height_left = np.linalg.norm(bl - tl)
    height_right = np.linalg.norm(br - tr)

    max_height = int(max(height_left, height_right))

    destination = np.array([
    [0, 0],
    [max_width - 1, 0],
    [max_width - 1, max_height - 1],
    [0, max_height - 1]
    ], dtype=np.float32)

    matrix = cv2.getPerspectiveTransform(
    corners.astype(np.float32),
    destination
    )

    warped = cv2.warpPerspective(
    image,
    matrix,
    (max_width, max_height)
    )

    return warped