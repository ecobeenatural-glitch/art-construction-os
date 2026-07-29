from core.base_step import BaseStep
from processors.image_cropper import ImageCropper


class CropStep(BaseStep):

    def __init__(self, output_path):
        self.output_path = output_path

    def run(self, context):

        cropper = ImageCropper(context.page_image)

        cropper.crop_white_margins(self.output_path)

        context.cropped_image = self.output_path

        