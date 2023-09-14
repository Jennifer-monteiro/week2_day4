import math

def circumference(radius):
    return 2 * math.pi * radius
radius = float(input("Enter circle's radius: "))
circle_circumference = circumference(radius)
print(f"The radius is: {circle_circumference:.2f}")
