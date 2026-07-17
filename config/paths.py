from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"

INPUT_DIR = DATA_DIR / "input"
OUTPUT_DIR = DATA_DIR / "output"
SAMPLES_DIR = DATA_DIR / "samples"
PROCESSED_DIR = DATA_DIR / "processed"
TEMPLATES_DIR = DATA_DIR / "templates"
DEBUG_DIR = DATA_DIR / "debug"

GLYPHS_DIR = OUTPUT_DIR / "glyphs"
PAGES_DIR = OUTPUT_DIR / "pages"
PROFILES_DIR = OUTPUT_DIR / "writer_profiles"