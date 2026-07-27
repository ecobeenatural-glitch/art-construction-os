from pathlib import Path

import cv2
import numpy as np


class DrawingInspector:

    def __init__(self, image_path: Path):
        self.image = cv2.imread(str(image_path))

        if self.image is None:
            raise FileNotFoundError(image_path)

    def report(self):

        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        height, width = gray.shape

        black = np.sum(gray < 245)
        white = np.sum(gray >= 245)

        total = black + white

        black_percent = black / total * 100
        white_percent = white / total * 100

        print()
        print("=" * 50)
        print("DRAWING REPORT")
        print("=" * 50)

        print(f"Image size   : {width} x {height}")
        print(f"Black pixels : {black_percent:.2f}%")
        print(f"White pixels : {white_percent:.2f}%")
        print(f"Aspect ratio : {width / height:.3f}")

        print("=" * 50)