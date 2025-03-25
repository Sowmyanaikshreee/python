class Human:
    def __init__(self,n,o):
        self.name=n
        self.occupation=o

    def do_work(self):
        if self.occupation=="actor":
            print(self.name , "shoots fim")
        elif self.occupation=="tennis player":
            print(self.name, "plays tennis")       

    def speak(self):
        print(self.name , "says how are you")

Tom = Human("Tom cruise","actor") 
Tom.do_work()
Tom.speak()

Shree = Human("Sheeba","tennis player")
Shree.do_work()
Shree.speak()