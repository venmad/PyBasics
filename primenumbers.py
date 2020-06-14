# Program to check the prime number
def a():
    a = int(input("Enter a number "))
    if a % 2 == 0 or a == 1:
        print("Not a Prime Number")
    else:
        print("Prime Number")

# program to print the prime numbers between the intervals
def b():
    a = int(input("Enter the First Interval "))
    b = int(input("Enter the Last Interval "))

    for num in range(a, b + 1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                print(num)


def c():
    a = int(input("Enter the First Interval "))
    b = int(input("Enter the Last Interval "))

    for i in range(a, b + 1):
        if i == 2:
            print(i)
        elif i == 1 or i % 2 == 0:
            continue
        else:
            print(i)


#a()
#b()
c()
