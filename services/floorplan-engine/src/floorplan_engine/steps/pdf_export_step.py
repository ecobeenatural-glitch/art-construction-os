from core.base_step import BaseStep
from processors.pdf_reader import PDFReader


class PDFExportStep(BaseStep):

    def __init__(self, pdf_path, output_path, dpi=300):
        self.pdf_path = pdf_path
        self.output_path = output_path
        self.dpi = dpi

    def run(self, context):

        reader = PDFReader(self.pdf_path)

        print(f"Pages: {reader.page_count}")

        reader.export_page(
            page_number=0,
            output_path=self.output_path,
            dpi=self.dpi,
        )

        reader.close()

        context.page_image = self.output_path

        print(f"Saved -> {self.output_path}")        