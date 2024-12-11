import requests
from pypdf import PdfReader
import re
import os

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
    
    @staticmethod
    def remove_file() -> None:
        if os.path.exists("/Users/micha/Desktop/fakultetZima.pdf"):
            os.remove("/Users/micha/Desktop/fakultetZima.pdf")
        else:
            print("The file does not exist")
    
def main() -> None:
    Pdf_menager.get_info()
    Pdf_menager.download()
    text = Pdf_menager.convert_to_text()
    print(text)
    Pdf_menager.remove_file()

if __name__ == "__main__":
    main()