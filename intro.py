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
        return False #"1 isn't a prime number, dude"
    elif n == 2:
        return True #"2 be prime, yo"
    elif [each for i,each in enumerate(m) if n % m[i] == 0]:
        return False #"DIS NOT PRIME, FOOL"
    else: 
        return True #str(n) + " be prime, yo"

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
    if each % 5 == 0:
        print 'Good: ' + str(each)
    elif prime(each) is True:
        print 'Job: ' + str(each)

# figure out how to get 5 to print for Job
    
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

#12. Implement a line class that takes two point objects and makes a line
# between them

class line:
    def __init__(self, x1, y1, x2, y2):
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
    p1 = (self.x1, self.y1)
    p2 = (self.x2, self.y2)
    def draw(p1, p2):
        d = sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
        print 'The distance between ' + str(point1) + ' and ' + str(point2) + ' is ' + str(d)

