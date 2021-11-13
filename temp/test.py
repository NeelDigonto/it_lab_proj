import sys
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
import io


def pdfparser(data):
    f = open("demofile2.txt", "w", encoding="utf-8")

    fp = open(data, 'rb')
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    # codec=codec,
    #device = TextConverter(rsrcmgr, retstr, laparams=laparams, codec=codec)
    device = XMLConverter(rsrcmgr, retstr,  laparams=laparams, codec=codec)
    #device = HTMLConverter(rsrcmgr, retstr, laparams=laparams, codec=codec)

    # Create a PDF interpreter object.
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    # Process each page contained in the document.

    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)
        data = retstr.getvalue()

        # print(data)
        f.write(data)

    f.close()




if __name__ == '__main__':
    pdfparser("./assets/papers/IJCNLP/2019/D19-1001.pdf")