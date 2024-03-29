import os
import time
import multiprocessing
from util import prepDir
import fitz
from util import _FILE_PREFIX_
from util import _FILE_PREFIX_LEN_

pdf_directory = "./assets/papers/IJCNLP/pdf/"
txt_directory = "./assets/papers/IJCNLP/txt/"
xml_directory = "./assets/papers/IJCNLP/xml/"

_PAR_COUNT_ = multiprocessing.cpu_count() * 2


def convertPaper(pdf_file_name) -> None:
    suffix = pdf_file_name[pdf_file_name.index(
        f"{_FILE_PREFIX_}") + _FILE_PREFIX_LEN_:pdf_file_name.index(".pdf")]
    pdf_file_path = os.path.join(pdf_directory, f"{_FILE_PREFIX_}{suffix}.pdf")

    if os.path.isfile(pdf_file_path):
        with fitz.Document(pdf_file_path) as pdf_file:
            with open(os.path.join(txt_directory, f"{_FILE_PREFIX_}{suffix}.txt"), "w", encoding="utf-8") as txt_output_file:
                text: str = ""
                for page in pdf_file:
                    text += page.get_text("text")
                lines = text.split('.')
                text = ""
                for line in lines:
                    line = line.strip()
                    line = line.replace("\n", ' ')
                    text += line + ".\n"
                txt_output_file.write(text)

            with open(os.path.join(xml_directory, f"{_FILE_PREFIX_}{suffix}.xml"), "w", encoding="utf-8") as xml_output_file:
                xml = ""
                for page in pdf_file:
                    xml += page.get_text("xml")
                xml_output_file.write(xml)


def convertAllPapers():
    files_to_convert: list[str] = os.listdir(pdf_directory)
    with multiprocessing.Pool(processes=_PAR_COUNT_) as pool:
        pool.map(convertPaper, files_to_convert)


def convert():
    prepDir([txt_directory, xml_directory])

    print("Converting the downloaded Reseach Papers....")

    start_time = time.time()
    convertAllPapers()
    end_time = time.time()

    print("Ignore any \"mupdf: invalid page object\" message")
    print(f"Papers Converted in {end_time - start_time} seconds\n")


if __name__ == "__main__":
    convert()
