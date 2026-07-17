from pathlib import Path
import cv2


def save_glyphs(binary_image, boxes, output_folder):
    """
    Save each extracted glyph as an individual image.

    Parameters
    ----------
    binary_image : numpy.ndarray
        Binary document image.

    boxes : list
        List of bounding boxes (x, y, w, h).

    output_folder : str | Path
        Folder where glyph images will be saved.
    """

    output_folder = Path(output_folder)
    output_folder.mkdir(parents=True, exist_ok=True)

    padding = 5

    for i, (x, y, w, h) in enumerate(boxes, start=1):

        glyph = binary_image[y:y+h, x:x+w]

        glyph = cv2.copyMakeBorder(
            glyph,
            padding,
            padding,
            padding,
            padding,
            cv2.BORDER_CONSTANT,
            value=255,
        )

        filename = output_folder / f"glyph_{i:04d}.png"

        cv2.imwrite(str(filename), glyph)

    print(f"Saved {len(boxes)} glyph(s) to '{output_folder}'.")