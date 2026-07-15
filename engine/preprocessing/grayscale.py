import cv2

def to_grayscale(image):
    """
    Convert a BGR image to grayscale.
    """

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    return gray