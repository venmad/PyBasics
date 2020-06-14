# Program to print the different patterns
def a():
    for i in range(4):
        for j in range(4):
            print("#", end=" ")
        print()


def b():
    for i in range(4):
        for j in range(i + 1):
            print("#", end=" ")
        print()


def c():
    for i in range(4):
        for j in range(4 - i):
            print(j + 1 + i, end=" ")
        print()
    # We can also print in this way
    for i in range(1, 5):
        print(i, end=" ")
        for j in range(1, 5 - i):
            print(i + j, end=" ")
        print()


def d():
    str1 = "APQR"
    str2 = "ABCD"
    for i in range(len(str1)):
        str1 = str1.replace(str1[i], str2[i])
        print(str1)


a()
b()
c()
d()
