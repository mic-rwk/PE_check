from pe_activities import PeActivities
import re
from datetime import *

class UI:
    
    @staticmethod
    def show_upcoming_week(all_classes : PeActivities):
        today = date.today().weekday()
        today_date = date.today()
        pattern = "Filia"
        dates = [] # list with classes with dates

        day_offset = 0  # counter of day shift
        for i, activity in enumerate(all_classes.get_activities()):     #print days (today) - Friday
            if all_classes.return_activity_index(i) >= today and not re.search(pattern, all_classes.get_acivity(i)):
                if i > 0:
                    if all_classes.return_activity_index(i) != all_classes.return_activity_index(i - 1) and all_classes.return_activity_index(i - 1) >= today:
                        day_offset += 1
                current_date = today_date + timedelta(days=day_offset)       
                dates.append(f"{activity} {current_date.strftime('%d.%m.%Y')}")

            
    @staticmethod
    def show_cancelled_classes(all_classes : list[PeActivities]):
        print(*all_classes, sep='\n')

    @staticmethod
    def filtering(all_classes : PeActivities, cancelled_classes : PeActivities): #by day, time, place, sports and combined
        pass

    @staticmethod
    def show_tommorow_classes(all_classes : PeActivities, cancelled_classes : PeActivities):
        pass

def main():
   example_list = ["dzien itd",
                  "wtorek 18:50-20:20 P-23 2.0.17 siłownia Jan Kowalski",
                  "piątek 18:50-20:20 P-23 2.0.17 siłownia Piotr Nowak",
                  "poniedziałek 18:50-20:20 P-23 2.0.17 siłownia Błażej Andrzej 17.12.2024 odwołane"]
   example_activities = PeActivities()
   example_activities.add_list(example_list)
   #cancelled_classes = example_activities.find_cancelled()
   #UI.show_cancelled_classes(cancelled_classes)

   UI.show_upcoming_week(example_activities)

if __name__ == "__main__":
   main()