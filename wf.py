import requests
from pypdf import PdfReader
import re
import pandas as pd

#pobieranie pliku
user_agent = "scrapping_script/1.0"
headers = {'User-Agent': user_agent}
URL = "https://swfis.pwr.edu.pl/fcp/BGBUKOQtTKlQhbx08SlkTWwVQX2o8DAoHNiwFE1wZDyEPG1gnBVcoFW8SBDRKTxMKRy0SODwBBAEIMQheCFVAORFCHzY/81/public/konsultacje/fakultety_24z.pdf"
r = requests.get(URL, headers=headers, stream = True)
with open("/Users/micha/Desktop/fakultetZima.pdf", "wb") as fd:
    fd.write(r.content)

reader = PdfReader('/Users/micha/Desktop/fakultetZima.pdf')

page = reader.pages[0]

text = page.extract_text()

pattern = "odwołane"
pattern_2 = r"\d{2}.\d{2}.\d{4}"

print(text)

print('\n')

cancelled_classes : str = []

lines_list = text.splitlines()

for i in range(1, len(lines_list)): 
    current_line = lines_list[i]
    previous_line = lines_list[i - 1]
    
    if re.search(pattern, current_line):
        if len(current_line) > len(pattern):
            cancelled_classes.append(current_line)
    
    elif re.search(pattern_2, current_line):
        text_with_date =  previous_line + " " + current_line 
        cancelled_classes.append(text_with_date) 

print(*cancelled_classes, sep ="\n")

