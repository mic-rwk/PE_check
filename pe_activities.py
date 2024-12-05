
class PeActivities:
    def __init__(self):
        self.activities : str = []

    def add_activities(self, activity : str) -> None:
        self.activities.append(activity)
    
    def print_activities(self) -> None:
        print(*self.activities, sep ="\n")
        
def main():
    example = PeActivities()
    example.add_activities("Przykładowe zajęcia odwołane")
    example.add_activities("Trening siłowy")
    example.print_activities()

if __name__ == "__main__":
   main()