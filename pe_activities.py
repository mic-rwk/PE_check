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

    def find_cancelled(self) -> list:
        pattern : str= "odwołane"
        pattern_2 : str = r"\d{2}.\d{2}.\d{4}"

        deleted_pe_activities : PeActivities = []

        for i in range(1, len(self.activities)): 
            current_line = self.activities[i]
            previous_line = self.activities[i - 1]
            
            if re.search(pattern, current_line):
                if len(current_line) > len(pattern):
                    deleted_pe_activities.append(current_line)
            
            elif re.search(pattern_2, current_line):
                text_with_date : str =  previous_line + " " + current_line  
                deleted_pe_activities.append(previous_line)
        
        return deleted_pe_activities
        
def main():
    example = PeActivities()
    example.add_activities("Przykładowe zajęcia odwołane")
    example.add_activities("poniedziałek 18:50-20:20 P-23 2.0.17 siłownia Banaszczyk Grzegorz 16.12.2024 odwołane")
    example.add_activities("Trening siłowy")
    print(*example.find_cancelled(), sep='\n')


if __name__ == "__main__":
   main()