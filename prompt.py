# program to explain the usage of prompt inputs
def a():
    x = int(input('Enter the First Number'))
    y = int(input('Enter the second Number'))
    z = x + y
    print('The sum of tow number is ', z)


# Fetch the character index
def b():
    ch = input('Enter a character')
    print(ch[0])


# Pass inputs via arguments

import sys


def c():
    x = sys.argv[1]
    y = sys.argv[2]
    z = x + y
    print(z)

# calling the above functions
a()
b()
#c()
