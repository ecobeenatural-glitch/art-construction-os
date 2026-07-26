from pathlib import Path
from PIL import Image


class ImageAnalyzer:

    def __init__(self, image_path: Path):
        self.image_path = image_path
        self.image = Image.open(image_path)

    def info(self):

        width, height = self.image.size

        print("=" * 50)
        print("IMAGE INFORMATION")
        print("=" * 50)

        print(f"File      : {self.image_path.name}")
        print(f"Size      : {width} x {height}")
        print(f"Mode      : {self.image.mode}")

        dpi = self.image.info.get("dpi", "Unknown")
        print(f"DPI       : {dpi}")

        print("=" * 50)