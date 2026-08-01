import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

SRC = ROOT / "services" / "floorplan-engine" / "src"

sys.path.insert(0, str(SRC))

from floorplan_engine.cli import main

main()