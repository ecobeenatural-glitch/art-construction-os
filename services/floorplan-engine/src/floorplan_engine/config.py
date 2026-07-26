from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[4]

SAMPLES_DIR = PROJECT_ROOT / "samples"
INPUT_DIR = SAMPLES_DIR / "input"
OUTPUT_DIR = SAMPLES_DIR / "output"

# Автоматично створюємо папку output
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

TEST_PDF = INPUT_DIR / "GC_136_clear.pdf"