from pathlib import Path
import fitz


class PDFReader:
    """Reads PDF floor plans and exports pages as images."""

    def __init__(self, pdf_path: Path):
        self.pdf_path = pdf_path
        self.doc = fitz.open(pdf_path)

    @property
    def page_count(self) -> int:
        return self.doc.page_count

    def export_page(
        self,
        page_number: int,
        output_path: Path,
        dpi: int = 300,
    ) -> Path:
        page = self.doc.load_page(page_number)

        zoom = dpi / 72
        matrix = fitz.Matrix(zoom, zoom)

        pix = page.get_pixmap(matrix=matrix)

        output_path.parent.mkdir(parents=True, exist_ok=True)

        pix.save(output_path)

        return output_path

    def close(self):
        self.doc.close()