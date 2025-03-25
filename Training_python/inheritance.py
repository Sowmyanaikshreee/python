class Vehicle:
    def general_usage(self):
        print("general use: transportation")

class car(Vehicle):
    def __init__(self):
        print("I'm a car")
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):
        print("Commute to work and vacate family")


class Motor(Vehicle):
    def __init__(self):
        print("I'm motor")
        self.wheels = 2
        self.has_roof = False

    def specific_usage(self):
        print("go for  riding")

c = car()
c.general_usage()
c.specific_usage() 

m = Motor()
m.general_usage()
m.specific_usage()
