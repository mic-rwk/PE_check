from pe_activities import PeActivities
import re
from datetime import *

class UI:
    
    @staticmethod
    def show_upcoming_week(all_classes : PeActivities):
        today = date.today().weekday()
        if(today == 5 or today == 6):
            today = 0
        i : int = 0
        while i < len(all_classes.get_activities()):       #zajęcia do piątku włącznie
            if all_classes.return_activity_index(i) >= today:
                print(all_classes.activities[i])
            i += 1

        i = 0
        while i < len(all_classes.get_activities()):    #nowy tydzien
            if all_classes.return_activity_index(i) <= today:
                print(all_classes.activities[i])
            i += 1
            
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