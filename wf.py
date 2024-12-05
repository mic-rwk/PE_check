import requests
from pypdf import PdfReader
import re
import pandas as pd
from pdf_menager import Pdf_menager

Pdf_menager.get_info()
Pdf_menager.download()
text = Pdf_menager.convert_to_text()

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

