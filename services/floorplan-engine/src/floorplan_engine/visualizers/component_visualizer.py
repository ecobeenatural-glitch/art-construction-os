import cv2


class ComponentVisualizer:

    def __init__(self, image, stats):

        self.image = image.copy()
        self.stats = stats

    def draw_ids(self, output_path):

        for label in range(1, len(self.stats)):

            x = self.stats[label, cv2.CC_STAT_LEFT]
            y = self.stats[label, cv2.CC_STAT_TOP]
            w = self.stats[label, cv2.CC_STAT_WIDTH]
            h = self.stats[label, cv2.CC_STAT_HEIGHT]

            cv2.rectangle(
                self.image,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2,
            )

            cv2.putText(
                self.image,
                str(label),
                (x, y - 5),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 0, 255),
                1,
                cv2.LINE_AA,
            )

        cv2.imwrite(str(output_path), self.image)

        print(f"Saved -> {output_path}")