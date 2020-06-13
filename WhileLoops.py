""" Program to describe the while loops """


# program to print the pattern
def a():
    i = 1
    while i <= 4:
        print("#", end=" ")
        j = 1
        while j <= 4:
            print("#", end=" ")
            j = j + 1
        i = i + 1
        print()


# program to print the numbers from 1 to 100 which are not divisible by 3 and 5
def b():
    i = 1
    while i <= 100:
        if i % 3 != 0 and i % 5 != 0:
            print(i, end=" ")
        i = i + 1
    print()


b()
