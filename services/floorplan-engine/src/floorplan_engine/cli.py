
from floorplan_engine.config import (
    TEST_PDF,
    EXPORT_FILE,
    CROP_FILE,
    BINARY_FILE,
    CLEAN_FILE,
    COMPONENTS_FILE,
    MIN_COMPONENT_AREA,
    COMPONENTS_CSV,
    DEBUG_COMPONENT_IDS,
)

from floorplan_engine.core.context import ProcessingContext
from floorplan_engine.core.pipeline import Pipeline
from floorplan_engine.steps.pdf_export_step import PDFExportStep
from floorplan_engine.steps.crop_step import CropStep
from floorplan_engine.steps.threshold_step import ThresholdStep
from floorplan_engine.steps.morphology_step import MorphologyStep
from floorplan_engine.processors.wall_detector import WallDetector
from floorplan_engine.analyzers.component_analyzer import ComponentAnalyzer
from floorplan_engine.analyzers.wall_classifier import WallClassifier
from floorplan_engine.visualizers.component_visualizer import ComponentVisualizer


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
    # Component Detection
    # -----------------------------
    detector = WallDetector(CLEAN_FILE)

    detector.load()

    detector.find_components()

    # -----------------------------
    # Debug visualization
    # -----------------------------
    visualizer = ComponentVisualizer(
        detector.image,
        detector.stats,
    )

    visualizer.draw_ids(DEBUG_COMPONENT_IDS)

    # -----------------------------
    # Component analysis
    # -----------------------------
    analyzer = ComponentAnalyzer(detector)

    components = analyzer.build_components()

    print()

    print("===== CONTOUR TEST =====")

    for c in components[:5]:

        if c.contour is None:
            print(f"{c.id}: contour=None")

        else:
            print(
                f"{c.id}: points={len(c.contour)}"
            )


    print(f"\nComponents: {len(components)}")
    print(components[0])

    analyzer.export_csv(COMPONENTS_CSV)

    # -----------------------------
    # Classification
    # -----------------------------
    #from analyzers.wall_classifier import WallClassifier

    classifier = WallClassifier(components)

    classifier.classify()

    # -----------------------------
    # Statistics
    # -----------------------------
    walls = sum(1 for c in components if c.cls == "WALL")
    others = sum(1 for c in components if c.cls == "OTHER")

    print("\n==============================")
    print("CLASSIFICATION")
    print("==============================")
    print(f"WALLS : {walls}")
    print(f"OTHERS: {others}")

    print("\nDetected WALL components:\n")

    for c in components:
        if c.cls == "WALL":
            print(c)

    # -----------------------------
    # Debug image
    # -----------------------------
    detector.filter_components(
        min_area=MIN_COMPONENT_AREA,
        output_path=COMPONENTS_FILE,
    )



if __name__ == "__main__":
    main()