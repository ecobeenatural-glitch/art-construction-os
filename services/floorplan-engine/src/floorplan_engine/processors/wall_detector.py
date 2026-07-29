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

     