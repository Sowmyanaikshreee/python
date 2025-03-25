class Shree():
    def eating(self):
        print("Love eating")

class Sheeba():
    def singing(self):
        print("Love singing")

class Pvn(Shree, Sheeba):
    def playing(self):
        print("Love playing")

p = Pvn()
p.eating()
p.singing()
p.playing()