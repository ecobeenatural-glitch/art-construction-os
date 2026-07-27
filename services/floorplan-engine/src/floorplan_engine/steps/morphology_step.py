from core.base_step import BaseStep
from morphology import MorphologyProcessor


class MorphologyStep(BaseStep):

    def __init__(self, output_path):
        self.output_path = output_path

    def run(self, context):

        morph = MorphologyProcessor(context.binary_image)

        morph.clean(self.output_path)

        context.cleaned_image = self.output_path