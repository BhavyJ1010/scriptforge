import cv2

def normalize_lighting(image):
    """
    Improve contrast using histogram equalization.
    """

    return cv2.equalizeHist(image)