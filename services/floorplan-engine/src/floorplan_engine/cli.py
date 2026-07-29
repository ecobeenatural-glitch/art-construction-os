from processors.pdf_reader import PDFReader
#from image_analyzer import ImageAnalyzer
from processors.image_cropper import ImageCropper
#from drawing_inspector import DrawingInspector
from processors.threshold import ThresholdProcessor
from processors.morphology import MorphologyProcessor




from config import (
    TEST_PDF,
    EXPORT_FILE,
    CROP_FILE,
    BINARY_FILE,
    CLEAN_FILE,
    COMPONENTS_FILE,
    MIN_COMPONENT_AREA,
    COMPONENTS_CSV,
)

from core.context import ProcessingContext
from core.pipeline import Pipeline
from steps.pdf_export_step import PDFExportStep
from steps.crop_step import CropStep
#from steps.inspector_step import InspectorStep
from steps.threshold_step import ThresholdStep
from steps.morphology_step import MorphologyStep
from processors.wall_detector import WallDetector
from analyzers.component_analyzer import ComponentAnalyzer


OUTPUT = EXPORT_FILE


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
            output_path=CROP_FILE,
        )
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
    #analyzer = ImageAnalyzer(context.page_image)
    #analyzer.info()

    detector = WallDetector(CLEAN_FILE)
    detector.load()
    detector.find_components()

    analyzer = ComponentAnalyzer(
        detector.labels,
        detector.stats,
    )

    analyzer.export_csv(COMPONENTS_CSV)


    detector.filter_components(
        min_area=MIN_COMPONENT_AREA,
        output_path=COMPONENTS_FILE,
    )



if __name__ == "__main__":
    main()