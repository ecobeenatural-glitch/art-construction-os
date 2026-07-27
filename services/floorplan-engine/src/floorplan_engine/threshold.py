from pathlib import Path

import cv2


class ThresholdProcessor:

    def __init__(self, image_path: Path):
        self.image_path = image_path

    def otsu(self, output_path: Path):

        image = cv2.imread(str(self.image_path), cv2.IMREAD_GRAYSCALE)

        _, binary = cv2.threshold(
            image,
            0,
            255,
            cv2.THRESH_BINARY + cv2.THRESH_OTSU,
        )

        cv2.imwrite(str(output_path), binary)

        print(f"Binary -> {output_path}")