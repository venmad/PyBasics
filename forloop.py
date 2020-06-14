# Program to define the usage of for loop
def a():
    x = [1, 'venu', 5.5]
    for i in x:
        print(i)


def b():
    for i in (1, 'venumadhav', 6.3):
        print(i)


# program to print the perfect square numbers
import math


def c():
    for i in range(1,501):
        a = math.sqrt(i)
        if i % a == 0:
            print(i, end=" ")
    print()


# Program to iterate through a list using indexing

def d():
    genre = ['pop', 'jazz', 'rock']
    for i in range(len(genre)):
        print("I like", genre[i])


a()
b()
c()
d()
