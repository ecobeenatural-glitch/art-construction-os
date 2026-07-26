from pathlib import Path
import fitz  # PyMuPDF


def pdf_info(pdf_path: Path) -> None:
    """Print basic information about a PDF file."""

    doc = fitz.open(pdf_path)

    print(f"File: {pdf_path.name}")
    print(f"Pages: {doc.page_count}")

    doc.close()


if __name__ == "__main__":
    pdf = Path("samples/input/GC_136_clear.pdf")
    pdf_info(pdf)
