import cv2

def detect_edges(image):
    """
    create all possible edges on all over the page
    """

    edges = cv2.Canny(image, 50, 150)

    return edges