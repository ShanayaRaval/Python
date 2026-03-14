import math  

def circumference(radius):
    
    c = 2 * math.pi * radius
    
    return c   


r = float(input("Enter the radius of the circle: "))  
result = circumference(r)  

print("Circumference of the circle is:", result)  