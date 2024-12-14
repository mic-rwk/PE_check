from pe_activities import PeActivities
import re

class UI:
    
    @staticmethod
    def show_upcoming_week(all_classes : PeActivities, cancelled_classes : PeActivities):
        pass

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
    pass

if __name__ == "__main__":
   main()