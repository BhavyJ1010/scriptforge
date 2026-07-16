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
from engine.preprocessing.lighting import normalize_lighting
from engine.preprocessing.threshold import adaptive_threshold


def preprocess_document(image):
    """
    Complete preprocessing pipeline for a document image.
    Returns all important intermediate stages.
    """

    # Resize
    resized = resize_image(image)

    # Basic preprocessing
    gray = to_grayscale(resized)
    blurred = gaussian_blur(gray)
    edged = detect_edges(blurred)
    morphed = morphological_close(edged)

    warped = resized

    # Try perspective correction
    contours = find_contours(morphed)
    sorted_contours = sort_contours_by_area(contours)

    if sorted_contours:
        approx = approximate_contour(sorted_contours[0])

        if len(approx) == 4:
            corners = approx.reshape(4, 2)
            ordered = order_points(corners)
            warped = four_point_transform(resized, ordered)

    # Final preprocessing
    warped_gray = to_grayscale(warped)
    normalized = normalize_lighting(warped_gray)
    binary = adaptive_threshold(normalized)

    

    return {
        "resized": resized,
        "gray": gray,
        "edges": edged,
        "page": warped,
        "normalized": normalized,
        "binary": binary,
    }