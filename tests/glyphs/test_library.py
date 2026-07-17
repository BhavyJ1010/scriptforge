from pathlib import Path

from engine.preprocessing.loader import load_image
from engine.preprocessing.pipeline import preprocess_document
from engine.segmentation.connected_components import segment_characters
from engine.glyphs.cleaning import clean_glyph_boxes
from engine.glyphs.library import save_glyphs

from config.paths import SAMPLES_DIR
from config.paths import GLYPHS_DIR

image = load_image(SAMPLES_DIR / "3.jpeg")

binary = preprocess_document(image)["binary"]

boxes = segment_characters(binary) # Character Segmentation

print(f"Detected components : {len(boxes)}")

clean_boxes = clean_glyph_boxes(boxes) # Glyph Cleaning

print(f"After cleaning      : {len(clean_boxes)}")
print(f"Removed             : {len(boxes) - len(clean_boxes)}")

save_glyphs(
    binary,
    clean_boxes,
    GLYPHS_DIR,
)