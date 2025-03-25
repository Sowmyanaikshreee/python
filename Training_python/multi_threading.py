import threading

def calc_square(numbers):
    print(" perform square of numbers")
    for i in numbers:
        print("square:", i*i)

def calc_cube(numbers):
    print(" perform cube numbers")
    for i in numbers:
        print("cube:", i*i*i)

arr = [1,2,3,4,5,6]

t1 = threading.Thread(target=calc_square, args=(arr,))
t2 = threading.Thread(target=calc_cube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print(" Printing is ready")