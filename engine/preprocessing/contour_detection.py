import cv2


def find_contours(edge_image):
    """
    Find all contours in an edge image.
    """

    contours, hierarchy = cv2.findContours(edge_image, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    return contours

def sort_contours_by_area(contours):
    """
    Sort contours from largest to smallest.
    """

    return sorted(contours, key=cv2.contourArea, reverse=True)

def approximate_contour(contour):
    """
    Approximate a contour to a polygon.
    """

    perimeter = cv2.arcLength(contour, True)

    approximation = cv2.approxPolyDP(contour, 0.02 * perimeter, True)

    return approximation