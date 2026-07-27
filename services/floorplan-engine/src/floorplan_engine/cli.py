from pdf_reader import PDFReader
from image_analyzer import ImageAnalyzer
from image_cropper import ImageCropper
from drawing_inspector import DrawingInspector
from threshold import ThresholdProcessor
from morphology import MorphologyProcessor





from config import (
    TEST_PDF,
    OUTPUT_DIR,
    CROPPED_FILE,
    BINARY_FILE,
    CLEAN_FILE,
)

from core.context import ProcessingContext
from core.pipeline import Pipeline
from steps.pdf_export_step import PDFExportStep
from steps.crop_step import CropStep
from steps.inspector_step import InspectorStep
from steps.threshold_step import ThresholdStep
from steps.morphology_step import MorphologyStep


OUTPUT = OUTPUT_DIR / "page_001.png"


def main():

    # -----------------------------
    # Pipeline
    # -----------------------------
    context = ProcessingContext()

    pipeline = Pipeline()

    pipeline.add(
        PDFExportStep(
            pdf_path=TEST_PDF,
            output_path=OUTPUT,
            dpi=300,
        )
    )

    pipeline.add(
        CropStep(
            output_path=CROPPED_FILE,
        )
    )

    pipeline.add(
        InspectorStep()
    )

    pipeline.add(
        ThresholdStep(
            output_path=BINARY_FILE,
        )
    )

    pipeline.add(
        MorphologyStep(
            output_path=CLEAN_FILE,
        )
    )

    pipeline.run(context)

    # -----------------------------
    # Existing processing
    # -----------------------------
    analyzer = ImageAnalyzer(context.page_image)
    analyzer.info()



if __name__ == "__main__":
    main()