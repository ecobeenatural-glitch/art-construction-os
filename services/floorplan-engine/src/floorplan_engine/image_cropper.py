from pathlib import Path

import cv2


class ImageCropper:

    def __init__(self, image_path: Path):
        self.image_path = image_path

    def crop_white_margins(self, output_path: Path):

        image = cv2.imread(str(self.image_path))

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Все темніше майже білого вважаємо кресленням
        _, thresh = cv2.threshold(gray, 245, 255, cv2.THRESH_BINARY_INV)

        points = cv2.findNonZero(thresh)

        x, y, w, h = cv2.boundingRect(points)

        cropped = image[y:y+h, x:x+w]

        output_path.parent.mkdir(parents=True, exist_ok=True)

        cv2.imwrite(str(output_path), cropped)

        print(f"Cropped -> {output_path}")