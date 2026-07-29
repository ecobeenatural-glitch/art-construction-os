import csv
import cv2


class ComponentAnalyzer:

    def __init__(self, labels, stats):
        self.labels = labels
        self.stats = stats

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