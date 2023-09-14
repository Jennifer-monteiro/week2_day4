import math
def square_footage(length, width):
    return length * width

length = float(input("House length: "))
width = float(input("House width: "))

house_sqft= square_footage(length, width)
print(f"The house's square footage is: {house_sqft:.2f} SQFT.")