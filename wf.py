import requests
from pypdf import PdfReader
import re
import pandas as pd
from pdf_menager import Pdf_menager
from pe_activities import PeActivities

def main():
    Pdf_menager.get_info()
    Pdf_menager.download()
    text = Pdf_menager.convert_to_text()

    pattern = "odwołane"
    pattern_2 = r"\d{2}.\d{2}.\d{4}"

    lines_list = text.splitlines()

    all_pe_activities : PeActivities = PeActivities()
    deleted_pe_activities : PeActivities = PeActivities()

    for i in range(1, len(lines_list)): 
        current_line = lines_list[i]
        previous_line = lines_list[i - 1]

        all_pe_activities.add_activities(current_line)
        
        if re.search(pattern, current_line):
            if len(current_line) > len(pattern):
                deleted_pe_activities.add_activities(current_line)
        
        elif re.search(pattern_2, current_line):
            text_with_date =  previous_line + " " + current_line  
            deleted_pe_activities.add_activities(previous_line)

    deleted_pe_activities.print_activities()

    Pdf_menager.remove_file()

if __name__ == "__main__":
    main()

