"""Program to explain the various
conditional statement"""


def a():
    a = int(input("Enter a number: "))
    print("The Entered Number is ", a)
    if a >= 0:
        print('The Entered Number is positive')
    else:
        print('The Entered Number is Negative')


def b():
    """Program to print the largest of three numbers"""
    a = int(input('Enter the first number: '))
    b = int(input('Enter the second number '))
    c = int(input('Enter the third number '))
    if a >= b and a >=c:
        print('The largest number is ', a)
    elif b >= a and b >= c:
        print('The largest number is ', b)
    else:
        print('The largest number is ', c)

a()
b()
print(b.__doc__)  # To print the doc string
