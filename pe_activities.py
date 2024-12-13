import re

class PeActivities:
    def __init__(self):
        self.activities : str = []

    def add_activities(self, activity : str) -> None:
        self.activities.append(activity)

    def add_list(self, lines_list : list) -> None:
        for i in range(1, len(lines_list)):
            current_line = lines_list[i]
            self.add_activities(current_line)
    
    def print_activities(self) -> None:
        print(*self.activities, sep ="\n")
        
def main():
    example = PeActivities()
    example.add_activities("Przykładowe zajęcia odwołane")
    example.add_activities("Trening siłowy")
    example.print_activities()

if __name__ == "__main__":
   main()