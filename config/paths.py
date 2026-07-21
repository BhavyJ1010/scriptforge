from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"

INPUT_DIR = DATA_DIR / "input"
SAMPLES_DIR = DATA_DIR / "samples"
TEMPLATES_DIR = DATA_DIR / "templates"
PROCESSED_DIR = DATA_DIR / "processed"
DEBUG_DIR = DATA_DIR / "debug"

OUTPUT_DIR = DATA_DIR / "output"

GLYPHS_DIR = OUTPUT_DIR / "glyphs"
PAGES_DIR = OUTPUT_DIR / "pages"
WRITER_PROFILES_DIR = OUTPUT_DIR / "writer_profiles"
EXPORTS_DIR = OUTPUT_DIR / "exports"