from pdf_reader import PDFReader
from image_analyzer import ImageAnalyzer
from config import TEST_PDF, OUTPUT_DIR

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


if __name__ == "__main__":
    main()