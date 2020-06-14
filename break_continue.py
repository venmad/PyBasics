# program to print the first 50 fibonacci numbers
def a():
    a = 0
    b = 1
    print(a, b, end=" ")
    for i in range(50):
        c = a + b
        a = b
        b = c
        print(c, end=" ")
    print()


def b():
    list = [0, 1]
    for i in range(50):
        list.append(list[-1] + list[-2])
    for i in list:
        print(i, end=" ")
    print()


def c():
    a = int(input('Enter a number to verify whether it is prime or non-prime? '))
    if a % 2 == 0:
        print("The Entered Number is a prime number")
    else:
        print("The Entered Number is not a prime number")


# Program to print the prime numbers
def d():
    for i in range(10):
        if i % 2 != 0:
            continue
        else:
            print(i)

def e():
    for i in range(5):
        if i == 3:
            break  # break statement stops the execution
        print("Break Statement,", i)
    for i in range(7):
        if i == 4:
            continue  # continue statement skips that expression when it met that condition
        print("Continue Statement,", i)


# program for usage of pass variable
def f():
    pass  # when we don't have any statements to execute then simply define pass variable


a()
b()
#c()
#d()
e()
