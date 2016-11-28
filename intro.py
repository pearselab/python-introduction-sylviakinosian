#1. Write a loop that prints out the numbers 20 to 10

x = range(20, 9, -1)

for i,each in enumerate(x):
    print(x[i])

#2. Write a list comprehension that returns the numbers from 20 to 10

[x[i] for i,each in enumerate(x)]

#3. Write a loop that prints out only even numbers from 20 to 10

for i,each in enumerate(x):
    if each % 2 == 0:
        print(each)

#4. Write a list comprehension that return only even number from 20 to 10

[each for i,each in enumerate(x) if each % 2 == 0]

#5. Write a function that determines if a number is a prime number

def prime(n):
    m = range(n-1,1,-1)
    if n == 1:
        return False
    elif n == 2:
        return True
    elif [each for i,each in enumerate(m) if n % m[i] == 0]:
        return False
    else: 
        return True

#6. Write a function that loads a text file, loops over the lines in it, and
# prints out the fifth character of the fifth line of that file

with open('silvermoon.txt') as f:
    for i, line in enumerate(f):
        if i == 4:
            print line[4]

#7. Write a loop that prints out the numbers from 1 to 20, printing "Good:
# NUMBER" if divisible by 5 and "Job: NUMBER" if the number is prime, and
# nothing otherwise

a = range(1,21)

for i,each in enumerate(a):
    if prime(each) is True and each % 5 == 0:
        print 'Good: ' + str(each)
        print 'Job: ' + str(each)
    elif prime(each) is True:
        print 'Good: ' + str(each)
    elif each % 5 == 0:
        print 'Job: ' + str(each)
    else:
        continue
    
#8. Write a function that calculates population size using the Gompertz curve

import math

def gomp(a, b, c, t):
    pop = a * exp(-b * exp(-c * t))
    return pop

#9. Write a function that draws a box of specified width and height

def box(w,h):
    print '*'*h
    for i in range(0,h-1):
        print '*' + ' '*(w-2) + '*'
    print '*'*h

#10. Implement a point class that holds x and y information for a point

class point:
    def __init__(self, x, y):
        self.x, self.y = x, y

point1 = point(5,4)

#11. Write a distance method that calculates the distance between two points in space

from math import sqrt

point2 = point(3,7)

def dist(p1, p2):
    d = sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)
    return d

dist(point1, point2)

#12. Implement a line class that takes two point objects and makes a line
# between them

class line:
    def __init__(self, p1, p2):
        self.p1, self.p2, = p1, p2

    def dist():
        d = sqrt((self.p2.x - self.p1.x)**2 + (self.p2.y - self.p1.y)**2)
        #print 'The distance between these two points is ' + str(d)
        return d

line1 = line(point1, point2)

