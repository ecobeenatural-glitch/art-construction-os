from core.base_step import BaseStep
from threshold import ThresholdProcessor


class ThresholdStep(BaseStep):

    def __init__(self, output_path):
        self.output_path = output_path

    def run(self, context):

        threshold = ThresholdProcessor(context.cropped_image)

        threshold.otsu(self.output_path)

        context.binary_image = self.output_path