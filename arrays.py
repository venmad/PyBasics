# Program to describe the usage of arrays
from array import *


def a():
    vals = array('i', [9, 6, 1, 14, 5])
    for i in vals:
        print(i)
    for j in range(len(vals)):
        print(vals[j])


# Program to copy an array
def b():
    vals = array('i', [1, 2, 3, 4])
    newArr = array(vals.typecode, (a * a for a in vals))  # Copying the array and squaring with same number
    print("Old array values are ", vals)
    print("New Array values are")
    for i in newArr:
        print(i)


def c():
    vals = array('i', [5, 2, 1, 8])
    vals.reverse()
    print("The reverse of array is ", vals)
    vals = sorted(vals)
    print("The sorted values are ", vals)

def d():
    arr = array('i', [])  # Defining an empty array
    n = int(input("Enter the length of array"))
    for i in range(n):
        vals = int(input("Enter the next value"))
        arr.append(vals)
    print(arr)

    # To search for an index of the value
    srch = int(input("Enter the value to search for the index"))

    k = 0
    for i in range(len(arr)):
        if arr[i] == srch:
            print(k)
            break
        k += 1

    print(arr.index(srch))  # To print using built in function

def e():
    arr = array('i', [])  # Defining an empty array
    n = int(input("Enter the length of array"))
    for i in range(n):
        vals = int(input("Enter the next value"))
        arr.append(vals)
    print(arr)
    rem = int(input("Enter the index value to remove"))
    #arr = array('i',[1, 45, 89, 3, 54])
    #arr.remove(arr[2])
    #print(arr)
    myarr = array(arr.typecode,[])
    for i in range(len(arr)):
        if i == rem:
            continue
        else:
            myarr.append(arr[i])
    print(myarr)

def f():
    arr = array('i',[1, 5, 85, 65])
    myarr = array(arr.typecode, [])
    for i in range(len(arr)-1,-1,-1):
            myarr.append(arr[i])
    print(myarr)
    arr.reverse()
    print(arr)



# a()
# b()
# c()
# d()
e()
# f()
