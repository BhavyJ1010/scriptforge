import cv2

def gaussian_blur(image):
    """
    smoothes the image using gaussian blur - weighted average of intensities of neighbouring pixels 
    """

    blurred = cv2.GaussianBlur(image, (5, 5), 0)

    return blurred