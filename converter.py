import os
from util import prepDir
import fitz

pdf_directory = "./assets/papers/IJCNLP/pdf/"
txt_directory = "./assets/papers/IJCNLP/txt/"
xml_directory = "./assets/papers/IJCNLP/xml/"

def convertPapers() -> None:
    for _, pdf_file_name in enumerate(os.listdir(pdf_directory)):
        suffix = pdf_file_name[pdf_file_name.index("doc") + 3:pdf_file_name.index(".pdf")]
        pdf_file_path = os.path.join(pdf_directory, f"doc{suffix}.pdf")

        if os.path.isfile(pdf_file_path):
            with fitz.Document(pdf_file_path) as pdf_file:
                with open(os.path.join(txt_directory, f"txt{suffix}.txt"), "w", encoding="utf-8") as txt_output_file:
                    text = ""
                    for page in pdf_file:
                        text += page.get_text("text")

                    txt_output_file.write(text)
            
                with open(os.path.join(xml_directory, f"xml{suffix}.xml"), "w", encoding="utf-8") as xml_output_file:
                    xml = ""
                    for page in pdf_file:
                        xml += page.get_text("xml")

                    xml_output_file.write(xml)

    
def convert():
    prepDir([txt_directory, xml_directory])
    convertPapers()

if __name__ == "__main__" :
        convert()
