import math
print("Two dimensional distance: ")
p1= eval(input("Enter the x,y for first point: "))
p2= eval(input("Enter the x,y for second point: "))
d= math.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)
print("DIstance= ",d)
print("Three dimensional distance: ")
p1= eval(input("Enter the x,y,z for first point: "))
p2= eval(input("Enter the x,y,z for second point: "))
d= math.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2+(p2[2]-p1[2])**2)
print("DIstance= ", d)
