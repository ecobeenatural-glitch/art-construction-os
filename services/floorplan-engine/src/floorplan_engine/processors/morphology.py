from pathlib import Path

import cv2
import numpy as np


class MorphologyProcessor:

    def __init__(self, image_path: Path):
        self.image_path = image_path

    def clean(self, output_path: Path):

        image = cv2.imread(
            str(self.image_path),
            cv2.IMREAD_GRAYSCALE,
        )

        kernel = np.ones((3, 3), np.uint8)

        cleaned = cv2.morphologyEx(
            image,
            cv2.MORPH_CLOSE,
            kernel,
        )

        cv2.imwrite(str(output_path), cleaned)

        print(f"Clean -> {output_path}")