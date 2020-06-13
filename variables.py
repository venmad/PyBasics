# program to describe the different types of variables

a = 5
print(a, "is a type of ", type(a))

b = 5.0
print(b, "is a type of ", type(b))

c = 3 + 4j
print(c, "is a type of ", type(c))
print("The real part of ", c, "is", c.real)
print("The Imaginary part of", c, "is", c.imag)

print(c, "is a complex number?", isinstance(c, complex))
print(b, "is a integer?", isinstance(b, int))
print(b, "is a float number?", isinstance(b, float))

# To import only a specific module use from keyword
from math import pi, cos

print(pi)
print(cos(0))

# Global and Local variables
globvar = 10


def read1():
    print('The Global variable value is', globvar)


def write1():
    global globvar  # calling the variable as global keyword
    globvar = 5  # updating the global variable value
    print('In write1 function, the value of globvar is ', globvar)


def write2():
    # The value of global variable is updated in the above method by using the global keyword
    print('The value of global variable is now calling from write2 function ', globvar)


# Local variable
def outer_func():
    a = 12

    def inner_func():
        nonlocal a
        a = 13
        print('The value of a in Inner Function', a)

    inner_func()
    print('The value of a in Outer Function', a)


read1()
write1()
write2()
outer_func()
