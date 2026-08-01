import csv
import cv2
from floorplan_engine.models import Component


class ComponentAnalyzer:

    def __init__(self, detector):
        self.detector = detector
        self.labels = detector.labels
        self.stats = detector.stats

    def build_components(self):

        components = []

        for label in range(1, len(self.stats)):

            left = int(self.stats[label][0])
            top = int(self.stats[label][1])
            width = int(self.stats[label][2])
            height = int(self.stats[label][3])
            area = int(self.stats[label][4])

            aspect = width / height if height else 0
            fill = area / (width * height) if width * height else 0


            contour = self.detector.find_component_contour(label)
            components.append(
                Component(
                    id=label,
                    area=area,
                    left=left,
                    top=top,
                    width=width,
                    height=height,
                    aspect_ratio=aspect,
                    fill_ratio=fill,
                    contour=contour,
                )
            )

        return components    

    def export_csv(self, csv_path):

        with open(csv_path, "w", newline="", encoding="utf-8") as f:

            writer = csv.DictWriter(
                f,
                fieldnames=[
                    "id",
                    "area",
                    "width",
                    "height",
                    "aspect_ratio",
                    "fill_ratio",
                    "left",
                    "top",
                ],
            )

            writer.writeheader()

            for label in range(1, len(self.stats)):

                x = self.stats[label, cv2.CC_STAT_LEFT]
                y = self.stats[label, cv2.CC_STAT_TOP]
                w = self.stats[label, cv2.CC_STAT_WIDTH]
                h = self.stats[label, cv2.CC_STAT_HEIGHT]
                area = self.stats[label, cv2.CC_STAT_AREA]

                writer.writerow(
                    {
                        "id": label,
                        "area": area,
                        "width": w,
                        "height": h,
                        "aspect_ratio": round(w / h, 3),
                        "fill_ratio": round(area / (w * h), 3),
                        "left": x,
                        "top": y,
                    }
                )

        print(f"CSV exported -> {csv_path}")