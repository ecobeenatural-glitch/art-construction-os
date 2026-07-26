from pdf_reader import PDFReader
from image_analyzer import ImageAnalyzer
from config import TEST_PDF, OUTPUT_DIR
from image_cropper import ImageCropper
from config import TEST_PDF, OUTPUT_DIR, CROPPED_FILE



OUTPUT = OUTPUT_DIR / "page_001.png"


def main():

    reader = PDFReader(TEST_PDF)

    print(f"Pages: {reader.page_count}")

    reader.export_page(
        page_number=0,
        output_path=OUTPUT,
        dpi=300,
    )

    reader.close()

    print(f"Saved -> {OUTPUT}")

    analyzer = ImageAnalyzer(OUTPUT)

    analyzer.info()

    cropper = ImageCropper(OUTPUT)

    cropper.crop_white_margins(CROPPED_FILE)


if __name__ == "__main__":
    main()