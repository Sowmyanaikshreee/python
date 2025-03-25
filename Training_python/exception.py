x = input("Enter x value")
y = input("Enter y value")
try:
    z = int(x) / int(y)
except Exception as e:
    z=None
print("Division is", z)