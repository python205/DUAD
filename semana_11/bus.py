class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []

    def add_passenger(self, person):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print(f"{person.name} boarded the bus.")
        else:
            print("The bus is full.")

    def remove_passenger(self):
        if self.passengers:
            removed = self.passengers.pop()
            print(f"{removed.name} got off the bus.")
        else:
            print("The bus is empty.")
