import cv2

def adaptive_threshold(image):
    """
    Convert grayscale image into a binary image using adaptive thresholding.
    """

    return cv2.adaptiveThreshold(
        image,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        15,
        11
    )