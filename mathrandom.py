import math, random
inp= float(input("Enter a float number: "))
print("Floor: ", math.floor(inp))
print("Ceil: ", math.ceil(inp))
print("Sqr root: ", math.sqrt(inp))
inp= float(input("Enter an angle: "))
print("Sin: ", math.sin(inp))
print("Cos: ", math.cos(inp))
print("Tan: ", math.tan(inp))
inp= int(input("Enter any number: "))
print(f"Random number between 0 and {inp}: ", random.randint(0, inp))
