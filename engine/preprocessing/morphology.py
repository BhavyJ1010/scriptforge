import cv2

def morphological_close(image, kernel_size=(5,5)):
    """
    Close small gaps in edges.
    """

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size)

    return cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)