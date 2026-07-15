import cv2


def resize_image(image, width=1000):
    """
    Resize an image while preserving aspect ratio.
    """

    height, current_width = image.shape[:2]

    scale = width / current_width

    new_height = int(height * scale)

    resized_image = cv2.resize(image,(width, new_height))

    return resized_image