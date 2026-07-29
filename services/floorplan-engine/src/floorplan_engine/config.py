from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[4]

SAMPLES_DIR = PROJECT_ROOT / "samples"

INPUT_DIR = SAMPLES_DIR / "input"

OUTPUT_DIR = SAMPLES_DIR / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

TEST_PDF = INPUT_DIR / "GC_136_clear.pdf"




DEBUG_DIR = OUTPUT_DIR / "debug"

DEBUG_DIR.mkdir(
    parents=True,
    exist_ok=True,
)

EXPORT_FILE = DEBUG_DIR / "01_export.png"

CROP_FILE = DEBUG_DIR / "02_crop.png"

BINARY_FILE = DEBUG_DIR / "03_binary.png"

CLEAN_FILE = DEBUG_DIR / "04_clean.png"

COMPONENTS_FILE = DEBUG_DIR / "05_components.png"

WALLS_FILE = DEBUG_DIR / "06_walls.png"

MIN_COMPONENT_AREA = 500

COMPONENTS_CSV = DEBUG_DIR / "components.csv"