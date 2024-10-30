from math import *

value = int(input("Enter the value: "))
element = input("Enter the element; Radius(r), Diametr(d), Length(l), Surface(s) -> ")


if element == "r":
    diameter = 2*value
    length = 2*pi*value
    surface = pi*pow(2, value)
    print("Given value is Radius;\nRadius is {}, Diameter is {}, Length is {}, Surface is {}".format(value, diameter, length, surface))

elif element == "d":
    radius = value/2
    length = 2*pi*radius
    surface = pi*pow(2, radius)
    print("Given value is Diameter;\nRadius is {}, Diameter is {}, Length is {}, Surface is {}".format(radius, value, length, surface))

elif element == "l":
    radius = value/(2*pi)
    diameter = 2*radius
    surface = pi*pow(2, radius)
    print("Given value is Length;\nRadius is {}, Diameter is {}, Length is {}, Surface is {}".format(radius, diameter, value, surface))

elif element == "s":
    radius = sqrt(value/pi)
    diameter = 2*radius
    length = 2*pi*radius
    print("Given value is Surface;\nRadius is {}, Diameter is {}, Length is {}, Surface is {}".format(radius, diameter, length, value))
    
else:
    print("Error. Please write value or element correctly!")