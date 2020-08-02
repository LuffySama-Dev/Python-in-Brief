"""
# Lets start with basic program
# Our very own Hello World
# Its very easy in python unlike C++ or Java. You just have to Print "Hello World"
# Program_1
"""
"""
print("Hello World !")
"""
#####################################################################################################################
"""
# Lets move forward with other favourite basic programs like Addition, Substraction, Multiplication, Division, etc
# Program_2
a = 6
b = 5
# Addition
c = a+b
# Substraction
d = a-b
# Multiplication
e = a*b
# Division
if (b>0):
    f = a/b
else:
    print("Can't Divide By Zero")

print("Addition = " + str(c) )
print("Substraction = " + str(d) )
print("Multiplication = " + str(e) )
print("Division = " + str(f) )

# We use if else for Division as denominatior can't be zero
"""
#####################################################################################################################
"""
# How will you print list of first 10 natural Numbers?
# Its simple.
# Python has made it simple for us.
l = list(range(11))
print("List of first 10 natural numbers is : " + str(l))

# Remember: "Range Start from 0 and not from 1."
"""
#####################################################################################################################
"""
# For Loops
# Print Square of first 10 Numbers
for i in range(10):
    print("Square of ", i, "is", i*i)
print("Done")

# See as simple as it could be
"""
#####################################################################################################################
"""
# Functions
# Our next point is Functions
# Functions are the most important part of programs. Using functions we can organinze our program easily
# Example:- Lets fins the average of the 2 numbers.
# First we will take the count of Numbers
def avg(x):
    sum = 0
    aveg = 0
    for i in range(x):
        sum = sum + i
    aveg = sum / x
    return aveg
    print(aveg)

avg(3)
"""
####################################################################################################################
"""
# Working with ARRAYS
# Arrays are used to represent the matrices .
# You will learn about importing packages.
# Here lets import numpy
# importing packages is easy
# Make sure you have required packages installed. TO install just type "pip install numpy" in your cmd
# Numpy package is popular and contains some useful stuff, like arrays and an ability to do calculations with them
import numpy
a= numpy.zeros([3,2])
#print(a)
# SO now we have created an array of shape 3 by 2
# Now we can modify our array
a[0,0] = 1
a[0,1] = 2
a[1,0] = 9
a[2,1] = 10
print(a)
# So now we can see the difference. We have replaced the values.
# Now if we have to look the value of array at certain posistion, how will we do that ?
# We can do it like this
print(a[0,1])
# OR
v = a[0,1]
print(v)
# So overall its the same. In first we are printing the value directly and in second we are
# If we try to look up an array element that doesn't exist we will get an error wiz. Index out of bound
"""
####################################################################################################################
"""
# Let's now learn to plot Array
# For plotting we will use Matplotlib
import numpy
a= numpy.zeros([3,2])
a[0,0] = 1
a[0,1] = 2
a[1,0] = 9
a[2,1] = 10
import matplotlib.pyplot
matplotlib.pyplot.imshow(a, interpolation="nearest")
"""
####################################################################################################################
"""
# Now lets Begin with objects
# What are the objects:-
# Objects are similar to the reusable functions brcause we define them once and use them many time.
# Example:
class Dog:
    def bark(self):
        print("Woof!")

Rocky = Dog()
Rocky.bark()

# We have created an object of class rocky. Now using rocky we can call the function in the class .
# Objects are instance of te class
# Another Example
class Dog:
    def __init__(self, petname, temp):
        self.name = petname
        self.temperature = temp

    def status(self):
        print("Dog name is ", self.name)
        print("Dog temperature is ", self.temperature)

    def serTemperature(self,temp):
        self.temperature = temp

    def bark(self):
        print("Woof!")

rocky = Dog("Rocky", 36)
rocky.status()
rocky.serTemperature(40)
rocky(status)
"""

####################################################################################################################
