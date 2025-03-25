class Accident(Exception):
    def __init__(self, msg):
        self.msg = msg
    def print_exception(self):
        print("user exception:" ,self.msg)
       


try:
    raise Accident("crash between 2 cars")
except Accident as e:
    print(e)