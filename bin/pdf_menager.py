import requests
from pypdf import PdfReader
import re
import os

class Pdf_menager:
    
    user_agent = "scrapping_script/1.0"
    headers = {'User-Agent': user_agent}
    url = "https://swfis.pwr.edu.pl/fcp/BGBUKOQtTKlQhbx08SlkTWwVQX2o8DAoHNiwFE1wZDyEPG1gnBVcoFW8SBDRKTxMKRy0SODwBBAEIMQheCFVAORFCHzY/81/public/konsultacje/fakultety_24z.pdf"
    reader : PdfReader
    path : str = "/Users/" + os.getlogin() + "/Desktop/fakultetZima.pdf"

    @classmethod
    def get_info(cls) -> None:
        r = requests.get(cls.url, headers=cls.headers, stream = True)
        with open(cls.path, "wb") as fd:
            fd.write(r.content)

#'/Users/micha/Desktop/fakultetZima.pdf'
    @classmethod
    def download(cls) -> None:
        cls.reader = PdfReader(cls.path)

    @classmethod
    def convert_to_text(cls) -> str:
        page = cls.reader.pages[0]
        text = page.extract_text()
        return text
    
    @classmethod
    def remove_file(cls) -> None:
        if os.path.exists(cls.path):
            os.remove(cls.path)
        else:
            print("The file does not exist")
    
def main() -> None:
    Pdf_menager.get_info()
    Pdf_menager.download()
    text = Pdf_menager.convert_to_text()
    print(text)
    print('\n')
    Pdf_menager.remove_file()
    

if __name__ == "__main__":
    main()