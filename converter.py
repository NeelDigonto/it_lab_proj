from io import StringIO
import os

from pdfminer.converter import TextConverter, XMLConverter, HTMLConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser



pdf_directory = "./assets/papers/IJCNLP/pdf/"
txt_directory = "./assets/papers/IJCNLP/txt/"
xml_directory = "./assets/papers/IJCNLP/xml/"

    
for _, pdf_file_name in enumerate(os.listdir(pdf_directory)):
    suffix = pdf_file_name[pdf_file_name.index("doc") + 3:pdf_file_name.index(".pdf")]
    pdf_file_path = os.path.join(pdf_directory, f"doc{suffix}.pdf")

    if os.path.isfile(pdf_file_path):
        with open(pdf_file_path, "rb") as pdf_file:

            with open(os.path.join(txt_directory, f"txt{suffix}.txt"), "w", encoding="utf-8") as txt_output_file:
                parser = PDFParser(pdf_file)
                doc = PDFDocument(parser)
                rsrcmgr = PDFResourceManager()
                codec = 'utf-8'
                device = TextConverter(rsrcmgr, txt_output_file, laparams=LAParams())
                interpreter = PDFPageInterpreter(rsrcmgr, device)
                for page in PDFPage.create_pages(doc):
                    interpreter.process_page(page)

            with open(os.path.join(xml_directory, f"txt{suffix}.xml"), "w", encoding="utf-8") as xml_output_file:
                parser = PDFParser(pdf_file)
                doc = PDFDocument(parser)
                rsrcmgr = PDFResourceManager()
                codec = 'utf-8'
                device = XMLConverter(rsrcmgr, xml_output_file, laparams=LAParams())
                interpreter = PDFPageInterpreter(rsrcmgr, device)
                for page in PDFPage.create_pages(doc):
                    interpreter.process_page(page)
    
