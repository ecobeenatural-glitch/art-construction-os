from pathlib import Path


class ProcessingContext:

    def __init__(self):

        self.pdf_path = None

        self.page_image = None
        self.cropped_image = None
        self.binary_image = None
        self.cleaned_image = None

        self.metadata = {}