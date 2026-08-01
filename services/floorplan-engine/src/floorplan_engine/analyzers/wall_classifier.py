class WallClassifier:

    def __init__(self, components):

        self.components = components

    def classify(self):

        for component in self.components:

            area = component.area
            width = component.width
            height = component.height
            fill = component.fill_ratio

            if (
                area > 50000
                and fill > 0.80
                and (width > 80 or height > 80)
            ):
                component.cls = "WALL"

            else:
                component.cls = "OTHER"

        print("Classification complete.")