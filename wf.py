import requests
from pypdf import PdfReader
import re
import pandas as pd
from pdf_menager import Pdf_menager
from pe_activities import PeActivities
from ui import UI

def main():
    Pdf_menager.get_info()
    Pdf_menager.download()
    text = Pdf_menager.convert_to_text()

    lines_list = text.splitlines()

    all_pe_activities : PeActivities = PeActivities()

    all_pe_activities.add_list(lines_list)

    #all_pe_activities.print_activities()

    #UI.show_cancelled_classes(all_pe_activities.find_cancelled())

    UI.filtering(all_pe_activities,place="P-23")

    Pdf_menager.remove_file()

if __name__ == "__main__":
    main()

