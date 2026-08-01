import cv2
import numpy as np
import csv

class WallDetector:

    def __init__(self, image_path):
        self.image_path = image_path

    def load(self):

        image = cv2.imread(
            str(self.image_path),
            cv2.IMREAD_GRAYSCALE,
        )

        if image is None:
            raise FileNotFoundError(self.image_path)

        self.image = image

        print(f"Loaded image: {image.shape}")

    def find_components(self):

        num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(
            self.image,
            connectivity=8,
        )

        print(f"Connected components: {num_labels}")

        self.labels = labels
        self.stats = stats
        self.centroids = centroids    
 

    def filter_components(self, min_area, output_path):

        result = np.zeros_like(self.image)

        kept = 0

        for label in range(1, len(self.stats)):

            area = self.stats[label, cv2.CC_STAT_AREA]

            if area >= min_area:

                result[self.labels == label] = 255
                kept += 1

        cv2.imwrite(str(output_path), result)

        print(f"Large components: {kept}")
        print(f"Saved -> {output_path}") 

    def find_contour(self, component_id):

        import numpy as np
        import cv2

        mask = np.uint8(self.labels == component_id) * 255

        contours, _ = cv2.findContours(
            mask,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE,
        )

        if not contours:
            return None

        return max(contours, key=cv2.contourArea)   

    def extract_component_mask(self, label):

        import numpy as np

        mask = np.zeros_like(self.labels, dtype="uint8")

        mask[self.labels == label] = 255

        return mask

    def find_component_contour(self, label):

        import cv2

        mask = self.extract_component_mask(label)

        contours, _ = cv2.findContours(
            mask,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE,
        )

        if len(contours) == 0:
            return None

        return max(contours, key=cv2.contourArea)

     