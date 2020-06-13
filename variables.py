# program to describe the different types of variables

a = 5
print(a, "is a type of ", type(a))

b = 5.0
print(b, "is a type of ", type(b))

c = 3+4j
print(c, "is a type of ", type(c))
print("The real part of ", c, "is", c.real)
print("The Imaginary part of", c , "is", c.imag)

print(c, "is a complex number?", isinstance(c,complex))
print(b, "is a integer?", isinstance(b,int))
print(b, "is a float number?", isinstance(b,float))

# To import only a specific module use from keyword
from math import pi,cos
print(pi)
print(cos(0))