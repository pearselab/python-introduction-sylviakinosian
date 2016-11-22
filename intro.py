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
    

