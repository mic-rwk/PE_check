import requests
from pypdf import PdfReader
import re

class Pdf_menager:
    user_agent = "scrapping_script/1.0"
    headers = {'User-Agent': user_agent}
    url = "https://swfis.pwr.edu.pl/fcp/BGBUKOQtTKlQhbx08SlkTWwVQX2o8DAoHNiwFE1wZDyEPG1gnBVcoFW8SBDRKTxMKRy0SODwBBAEIMQheCFVAORFCHzY/81/public/konsultacje/fakultety_24z.pdf"
    reader : PdfReader

    @staticmethod
    def get_info() -> None:
        r = requests.get(Pdf_menager.url, headers=Pdf_menager.headers, stream = True)
        with open("/Users/micha/Desktop/fakultetZima.pdf", "wb") as fd:
            fd.write(r.content)

#'/Users/micha/Desktop/fakultetZima.pdf'
    @staticmethod
    def download() -> None:
        Pdf_menager.reader = PdfReader('/Users/micha/Desktop/fakultetZima.pdf')

    @staticmethod
    def convert_to_text() -> str:
        page = Pdf_menager.reader.pages[0]
        text = page.extract_text()
        return text
    
if __name__ == "__main__":
    Pdf_menager.get_info()
    Pdf_menager.download()
    text = Pdf_menager.convert_to_text()