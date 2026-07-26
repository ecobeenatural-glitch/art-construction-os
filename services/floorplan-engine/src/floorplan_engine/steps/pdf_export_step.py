from core.base_step import BaseStep
from pdf_reader import PDFReader  



class PDFExportStep(BaseStep):

    def run(self, context):
        print("PDFExportStep")  